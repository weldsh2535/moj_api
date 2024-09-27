from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from reports.models import Report
from reports.serializers import ReportSerializer


# Create your views here.
@api_view(['POST'])
def create_report(request):
    report_data = request.data
    report_serializer = ReportSerializer(data=report_data)
    if report_serializer.is_valid():
        report_serializer.save()
        return Response(report_serializer.data, status=status.HTTP_201_CREATED)

    return Response(report_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_total_report(request):
    report = Report.objects.all().count()
    return Response(report)
@api_view(['GET'])
def get_report(request):
    report = Report.objects.all()
    serializer = ReportSerializer(report, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_report_by_username(request,username):
    report = Report.objects.filter(username=username)
    report_serializer = ReportSerializer(report, many=True)
    return Response(report_serializer.data)