
from django.shortcuts import render
from django.contrib.auth.models import User
#from .forms import NewTopicForm
from student.models import Student
from teacher.models import Teacher


def home(request):
	return render(request,'index.html')
