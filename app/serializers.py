from .models import*
from rest_framework import serializers


class GalarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Galary
        fields = '__all__'