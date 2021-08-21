from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
# Create your views here.
# viewsets provides the implementation for CRUD 
#Code specifies the serializer_class and the queryset
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
