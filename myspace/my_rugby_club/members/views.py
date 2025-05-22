from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):#function view
    mymembers = Member.objects.all().values()#Query the Database and assign records to the created object 'mymembers' 
    template = loader.get_template('all_members.html')#loads the template named all_members.html and assigns to object template
    context = {#create dictionary context that stores data you want to pass into the template.
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))#ombines the dictionary and the template and returns them as an HttpResponse

def details(request, id):
    mymember = Member.objects.get(id=id)
    template  = loader.get_template('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())