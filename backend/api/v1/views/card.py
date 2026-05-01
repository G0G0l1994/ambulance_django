from functools import partial
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser,FormParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from django_eventstream import send_event


from api.v1.serializers.card import CardDetailSerializer, CardCreateSerializer,CardUpdateSerializer, CardListSerializer, MKBSerializer
from card.models import Card,MKB


class CardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

class CardDetailAPIView(APIView):
    serializer_class = CardDetailSerializer
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser,FormParser]
    permission_classes = [IsAuthenticated]

    def get(self,request, card_id=None):
        
        
        cards = Card.objects.select_related(
            'patient_id',
            'datetime_data',
            'common_data',
            'parameters_before_data',
            'parameters_after_data',
            'skin_data',
            'air_data',
            'heart_data',
            'stomach_data',
            'nervous_data',
            'urinary_data',
            'ecg_data',
            'aid_data',
            'diagnosis_data',
            ).prefetch_related().get(id=card_id)
        serializer = self.serializer_class(cards)
        print(serializer.data)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
        
class CardCreateAPIView(APIView):

    serializer_class = CardCreateSerializer
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser,FormParser]
    permission_classes = [IsAuthenticated]
        
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CardUpdateAPIVView(APIView):
    serializer_class = CardUpdateSerializer
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser, FormParser]
    permission_classes = [IsAuthenticated]

    

    def put(self, request, card_id):
        try:
            card = Card.objects.get(id=card_id)
        except Card.DoesNotExist:
            return Response({'detail': "Card not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(card, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(f"card {card_id} updated")
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CardListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request, user_id = None):
        paginator = CardPagination()
        if user_id:
            cards = Card.objects.filter(doctor_id=user_id).select_related(
            'patient_id',
            'doctor_id',
            'datetime_data',
            'common_data',
            'parameters_before_data',
            'parameters_after_data',
            'skin_data',
            'air_data',
            'heart_data',
            'stomach_data',
            'nervous_data',
            'urinary_data',
            'ecg_data',
            'aid_data',
            'diagnosis_data',
            ).prefetch_related().order_by('-id')
            pagator_result = paginator.paginate_queryset(cards,request, view=self)
            serializer = CardListSerializer(pagator_result,many=True)
            return paginator.get_paginated_response(serializer.data)
        cards = Card.objects.select_related(
            'patient_id',
            'datetime_data',
            'common_data',
            'parameters_before_data',
            'parameters_after_data',
            'skin_data',
            'air_data',
            'heart_data',
            'stomach_data',
            'nervous_data',
            'urinary_data',
            'ecg_data',
            'aid_data',
            'diagnosis_data',
            ).prefetch_related().all().order_by('-id')
        pagator_result = paginator.paginate_queryset(cards,request, view=self)
        serializer = CardListSerializer(pagator_result,many=True)
        return paginator.get_paginated_response(serializer.data)
        

class MKBListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):

        mkb_list = MKB.objects.all()
        serializer = MKBSerializer(mkb_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DispatchCardToCrewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        card_id = request.data.get("card_id")
        crew_number = request.data.get("crew_number")

        if not card_id or not crew_number:
            return Response(
                {"detail": "card_id and crew_number is required"}, 
                status=status.HTTP_400_BAD_REQUEST
                )
        try:
            card = Card.objects.get(id=card_id)
        except Card.DoesNotExist:
            return Response(
                {"detail": "Card not found"}, 
                status=status.HTTP_400_BAD_REQUEST
                )
        # Преобразуем crew_number в int для сохранения в Card.crew (IntegerField)
        try:
            crew_number_int = int(crew_number)
        except (ValueError, TypeError):
            return Response(
                {"detail": "Invalid crew_number format"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        card.crew = crew_number_int
        card.status = 'handed_crew'
        card.save(update_fields=['crew', "status"])

        # Формируем канал для SSE (используем строковое значение crew_number)
        channel = f"crew-{crew_number}"
        payload = {
            "type": "card_assigned",
            "card_id": card.id,
            "crew_number": crew_number,
            "doctor_id": card.doctor_id.id if card.doctor_id else None,
            "status": card.status,
            "address": card.address,
            "cause": card.cause,
            "transmission_time": datetime.now(),
            "detail_card": f"/cards/{card.id}/update",
            "update_api_url": f"/api/cards/{card.id}/update/",
            "accept_next_status": "in_progress"
        }
        send_event(channel, "new_call", payload)
        return Response(
            {"success": True, "event": payload}, 
            status=status.HTTP_200_OK
            )

        