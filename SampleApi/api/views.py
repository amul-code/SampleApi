# from django.shortcuts import render
# import json
from rest_framework.decorators import api_view
# from django.http import HttpResponse
# from rest_framework.request import Request
from rest_framework.response import Response
from api import serializers, models
from rest_framework.parsers import JSONParser
import json

from rest_framework.generics import RetrieveAPIView, ListAPIView , UpdateAPIView, RetrieveUpdateAPIView
# Create your views here.


class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

@api_view()
def articleApi(request):
    articles = models.Articles.objects.all()
    response = serializers.ArticleSerializer(articles, many=True)
    return Response(response.data)

@api_view(['POST'])
def createarticleApi(request):
    body = json.loads(request.body)
    response = serializers.ArticleSerializer(data = body)
    if response.is_valid():
        
        inst = response.save()
        response = serializers.ArticleSerializer(inst)
        return Response(response.data)
    return Response(response.errors)
@api_view()
def usersApi(request):
    # users = [
    #     {
    #         "name": "AMul rathore",
    #         "Designation": "Developer"
    #     },
    #     {
    #         "name": "Bunty",
    #         "Designation": " Java Developer"
    #     },
    # ]
    student = Student("Amul", 1, 100)
    student1 = Student("baba", 2, 120)
    student2 = Student("bunty", 3, 300)
    student3 = Student("aayush", 4, 700)
    response = serializers.StudentSerializer(
        [
            student,
            student1,
            student2,
            student3,
        ], many =True
    )
    return Response(response.data)

class ArticlesListView(ListAPIView):
    queryset = models.Articles.objects.all()
    serializer_class = serializers.ArticleSerializer
    def get_queryset(self):
        query = {}
        for key, value in self.request.GET.items():
            query["{}__icontains".format(key)] = value
        return models.Articles.objects.filter(**query)

class ArticlesDetailView(RetrieveAPIView):
    queryset = models.Articles.objects.all()
    serializer_class = serializers.ArticleSerializer

    # def post(self, request):
    #     return  Response(request, body)