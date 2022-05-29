import imp
from django.shortcuts import render
from app1 import serilizers
from app1.models import Movies, Review,StreamingPlaform
from app1.serilizers import MovieSerilizer, ReviewSerializer,StreamingPlaform, StreamingSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework .decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self,request,*args, **kwargs):
#         return self.list(request,*args, **kwargs)
#     def post(self,request,*args, **kwargs):
#         return self.create(request,*args, **kwargs)

# class ReviewDetails(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request,*args, **kwargs)


class StreamingPlatfromList(APIView):
    def get(self,request):
        query = StreamingPlaform.objects.all()
        serilizers_class = StreamingSerializer(query, many=True,context={'request': request})
        return Response(serilizers_class.data)
    def post(self,request):
        serilizers = StreamingSerializer(data=request.data)
        if serilizers.is_valid():
            serilizers.save()
            return Response(serilizers.data,status=status.HTTP_201_CREATED)
        return Response(serilizers.errors)

class Movie_list(APIView):
    def get(self,request):
        queryset = Movies.objects.all()
        serializer = MovieSerilizer(queryset,many=True,)
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
