from django.shortcuts import render, redirect, get_object_or_404
from .models import HaveToilet
from .forms import CreateHaveToiletForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def home(request):
    current_posts = HaveToilet.objects.all()
    context = {
        'current_posts': current_posts,
    }
    return render(request, 'dashboard/home.html', context)


@login_required
def have_toilet(request):
    if request.method == 'POST':
        form = CreateHaveToiletForm(request.POST, request.FILES)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, f'Your toilet post has been created!')
            return redirect('home')
    else:
        form = CreateHaveToiletForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/post_toilet.html', context)
