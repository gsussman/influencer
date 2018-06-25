# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Search

# Create your views here.
def home(request):
    if request.method == 'POST':
        result = request.POST
        searchreq = result['search']
        print (result['search'])
        a = Search(search = searchreq)
        a.save()
        return redirect('/error/')
    else:
        return render(request, 'search/homev3.html', {})
        
def error(request):
    return render(request, 'search/error.html', {})
    
def result_fitnessmotivation(request):
    return render(request, 'search/results_fitnessmotivation1.html', {})