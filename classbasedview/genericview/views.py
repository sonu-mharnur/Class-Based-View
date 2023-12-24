from django.shortcuts import render
from django.views.generic import CreateView
from .models import Empoyee
# Create your views here.

class CreateUser(CreateView):
    model = Empoyee
    template_name = 'genericview/Employee.html'
    fields = ['eno','ename','esal']

    def get(self,request):

# print(dir(CreateView()))