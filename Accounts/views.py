from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from Accounts.models import CustomUser
from school.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
