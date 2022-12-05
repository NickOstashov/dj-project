from django.shortcuts import render
from django.views.generic import ListView
from psu.models import Problem, FAQ
from rest_framework import viewsets
from psu.serializers import ProblemSerializer, FaqSerializer
from django_filters import FilterSet,CharFilter

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


class CategorySearch(FaqPage,ListView):
    def get_queryset(self):
        return FAQ.objects.filter(question__icontains = self.request.GET.get('srh'))




# django_rest_framework


class ProblemSetFilter(FilterSet):
    naming__icontains = CharFilter(field_name="naming",lookup_expr="icontains")
    class Meta:
        model = Problem
        exclude = ['icon']
        fields = "__all__"

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    filterset_class = ProblemSetFilter


class FaqSetFilter(FilterSet):
    question__icontains = CharFilter(field_name="question",lookup_expr="icontains")
    class Meta:
        model = FAQ
        fields = "__all__"

class FaqViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FaqSerializer
    filterset_class = FaqSetFilter