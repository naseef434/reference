from django.shortcuts import render
from app1 import serilizers
from app1.models import Movies
from app1.serilizers import MovieSerilizer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework .decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

# @api_view(['GET'])
# def movie_lists(request):
#     query = Movies.objects.all()
#     serializer = MovieSerilizer(query, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def movie_list(request):
#     serializer = MovieSerilizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({
#             "status" : status.HTTP_201_CREATED,
#             "message" : "new movie added",
#             "data" : serializer.data
#         })
#     return Response(serializer.errors)


class Movie_list(APIView):
    def get(self,request):
        queryset = Movies.objects.all()
        serializer = MovieSerilizer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = MovieSerilizer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({
            "status" : status.HTTP_201_CREATED,
            "message" : "new movie added",
            "data" : serializer.data
           })
        return Response(serializer.errors)

class MovieDetails(APIView):
    def get(self,request,pk):
        try:
           queryset = Movies.objects.get(id=pk)
           serilizers = MovieSerilizer(queryset)
           return Response(serilizers.data)
        except Movies.DoesNotExist:
            return Response({
            "message" : f"{pk} nout found",
            "status" : status.HTTP_204_NO_CONTENT,
            
           })

    def put(self,request,pk):
        try:
           queryset = Movies.objects.get(id=pk)
           serilizers = MovieSerilizer(queryset,data=request.data)
           if serilizers.is_valid():
               serilizers.save()
               return Response(serilizers.data)
        except Movies.DoesNotExist:
            return Response({
            
            "message" : f"{pk} nout found",
            "status" : status.HTTP_201_CREATED,
            
           })
