from django.urls import path

from rest_framework import routers
from .views import To_do_list


router = routers.DefaultRouter()
router.register('To_do_list',To_do_list)

urlpatterns = router.urls