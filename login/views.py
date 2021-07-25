from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author' : 'Hamza', 
		'title' : 'Random Title',
		'content' : 'Amazing Content',
		'date_posted' : '18th September 2020'
	},
	{
		'author' : 'Graham Wells', 
		'title' : 'Amazing Title',
		'content' : 'Philosophical content',
		'date_posted' : '17th March 2003'
	}
]

def home(request):
	return render(request, 'login/test.html')

def about(request):
	context = {
		'posts' : posts
	}
	return render(request, 'login/about.html', context)

def artists(request):
	return render(request, 'login/artists.html', {'title' : 'Artists'})