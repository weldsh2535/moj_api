from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from solutions.models import Solution
from solutions.serializers import SolutionSerializer


# Create your views here.
@api_view(['POST'])
def create_solution(request):
    solutions = request.data
    solution_serializer = SolutionSerializer(data=solutions)
    if solution_serializer.is_valid():
        solution_serializer.save()
        return Response(solution_serializer.data, status=status.HTTP_201_CREATED)

    return Response(solution_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def create_solution_view(request):
    print(request.data)
    Solution.objects.create(
        UserId = request.data.get('UserId'),
        reportId = request.data.get('reportId'),
        brand = request.data.get('brand'),
        model = request.data.get('model'),
        happenedProblem = request.data.get('happenedProblem'),
        sole = request.data.get('sole'),
        startDate = request.data.get('startDate'),
        endDate = request.data.get('endDate'),
        isProblemFixed = request.data.get('isProblemFixed'),
        reasonProblemNotFixed = request.data.get('reasonProblemNotFixed'),
        itTechName = request.data.get('itTechName')
    )
@api_view(['GET'])
def get_solution(request):
    solutions = Solution.objects.all()
    solution_serializer = SolutionSerializer(solutions, many=True)
    return Response(solution_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_solution_by_id(request, pk):
    solution = Solution.objects.get(id=pk)
    try:
        solution_serializer = SolutionSerializer(solution)
        return Response(solution_serializer.data, status=status.HTTP_200_OK)
    except Solution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_solution_by_report_id(request, report_id):
    solution = Solution.objects.get(reportId=report_id)
    try:
        solution_serializer = SolutionSerializer(solution)
        return Response(solution_serializer.data, status=status.HTTP_200_OK)
    except Solution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_solution(request, pk):
    solution = Solution.objects.get(id=pk)
    solution_serializer = SolutionSerializer(solution, data=request.data)
    if solution_serializer.is_valid():
        solution.save()
        return Response(solution_serializer.data, status=status.HTTP_200_OK)

    return Response(solution_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_solution(request, pk):
    solution = Solution.objects.get(id=pk)
    solution.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_solutions_by_report_id(request,report_id):
    solutions = Solution.objects.get(reportId= report_id)
    solution_serializer = SolutionSerializer(solutions, many=True)
    return Response(solution_serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_solutions_by_report_id(request,report_id):
    solutions = Solution.objects.get(reportId=report_id)
    solution_serializer = SolutionSerializer(solutions, data=request.data)
    if solution_serializer.is_valid():
        solutions.save()
        return Response(solution_serializer.data, status=status.HTTP_200_OK)

    return Response(solution_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_solutions_by_report_id(request,report_id):
    solutions = Solution.objects.get(reportId=report_id)
    solutions.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_solutions_by_user_id_reports(request,user_id):
    try:
        solutions = Solution.objects.filter(UserId=user_id)
        solution_serializer = SolutionSerializer(solutions, many=True)
        return Response(solution_serializer.data, status=status.HTTP_200_OK)
    except Solution.DoesNotExist as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)




