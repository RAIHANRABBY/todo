from time import time, timezone
from tkinter import Widget
from django.db import models
from  django import forms

# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=20,null=False,blank=False)
    description = models.TextField()
    date = models.DateField()
    create = models.DateTimeField(auto_now_add=True)

    # to use the ordering. ordering the posts
    class Meta:
        ordering = ['-create']

    def __str__(self):
        return self.title