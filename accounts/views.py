from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.templatetags.static import static
from rest_framework.response import Response
from rest_framework import status

from accounts.models import CustomUser, UserRatingInfo
from accounts.serializers import UserSerializer, UserRatingSerializer


# Create your views here.
@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request,username=username,password=password)
    if user:
        if user.is_active == 1:
            token, _ = Token.objects.get_or_create(user=user)
            avatar_url= None
            # if user.avatar:
            #     try:
            #         avatar_url = user.avatar.url
            #     except ValueError:
            #         avatar_url = static("avatars/default_avatar.jpg")
            user_data = {
                "firstName": user.first_name,
                "lastName": user.last_name,
                "username": user.username,
                "UserId": user.id,
                "role": user.user_type.name,
            }
            response_data = {
                "access_token": token.key,
                "username": user_data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User is not active. Please contact the administrator."}, status=status.HTTP_401_UNAUTHORIZED,)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED, )

@api_view(['GET'])
def get_login_info(request):
    login_data = CustomUser.objects.all()
    serialize = UserSerializer(login_data, many=True)
    return Response(serialize.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_rating(request):
    rating_data = request.data
    rating_serializer = UserRatingSerializer(data=rating_data)
    if rating_serializer.is_valid():
        rating_serializer.save()
        return Response({"success": rating_serializer.data}, status=status.HTTP_201_CREATED)

    else:
        return Response({"error": rating_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_rating_by_id(request, id):
    ratings = UserRatingInfo.objects.filter(id=id)
    if ratings.exists():
        data = [
            {
                'id': rating.id,
                'rating': rating.rating,
                # Add other fields here
            }
            for rating in ratings
        ]
        return Response(data, status=200)
    else:
        return Response({'error': 'Rating not found'}, status=404)
