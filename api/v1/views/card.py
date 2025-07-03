from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response


from api.v1.serializers.card import CardSerializer
from card.models import Card


class CardAPIView(APIView):
    serializer_class = CardSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    parser_classes = [JSONParser]

    def get(self,request):
        
        cards = Card.objects.all()
        serializer = self.serializer_class(cards, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
        
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        pass