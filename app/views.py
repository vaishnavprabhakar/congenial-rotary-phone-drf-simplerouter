from .serializer import UserSerializer
from django.contrib.auth.models import User 
# Create your views here.
from rest_framework import viewsets



class UserSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)