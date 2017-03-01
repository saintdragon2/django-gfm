from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'blogengine/post_list.html',
        {
            'title': 'gfm test',
            'posts': posts,
        }
    )
