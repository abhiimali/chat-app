from django.contrib import admin

# Register your models here.
from userapp.models import Message


admin.site.register(Message)
