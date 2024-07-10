from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def all_recipes(request):
    template = loader.get_template('recipes.html')
    return HttpResponse(template.render())
