from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NeedPost
from .forms import CreateNeedPostForm
from django.views.generic import ListView, CreateView


def need_toilet(request):
    current_posts = NeedPost.objects.all().order_by('-priority')
    context = {
        'current_posts': current_posts,
    }
    return render(request, 'dashboard/need_toilet.html', context)


def create_post(request):
    if request.method == 'POST':
        form = CreateNeedPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('need-toilet')
    else:
        form = CreateNeedPostForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/create_post.html', context)
