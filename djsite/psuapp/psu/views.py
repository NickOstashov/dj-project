from django.shortcuts import render
from django.views.generic import ListView
from psu.models import Problem, FAQ
from rest_framework import viewsets
from psu.serializers import ProblemSerializer, FaqSerializer, ApplicationSerializer, UserSerializer
from django_filters import FilterSet,CharFilter
from users.models import Applications, CustomUser
from rest_framework.decorators import action
from django.http import JsonResponse

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
        exclude = ['icon','extension_field']
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


class ApplicationSetFilter(FilterSet):
    username__icontains = CharFilter(field_name="user_name",lookup_expr="icontains")
    class Meta:
        model = Applications
        fields = "__all__"

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Applications.objects.all()
    serializer_class = ApplicationSerializer
    filterset_class = ApplicationSetFilter

class UserSetFilter(FilterSet):
    username__icontains = CharFilter(field_name="username",lookup_expr="icontains")
    class Meta:
        model = CustomUser
        fields= '__all__'

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    model = CustomUser
    serializer_class = UserSerializer
    filterset_class  = UserSetFilter

    @action(detail=False,methods=['GET'])
    def who_iam(self,request):
        queryset = CustomUser.objects.all()
        queryset =queryset.filter(id=self.request.user.id)
        data = self.serializer_class(queryset,many=True).data
        return JsonResponse(data,safe=False)
        