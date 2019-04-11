from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ReviewCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        check = Review.objects.filter(user=self.request.user, company=serializer.validated_data.get('company'))
        if not check:
            serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Review.objects.filter(user=self.request.user)
        return queryset


class CompanyCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
