from asyncore import read
from dataclasses import fields
from xml.parsers.expat import model
from rest_framework import serializers
from app1.models import Movies,StreamingPlaform,Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class MovieSerilizer(serializers.ModelSerializer):
    on_showing = serializers.SerializerMethodField()
    review = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'

    class Meta:
        model = Movies
        fields = '__all__'
        # exclude = ['story_line']
    
    #field level validation shoud give the field name after validate method
    # def validate_discription(self,value):
    #     if len(value) > 10 : 
    #         raise serializers.ValidationError("name is too big")
    #     return value

    #object level validations
    def validate(self, data):
        if len(data['name']) == len(data['story_line']):
            raise serializers.ValidationError("Movie name and Discription are equal!")
        elif len(data['name']) > 10 : 
            raise serializers.ValidationError("name is too big")
        return data



    def get_on_showing(self,data):
        onshow = "Now Streaming!"
        return onshow

class StreamingSerializer(serializers.ModelSerializer):
    movies = MovieSerilizer(many=True,read_only=True)
    
    class Meta:
        model = StreamingPlaform
        fields = '__all__'
        #exclude = ['about']

