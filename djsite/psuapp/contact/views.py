from django.shortcuts import render
from django.views.generic import ListView
from contact.models import Contact

# Create your views here.
class ContactHomePage(ListView):
    model = Contact
    template_name = 'psu/index.html'
    context_object_name = 'contact'

def get_contact(request):
    pass