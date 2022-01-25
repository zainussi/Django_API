from rest_framework import serializers
from .models import QA

class QASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QA
        fields = ('__all__')