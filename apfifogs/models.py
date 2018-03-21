from django.db import models

class University(models.Model):
    name = models.CharField(max_length=300)
    short_name = models.CharField(max_length=50)
    town = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    name_of_fachschaft = models.CharField(max_length=300)
    type_of_organisation = models.CharField(max_length=300)
    amount_all_students = models.CharField(max_length=300)
    amount_represented_students = models.CharField(max_length=300)
    amount_activ_fachschaftler =  models.CharField(max_length=300)

class Program(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name =  models.CharField(max_length=300)
    beginners =  models.CharField(max_length=300)
    beginners_last_year =  models.CharField(max_length=300)

