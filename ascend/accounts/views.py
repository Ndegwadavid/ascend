from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@ensure_csrf_cookie
def register_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login_view')
        else:
            for field, errors in serializer.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    return render(request, 'accounts/register.html')

@ensure_csrf_cookie
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            response = redirect('dashboard')
            response.set_cookie('refresh_token', str(refresh), httponly=True, samesite='Strict')
            response.set_cookie('access_token', str(refresh.access_token), httponly=True, samesite='Strict')
            return response
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'accounts/login.html')

@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_logout(request):
    try:
        refresh_token = request.COOKIES.get('refresh_token')
        token = RefreshToken(refresh_token)
        token.blacklist()
        response = Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)
        response.delete_cookie('refresh_token')
        response.delete_cookie('access_token')
        return response
    except Exception as e:
        return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

def logout_view(request):
    logout(request)
    response = redirect('login_view')
    response.delete_cookie('refresh_token')
    response.delete_cookie('access_token')
    messages.success(request, "You have been logged out.")
    return response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

token_obtain_pair = TokenObtainPairView.as_view()
token_refresh = TokenRefreshView.as_view()

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"success": "CSRF cookie set"})