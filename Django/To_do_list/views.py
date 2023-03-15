from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render

from .models import task
from .serializers import taksSerializer

class To_do_list(ModelViewSet):
    queryset = task.objects.all()
    serializer_class = taksSerializer


def index(request):
    return render(request,'index.html')



