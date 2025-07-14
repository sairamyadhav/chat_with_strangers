from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from .validators import validate_username, validate_password
from .models import AuthUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class SignInSerializer(ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = AuthUser
        fields = ['username', 'email', 'password', 'is_verified', 'is_staff']

    def validate_username(self, username):
        validate_username(username)
        return username

    def validate_password(self, password):
        validate_password(password)
        return password
    
    def create(self, validated_data):
        user = AuthUser.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['is_verified'] = user.is_verified
        return token
    
class GuestSigninSerializer(ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = AuthUser
        fields = ['username', 'password']

    def validate_username(self, username):
        validate_username(username)
        return username

    def validate_password(self, password):
        validate_password(password)
        return password
    
    def create(self, validated_data):
        user = AuthUser.objects.create_user(**validated_data)
        return user