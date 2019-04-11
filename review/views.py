from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ReviewCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer

    def get_client_ip(self,request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        # if x_forwarded_for:
        #     ip = x_forwarded_for.split(',')[0]
        # else:
        ip = request.META.get('REMOTE_ADDR')
        return ip

    def perform_create(self, serializer):
        print(self.get_client_ip(self.request))
        check = Review.objects.filter(user=self.request.user, company=serializer.validated_data.get('company'))
        if not check:
            serializer.save(user=self.request.user,ip_address=self.get_client_ip(self.request))

    def get_queryset(self):
        queryset = Review.objects.filter(user=self.request.user)
        return queryset



class CompanyCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
