from django.shortcuts import render
from .forms import joinForm,contactForm
from .models import Member,Title,Image,nustartup,Createevents,join,house

def home(request):
     return render(request,"home.html")



def team(request):
	titles = Title.objects.all().order_by('priority')
	dic={}
	for title in titles:
		members=Member.objects.filter(title=title)
		dic.update({members:title})
	return render(request,'team.html',{'dic':dic})


def gallery(request):
	pics = Image.objects.all()
	return render(request,'gallery.html',{'pics':pics})


def startups(request):
	startups=nustartup.objects.all
	return render(request,'tech.html',{'startups':startups})



def First(request):
	first=Createevents.objects.all
	return render(request,'house.html',{'first':first})


def join(request):
	template="join.html"

	if request.method == "POST":
		form = joinForm(request.POST)

		if form.is_valid():
			form.save()

	else:
		form = joinForm()

	context = {
		'form' : form 
	}			

	return render(request, template, context)


def contact(request):
	template="contact.html"

	if request.method == "POST":
		form = contactForm(request.POST)

		if form.is_valid():
			form.save()

	else:
		form = contactForm()

	context = {
		'form' : form 
	}			

	return render(request, template, context)


def ingenuity(request):
	return render(request,"ingenuity.html")



def house(request):
	template="join2.html"

	if request.method == "POST":
		form = houseForm(request.POST)

		if form.is_valid():
			form.save()

	else:
		form = houseForm()

	context = {
		'form' : form 
	}			

	return render(request, template, context)