from django.http import HttpResponse
from django.shortcuts import render

from .forms import ToDoForm


def todo(request):
	context = {}
	
	form = ToDoForm(request.POST or None)
	
	if form.is_valid():
		form.save()
	
	context["form"] = form
	return render(request, "todo.html", context)
	
