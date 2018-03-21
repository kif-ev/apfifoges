from django.contrib import admin

# Register your models here.
from .models import University, Program

admin.site.register(University)
admin.site.register(Program)