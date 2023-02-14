from django.contrib import admin
from django.urls import path , include

# from .views import home 
# from .views import RegisterAPIView , apiApiView 

from userapp import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('' ,views.apiApiView.as_view()),
    path('register/' ,views.RegisterAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('messages/',views.MessageAPIView.as_view()),
   

]


