from django.urls import path, include
from .views import ProfileView
from rest_framework import routers, urlpatterns

router = routers.SimpleRouter()
router.register(r'', ProfileView)

urlpatterns = [
    path('', include(router.urls)),
]
