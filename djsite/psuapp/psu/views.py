from django.shortcuts import render
from django.views.generic import ListView
from psu.models import Problem, FAQ
# from contact.models import Contact


# Create your views here.

class HomePage(ListView):
    model = Problem
    template_name = 'psu/index.html'
    context_object_name = 'list'
    
    def get_context_data(self,*args,**kwargs):
        from contact.models import Contact
        context = super().get_context_data(*args,**kwargs)
        context['contact'] = Contact.objects.all()

        return context


class Search(ListView):
    template_name = 'psu/index.html'
    context_object_name = "list"

    def get_queryset(self):
        return Problem.objects.filter(naming__icontains = self.request.GET.get('srh'))

    def get_context_data(self,*args,**kwargs):
        from contact.models import Contact
        context = super().get_context_data(*args,**kwargs)
        context['srh'] = self.request.GET.get('srh')
        context['contact'] = Contact.objects.all()
        return context
    
class FaqPage(ListView):
    model = FAQ
    template_name = 'psu/problem_detail.html'
    context_object_name = 'contant'
    def get_queryset(self):
        return FAQ.objects.filter(problem_id=self.kwargs['pr_id'])

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['title'] = FAQ.objects.filter(problem_id=self.kwargs['pr_id'])[0].problem
        return context


    