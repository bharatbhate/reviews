from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
#
# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = ('name',)

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    #company = CompanySerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", )

