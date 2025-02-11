from django.contrib import admin


#register your model here.
from .models import *
admin.site.register(Employees)