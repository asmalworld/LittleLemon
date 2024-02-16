from django.shortcuts import render

from .models import Booking
from .models import Menu
from datetime import datetime
import json


# Create your views here.
def index(request):
    return render(request, 'index.html')