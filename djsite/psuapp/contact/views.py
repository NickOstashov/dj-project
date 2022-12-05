from django.shortcuts import render
from contact.models import Contact
from rest_framework import serializers, viewsets

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
# Create your views here.