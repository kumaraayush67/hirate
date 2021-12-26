from django.contrib.auth import get_user_model

from rest_framework import generics, permissions
from .serializers import SignUpSerializer

User = get_user_model()

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]