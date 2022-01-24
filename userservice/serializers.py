import imp
from rest_framework import serializers
from django.contrib.auth.models import User 
from userservice.models import Profile, Role
from rest_framework_simplejwt.tokens import RefreshToken

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs = {'email': {'required': True}} 
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['_id','first_name','last_name','phone_number']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['_id','isPdfDownload','apiCurrentLimit']

class UserSerializerWithProfileAndRole(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isActive = serializers.SerializerMethodField(read_only=True)

    profile = serializers.SerializerMethodField(read_only=True)
    role = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['_id','username','email','name','isActive','profile','role']

    def get__id(self, obj):
        return obj.id

    def get_isActive(self, obj):
        return obj.is_active

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name

    def get_profile(self, obj):
        profile = obj.profile_set.all()
        serializer = ProfileSerializer(profile, many=True)
        return serializer.data

    def get_role(self, obj):
        role = obj.role_set.all()
        serializer = RoleSerializer(role, many=True)
        return serializer.data

