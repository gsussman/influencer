# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.search
        
class Email(models.Model):
    email = models.EmailField(max_length=250)
    
    def __str__(self):
        return self.email