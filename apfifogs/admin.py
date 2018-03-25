from django.contrib import admin

# Register your models here.
from .models import University, Program

class ProgramsInLine(admin.StackedInline):
    model = Program
    extra = 3

@admin.register(University)
class UniversitAdmin(admin.ModelAdmin):
    inlines =  [ProgramsInLine]
    readonly_fields = ("edit_id",)
    list_display = ('short_name','name','state','edit_id')

@admin.register(Program)
class ProgrammAdmin(admin.ModelAdmin):
    list_display = ('name','university')
