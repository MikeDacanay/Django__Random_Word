from django.shortcuts import render, HttpResponse, redirect,render
from django.utils.crypto import get_random_string 
# the index function is called when root is visited



def index(request):
	return render(request,'firstapp/index.html')

def generate(request):
	if 'counter' not in request.session:
		request.session['counter']=0
	request.session['counter']+=1
	request.session['rand_str']=get_random_string(length=14)
	return redirect("/")

def reset(request):
	if 'counter' in request.session:
		del request.session['counter']
	if 'rand_str' in request.session:
		del request.session['rand_str']
	# if 'counter' in request.session:
	# 	del request.session['counter']
	return redirect('/')