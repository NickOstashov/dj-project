from django.shortcuts import render
from django.views.generic import ListView
from psu.models import Problem


# Create your views here.

class HomePage(ListView):
    model = Problem
    template_name = 'psu/index.html'
    context_object_name = 'list'

# def index(request):
#     problem_list = Problem.objects.all()
#     context = {
#         'problems':problem_list
#     }
#     return render(request,'psu/index.html',context)
