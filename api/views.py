from django.shortcuts import render
from api.models import Women
from django.views.generic import  ListView, TemplateView, CreateView, DetailView
from rest_framework import  generics
from api.serializer import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
