from django.urls import path

from rest_framework import routers
from .views import To_do_list
from .views import index


router = routers.DefaultRouter()
router.register('To_do_list',To_do_list)

urlpatterns = [
    path('', index, name='index'),
]

urlpatterns += router.urls

