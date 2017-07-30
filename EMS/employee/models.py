from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=500)
    job_title = models.CharField(max_length=100)
    date_started = models.DateField(blank=True, null=True)
    job_description = models.CharField(max_length=100)
    photo = models.FileField(blank=True, null=True)
    
    
    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name

