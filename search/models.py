# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
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