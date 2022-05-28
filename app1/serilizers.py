from rest_framework import serializers
from app1.models import Movies
class MovieSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

    #field level validation shoud give the field name after validate method
    def validate_name(self,value):
        if len(value) > 10 : 
            raise serializers.ValidationError("name is too big")
        return value