from rest_framework.serializers import ModelSerializer

from .models import task

class taksSerializer(ModelSerializer):
    class Meta:
        model = task
        fields = ['id','name','status']