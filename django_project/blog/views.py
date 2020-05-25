from django.shortcuts import render
from django.http import HttpResponse

#list of dictionaries
posts = [
    {
        'author': 'Roberta',
        'title': 'First Post',
        'content': 'Content for my first post',
        'date_posted': 'November 10, 2016'
    },
        {
        'author': 'Lima',
        'title': 'About Monday',
        'content': 'Content for my post regarding mondays',
        'date_posted': 'May 25s, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)
    

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
