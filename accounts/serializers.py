from rest_framework import serializers

from accounts.models import UserRatingInfo, CustomUser


class UserSerializer(serializers.ModelSerializer):
    UserId = serializers.CharField(source='id')
    role = serializers.CharField(source='user_type_id')
    class Meta:
        model = CustomUser
        fields = ['UserId','username','password','first_name','last_name','role']


class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRatingInfo
        fields = '__all__'