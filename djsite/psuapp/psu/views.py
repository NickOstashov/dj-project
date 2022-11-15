from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from psu.models import Problem, FAQ
# from contact.models import Contact


# Create your views here.

class HomePage(ListView):
    model = Problem
    template_name = 'psu/index.html'
    context_object_name = 'list'

    # def get_seach(request):
    #     search_query = request.GET.get('search','')
    
    
    def get_context_data(self,*args,**kwargs):
        from contact.models import Contact
        context = super().get_context_data(*args,**kwargs)
        context['contact'] = Contact.objects.all()

        return context

# class FaqPage(DetailView):
#     model = FAQ
#     template_name = 'psu/detail.html'
#     context_object_name = 'list'

#     def get_queryset(self):
#         return FAQ.objects.filter(section=self.kwargs['pk'])


def pr_faq(request,pk):
    model = FAQ.objects.filter(section_id = pk)
    