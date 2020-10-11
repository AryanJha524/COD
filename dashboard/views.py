from django.shortcuts import render, redirect, get_object_or_404
from .models import NeedPost, Comment
from .forms import CreateNeedPostForm, CreateCommentForm
from django.contrib.auth.decorators import login_required


@login_required
def need_toilet(request):
    current_posts = NeedPost.objects.all().order_by('-priority')
    context = {
        'current_posts': current_posts,
    }
    return render(request, 'dashboard/need_toilet.html', context)


@login_required
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


@login_required
def detailed_view(request, pk):
    current_post = get_object_or_404(NeedPost, id=pk)
    comments = Comment.objects.filter(post=current_post)
    if request.method == 'POST':
        comment_form = CreateCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.panel = current_post
            comment.save()
            return redirect('detailed-view', pk=current_post.id)
    else:
        comment_form = CreateCommentForm()
    context = {
        'current_post': current_post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'dashboard/detailed_view.html', context)
