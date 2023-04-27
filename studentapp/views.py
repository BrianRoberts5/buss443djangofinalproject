from django.shortcuts import render
from django.http import HttpResponse
from studentapp.models import studentdatafixed, Course
from django.db import connection
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    context = {'name': 'Brian Roberts'}
    return render(request, 'studentapp/home.html', context)
    #return HttpResponse('<h1>This is the student information app</h1>')
@login_required
def getstudentdatafixed(request):
    sdata = studentdatafixed.objects.all()
    paginator = Paginator(sdata, 10)
    page = request.GET.get('page')
    pagedata = paginator.get_page(page)
  #  print(pagedata[0].__dict__)
    context = {'data':pagedata}
    return render(request, 'studentapp/studentdata.html', context)
@login_required    
def dashboard(request):
    return render(request, 'studentapp/dashboard.html')
@login_required    
def course_details(request):
    courses_list = Course.objects.all()
    paginator = Paginator(courses_list, 10)
    page = request.GET.get('page')
    courses = paginator.get_page(page)
    context = {'courses': courses}
    return render(request, 'students/course_details.html', context)