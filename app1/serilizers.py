from rest_framework import serializers
from app1.models import Movies
class MovieSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        #fields = ['id','name','discription']
        exclude = ['discription']
    
    #field level validation shoud give the field name after validate method
    # def validate_discription(self,value):
    #     if len(value) > 10 : 
    #         raise serializers.ValidationError("name is too big")
    #     return value

    #object level validations
    def validate(self, data):
        if len(data['name']) == len(data['discription']):
            raise serializers.ValidationError("Movie name and Discription are equal!")
        elif len(data['name']) > 10 : 
            raise serializers.ValidationError("name is too big")
        return data