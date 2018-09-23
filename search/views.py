# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Search, Email, OrderedList, Influencer, NicheList
from forms import PostForm, UserForm, ProfileForm
import operator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
from django.contrib import messages

from django.db.models import Q

# Create your views here.
def home(request):
    if request.method == 'POST':
        result = request.POST
        searchreq = result['search']
        print (result['search'])
        a = Search(search = searchreq)
        a.save()
        #if searchreq:
        #    query_list = searchreq.split()
        #    result = result.filter(
        #        reduce(operator.and_,
        #               (Q(title__icontains=q) for q in query_list)) |
        #        reduce(operator.and_,
        #               (Q(content__icontains=q) for q in query_list))
        #    )
        return redirect('/error/')
    else:
        return render(request, 'search/homev3.html', {})
        
def error(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print (email)
            a = Email(email=email)
            a.save()
            return redirect('/result/pets/')
    else:
        form = PostForm()
        return render(request, 'search/results_error_blur.html', {'form':form})

def result_fitnessmotivation_blur(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print (email)
            a = Email(email=email)
            a.save()
            return redirect('/result/fitness-motivation/')
    else:
        form = PostForm()
        return render(request, 'search/results_fitnessmotivation1_blur.html', {'form':form})

def result_fitnessmotivation(request):
    return render(request, 'search/results_fitnessmotivation1.html', {})
    
def result_pets(request):
    return render(request, 'search/results_pets.html', {})
    
def result_pets_blur(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print (email)
            a = Email(email=email)
            a.save()
            return redirect('/result/pets/')
    else:
        form = PostForm()
        return render(request, 'search/results_pets_blur.html', {'form':form})
        
def result_autotest(request):
    influencers = OrderedList.objects.filter(list__nichename = 'Gene List 1').order_by('order')
    return render(request, 'search/results_autotest.html', {'influencers': influencers})
    
def result_digital_marketing(request):
    influencers = OrderedList.objects.filter(list__nichename = 'digital-marketing').order_by('order')
    return render(request, 'search/results_digital-marketing.html', {'influencers': influencers})
    
def result(request, nichelist):
    print (nichelist)
    influencers = OrderedList.objects.filter(list__nichename = nichelist).order_by('order')
    return render(request, 'search/results_digital-marketing.html', {'influencers': influencers})
    
def result_mental_health(request):
    influencers = OrderedList.objects.filter(list__nichename = 'Mental Health').order_by('order')
    return render(request, 'search/results_mental-health.html', {'influencers': influencers})
    
def result_teaching_inspiration(request):
    influencers = OrderedList.objects.filter(list__nichename = 'Teaching Inspiration').order_by('order')
    return render(request, 'search/results_mental-health.html', {'influencers': influencers})
    
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('/update-profile/')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'search/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })