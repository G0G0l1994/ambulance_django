from functools import partial
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser,FormParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from api.v1.serializers.card import CardDetailSerializer, CardCreateSerializer,CardUpdateSerializer, CardListSerializer
from card.models import Card


class CardDetailAPIView(APIView):
    serializer_class = CardDetailSerializer
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser,FormParser]
    permission_classes = [IsAuthenticated]

    def get(self,request, card_id=None):
        
        user = request.user
        cards = Card.objects.filter(id=card_id, doctor_id = user.id)
        serializer = self.serializer_class(cards)
        
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

    def patch(self, request, card_id):
        try:
            card = Card.objects.get(id=card_id)
        except Card.DoesNotExist:
            return Response({'detail': "Card not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(card, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CardListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):

        cards = Card.objects.all().order_by('-id')
        serializer = CardListSerializer(cards,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)