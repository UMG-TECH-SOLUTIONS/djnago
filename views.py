from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
	# DONT REPEAT YOURSELF = DRY

def hello(request):
    title = "Hello World!"
    return render(request, "base.html", {"title":title})

def name(request):
    return render(request, "name.html", {"title":"Mahi"})

def middle_name(request):
    return render(request, "middle_name.html", {"title":"Aminu"})

def surname(request):
    context      =  {"title":"Aliyu"}
    something    =  "surname.html"
    template_obj =  get_template(something)
    return HttpResponse(template_obj.render(context))
