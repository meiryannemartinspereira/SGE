from rest_framework import serializers
from inflows.models import Outflow

class OutflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outflow
        fields = '__all__'