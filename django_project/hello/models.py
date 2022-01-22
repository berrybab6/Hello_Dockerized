from django.db import models

# Create your models here.
class Hello(models.Model):
    title = models.CharField(max_length=100, blank=False, primary_key=True)
    description = models.TextField(blank=True,null=True)