from rest_framework import serializers, viewsets

from application.models.configuration.config import Config as ApiModel


class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiModel
        fields = ['id', 'key', 'value']


class ViewSet(viewsets.ModelViewSet):
    queryset = ApiModel.objects.all()
    serializer_class = Serializer
