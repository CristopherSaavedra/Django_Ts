from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DistritoListView(generics.ListAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer

class ReporteListView(generics.ListAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class RegisterDistritoAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DistritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Distrito registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegisterReporteAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReporteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Reporte registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class ReporteCreateView(generics.CreateAPIView):
#     queryset = Reporte.objects.all()
#     serializer_class = ReporteSerializer

class RegisterClientAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginClientAPIView(APIView):
   def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            
            if user.check_password(password) and user.is_client:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)