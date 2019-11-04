from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . import serializers
from . import models

# class HeroViewSet(viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('name')
#     serializer_class =  HeroSerializer

@api_view(['GET',])
def hero_wiew(request):
    if request.method == 'GET':
        try:
            hero_query = models.Hero.objects.all().order_by('name')
        except models.Hero.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.HeroSerializer(hero_query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)