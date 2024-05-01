from django.http import HttpResponse
from django.shortcuts import render

from apps.models import Post, Tag


def post_list_view(request):
    posts = Post.objects.all()
    contex = {
        'posts': posts,
        'tags': Tag.objects.all(),
        'latest_post': Post.objects.order_by('-created_at')[:3],
    }
    return render(request, 'apps/list.html', contex)


def post_detail_view(request, pk):
    post = Post.objects.get(uuid=pk)
    contex = {
        'post': post,
        'tags': Tag.objects.all(),
        'latest_post': Post.objects.order_by('-created_at')[:3],
    }
    return render(request, 'apps/detail.html', contex)