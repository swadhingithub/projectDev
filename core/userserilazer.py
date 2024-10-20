from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from Students.models import Team, Project, Report,TeamRequest,StudentProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from Students.models import StudentProfile
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, required=True)
    password2 = serializers.CharField(write_only=True, min_length=8, required=True)
    role=serializers.ReadOnlyField()


    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2','role')
        read_only_fields = ['id','date_joined','role']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        validated_data['role'] = 'student'
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerilizer(serializers.Serializer):
   username = serializers.CharField(required=True)
   password = serializers.CharField(write_only=True, required=True)


