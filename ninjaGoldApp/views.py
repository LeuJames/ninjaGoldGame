from django.shortcuts import render, HttpResponse, redirect
from time import strftime
import random

def index(request):
    return render(request, 'index.html')

def processMoney(request):
    if 'count' in request.session:
        if request.POST['location'] == 'farm':
            score = random.randint(10,20)
        elif request.POST['location'] == 'cave':
            score = random.randint(5,10)
        elif request.POST['location'] == 'house':
            score = random.randint(2,5)
        elif request.POST['location'] == 'casino':
            score = random.randint(-50,50)
        request.session['count'] += score
        if score > 0:
            request.session['activities'].append({'class': 'green', 'log': f"You earned {score} golds from the {request.POST['location']}! {strftime('%Y/%m/%d %I:%M:%S %p')}"})
        else:
            request.session['activities'].append({'class': 'red', 'log': f"You lost {-1*score} golds at the {request.POST['location']}... Ouch!!! {strftime('%Y/%m/%d %I:%M:%S %p')}"})
    else:
        request.session['count'] = 0
        request.session['activities'] = []
    return redirect('/')

def reset(request):
    request.session['count'] = 0
    request.session['activities'] = []
    return redirect('/')