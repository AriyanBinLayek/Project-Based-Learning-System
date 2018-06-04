from django import forms
from django.contrib.auth.models import User
from student.models import Student
from teacher.models import Teacher

class NewTopicForm(forms.ModelForm):


	class Meta:
		model = Student
		field = ['user.first_name','user.last_name','user.email','contact_no','user.username','user.password']
		