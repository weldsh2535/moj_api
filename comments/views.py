from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from comments.models import Comment
from comments.serializers import CommentSerializer


# Create your views here.

@api_view(['POST'])
def create_comment(request):
    comment_data = request.data
    comment_serializer = CommentSerializer(data=comment_data)
    if comment_serializer.is_valid():
        comment_serializer.save()
        return Response(comment_serializer.data, status=status.HTTP_201_CREATED)

    return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_comment(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_comments(request,pk):
    comments = Comment.objects.get(commentId=pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_comments(request,pk):
    comments = Comment.objects.get(commentId=pk)
    serializer = CommentSerializer(instance=comments, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_comments(request,pk):
    comments = Comment.objects.get(commentId=pk)
    comments.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



