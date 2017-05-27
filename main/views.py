from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	return render(request, 'main/index.html')


def about(request):
	return render(request, 'main/about.html')