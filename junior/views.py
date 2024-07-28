from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Ticket
from .serializers import EventSerializer,TicketSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
 
 
class eventlist(APIView):
 
    def get(self,request):
        book1 = Event.objects.all()
        serializer = EventSerializer(book1, many= True)
        return Response(serializer.data) 
 
    def post(self):
        pass

class ticketlist(APIView):
 
    def get(self,request):
        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket, many= True)
        return Response(serializer.data) 
 
    def post(self):
        pass

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)