from django.shortcuts import render
from django.http import HttpResponse
from .models import Program, University
from django.template import loader


def index(request, university_id=None):
    if university_id:
        return HttpResponse("You want to edit {}".format(university_id))
    else:
        return HttpResponse("foooo")



def slides(request):
    university_list = sorted(University.objects.all(), key=lambda x:x.state, reverse=True)
    next = None
    for university in university_list:
        university.program_list =Program.objects.filter(university=university)
        university.next = next
        next = university.short_name

    university_list = sorted(university_list, key=lambda x:x.state)
    template = loader.get_template('slides.html')
    context = {'university_list':university_list}



    return HttpResponse(template.render(context,request))

