# -*- coding: utf-8 -*-
"""
User-related Views
Functional Description: Implements the core logic for processing user-related information workflows
Creation Date: 2025-09-09
Last Modified: 2025-09-09
Author: Zhan Cui
Copyright Notice: © 2025 Company Name. All rights reserved.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserRegisterSerializer, UserLoginSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                print('接口测通')
                refresh = RefreshToken.for_user(user)
                result = {
                    'user_id': user.id,   # 用户ID == 工号
                    'username': user.username,
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                    'is_staff': user.is_staff,   # 布尔值标识管理员身份
                    'permissions': self.get_user_permissions(user)  # 权限数组（示例[*]表示全权限）
                }
                return Response(result)
            return Response({'error': 'Invalid credentials'}, status=401)
        return Response(serializer.errors, status=400)
    
    def get_user_permissions(self, user):
        if user.is_superuser:
            return ['*']
        return list(user.get_all_permissions())

    