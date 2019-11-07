from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    data_to_template = {
        'nav' 		: 'home',
        'title'      : 'Vaping.com'
    }
    return render(request, 'core/body.html', data_to_template)