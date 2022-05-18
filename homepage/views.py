from django.shortcuts import render
from datetime import datetime
from .models import Course
# Create your views here.


def home(request):
    course_list = Course.objects.all()
    return render(request, 'home.html', {
        'course_list': course_list,
    })

def detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'detail.html', {
        'course': course
    })

def search(request):
    return render(request, 'search.html', {
        'current_time': str(datetime.now()),
    })
