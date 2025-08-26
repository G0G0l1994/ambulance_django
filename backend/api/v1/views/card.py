from functools import partial
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser,FormParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from api.v1.serializers.card import CardDetailSerializer, CardCreateSerializer,CardUpdateSerializer, CardListSerializer, MKBSerializer
from card.models import Card,MKB


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
        print(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CardListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request, user_id = None):

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
            serializer = CardListSerializer(cards,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
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
        serializer = CardListSerializer(cards,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MKBListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):

        mkb_list = MKB.objects.all()
        serializer = MKBSerializer(mkb_list, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


 