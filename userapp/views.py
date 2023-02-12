from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer , MessageSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.permissions import IsAuthenticated
from .models import Message
# Create your views here.

class apiApiView(LoginRequiredMixin,APIView):
    def get(self,request):
        return Response({ 'Message' :' Signup Api Made By Abhijit Mali '})


        
class RegisterAPIView(APIView):

    def get(self,request):
        return Response({'Message':'This is get method of signup API'},status=status.HTTP_200_OK)

    def post(self,request):
        try:
            obj =  RegisterSerializer(data =  request.data)
            if obj.is_valid():
                obj.save()
                return Response({'Message':'Successfully Signed up'},status = status.HTTP_200_OK)

            return Response(obj.errors,status = status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message':'Something Failed due to {}'.format(str(e))}, status = status.HTTP_400_BAD_REQUEST)



class MessageAPIView(APIView):

    def get(self,request):
        data = Message.objects.all()
        print(data)
        serializer = MessageSerializer(data=data)
        serializer.is_valid()
        print(serializer.data)
        return Response(serializer.data)
    def post(self, request):
        # permission_classes = (IsAuthenticated)
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)


