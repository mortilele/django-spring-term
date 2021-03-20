from rest_framework import serializers

from users.models import UserProfile, User


class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('address',)


class UserModelSerializer(serializers.ModelSerializer):
    profile = UserProfileModelSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'profile')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])
        return user
