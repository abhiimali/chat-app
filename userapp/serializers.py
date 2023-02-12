from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Message 


class RegisterSerializer(serializers.ModelSerializer):
    #  custom fields are used 
    first_name = serializers.CharField(max_length = 20)
    last_name =  serializers.CharField(max_length = 20)
    email = serializers.EmailField()
    username = serializers.CharField(max_length = 20)
    password =  serializers.CharField(max_length = 20)
    confirm_password = serializers.CharField(max_length = 20)

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password','confirm_password')

    def create(self,validated_data):
        del validated_data['confirm_password']
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self,value):

        if value.get('password') != value.get('confirm_password'):
            raise serializers.ValidationError('Both the passwords does not match')
        return value

# login Serialiazer 



#  Message Serializers 

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Message
        fields = ['sender', 'message' ,'timestamp']



