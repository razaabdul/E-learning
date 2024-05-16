from rest_framework import serializers
from .models import *
from datetime import datetime
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from django.contrib.auth.hashers import make_password


User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        # fields = ("first_name", "last_name", "password", "email")
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data.pop("email")
        password = validated_data.pop('password')
        user = User.objects.create_user(
            email=email,
            password=password,
        )
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        # Calculate expires_in
        expires_in_timestamp = refresh.access_token.payload["exp"]
        expires_in_datetime = datetime.fromtimestamp(expires_in_timestamp)
        expires_in_seconds = int((expires_in_datetime - datetime.now()).total_seconds())

        return {
            "user": user,
            "refresh_token": str(refresh),
            "access_token": access_token,
            "expires_in": expires_in_seconds,
        }

class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data.pop("email")
        password = validated_data.pop('password')
        user = User.objects.create_user(
            email=email,
            password=password,
            **validated_data
        )
        return {"user":user}

class StudentRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data.pop("email")
        password = validated_data.pop('password')
        user = User.objects.create_user(
            email=email,
            password=password,
            **validated_data
        )
        return {"user":user}

class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    # def update(self, instance, validated_data):
    #     # Exclude password field from the validated data
    #     validated_data.pop("password", None)

    #     # Update instance with the validated data
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
        
    #     # Save the instance
    #     instance.save()
    #     print(instance,'instaaaaaaaaaaaaaaaaaaaaaaa')
    #     return instance

class UserResponseSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    refresh_token = serializers.CharField()
    access_token = serializers.CharField()
    expires_in = serializers.IntegerField()

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = User.objects.filter(email=email).first()
        if user is None:
            raise serializers.ValidationError("User not found.")
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid password.")
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        expires_in_timestamp = refresh.access_token.payload["exp"]
        expires_in_datetime = datetime.fromtimestamp(expires_in_timestamp)
        expires_in_seconds = int((expires_in_datetime - datetime.now()).total_seconds())
        
        return {
            "user": user.id,
            "access_token": access_token,
            "expires_in": expires_in_seconds,
            'type':user.user_type
        }


class UserLogoutSerializer(serializers.Serializer):
    # refresh_token = serializers.CharField()

    # def logout_user(self):
    #     refresh_token = self.validated_data['refresh_token']

    #     try:
    #         token = RefreshToken(refresh_token)
    #         token.blacklist()
    #     except Exception as e:
    #         raise serializers.ValidationError('Invalid refresh token')
    access_token = serializers.CharField()

    def logout_user(self):
        access_token = self.validated_data['access_token']
        if BlacklistedToken.objects.filter(token=access_token).exists():
            raise serializers.ValidationError('Access token already blacklisted')
        BlacklistedToken.objects.create(token=access_token)
        
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class ClassDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDetails
        fields = '__all__'

class CourseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDetails
        fields = '__all__'

class CourseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSection
        fields = '__all__'

class CourseSubSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubSection
        fields = '__all__'


class CourseLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLevel
        fields = '__all__'

class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = '__all__'

class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRating
        fields = '__all__'