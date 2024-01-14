from django.contrib.auth import get_user_model
from rest_framework import serializers
from app.models import Buck

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(max_length=None, use_url=False, required=False)

    class Meta:
        model = User
        exclude = ['password', "groups", "user_permissions"]
        read_only_fields = ['username']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('username'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'))
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class BuckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buck
        fields = '__all__'
        extra_kwargs = {'owner': {'read_only': True}}
