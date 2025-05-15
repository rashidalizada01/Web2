from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from django.views import View

from post.models import PostModel


# Create your views here.
def post(request):
    return HttpResponse('This is post page')

def detail(request):
    return HttpResponse('This is detail of previous article')

def comments(request):
    if request.method == 'GET':
        return HttpResponse('This is GET method of showing comments')

    if request.method == 'POST':
        return HttpResponse('This is POST method of showing comments')


class Post(View):
    def get(self, request):
        articles = [
            {
                'title': 'Eathquake happened in Turkiye',
                'description': 'People run out',
                'date': datetime.now()
            },
            {
                'title': 'Our diplomats signed contract with china',
                'description': 'Business will develop',
                'date': datetime.now()
            }
        ]
        return render(request, 'articles.html',{
            'posts': articles
        })


class CreatePost(View):
    def get(self, request):
        return render(request, 'create_article.html')
    def post(self, request):
        title = request.POST.get('title', 'unknown')
        description = request.POST.get('description', 'unknown')
        date = datetime.now()
        PostModel.objects.create(
            title = title,
            description = description,
            date = date
        )
        return redirect(reverse('list_articles'))