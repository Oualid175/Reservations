from django.template.loader import get_template
from django.shortcuts import render
from .forms import YourForm, DateForm
import calendar
from datetime import datetime

def index(request):
    return render(request,'index.html')