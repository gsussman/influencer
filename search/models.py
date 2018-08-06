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
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
        
class Influencer(models.Model):
    name = models.CharField(max_length=250)
    decription = models.TextField()
    facebook = models.CharField(max_length=250, blank=True)
    twitter = models.CharField(max_length=250, blank=True)
    instagram = models.CharField(max_length=250, blank=True)
    youtube = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.name

class NicheList(models.Model):
    nichename = models.CharField(max_length=250)
    nichedescription = models.TextField(blank=True)
    influencers = models.ManyToManyField(Influencer, through = "OrderedList")
    
    def __str__(self):
        return self.nichename
        
class OrderedList(models.Model):
    list = models.ForeignKey(NicheList)
    influencers = models.ForeignKey(Influencer)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.list.nichename