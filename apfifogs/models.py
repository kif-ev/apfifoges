from django.db import models
import uuid

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
    edit_id = models.CharField(max_length=100, default=uuid.uuid1().hex, unique=True)

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.short_name




class Program(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name =  models.CharField(max_length=300)
    beginners =  models.CharField(max_length=300)
    beginners_last_year =  models.CharField(max_length=300)

    def __str__(self):
        return self.name

