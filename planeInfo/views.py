from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Plane,Passenger

# Create your views here.
def home(request):
	planelist= Plane.objects.all()
	context = {'planelist': planelist}
	return render(request,'planeInfo/base.html',context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)