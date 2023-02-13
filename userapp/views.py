from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer , MessageSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.permissions import IsAuthenticated , AllowAny
from .models import Message
# Create your views here.

class apiApiView(APIView):
    # authentication_classes = [AllowAny]
    permission_classes = []
    def get(self,request):
        return Response({ 'Message' :' Signup Api Made By Abhijit Mali '})


        
class RegisterAPIView(APIView):
    permission_classes = []
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
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        data = Message.objects.all()
        print(data)
        serializer = MessageSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=False)
        print(serializer.data)
        return Response(serializer.data)
    def post(self, request):
        print(request.data)
        serializer = MessageSerializer(data={**request.data,"sender":request.user.username})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Message Sent'} ,status=status.HTTP_201_CREATED)

    def delete(self,request):
        id =request.query_params.get('id')
        Message.objects.filter(id=id).delete()
        return Response({'message':'Message Deleted'},status=status.HTTP_201_CREATED)



