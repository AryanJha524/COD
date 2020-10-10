from django.shortcuts import render
from django.http import HttpResponse
from .models import NeedPost
from .forms import CreateNeedPostForm
from django.views.generic import ListView, CreateView

# Create your views here.


def index(request):
    return HttpResponse("Hello, world")


class ItemListCreateView(CreateView, ListView):
    model = NeedPost
    template_name = 'dashboard/home.html'
    context_object_name = 'need_toilet_items'
    fields = ['name', 'priority']
    paginate_by = 10

    def get_success_url(self):  # returns to homepage after creating a new post
        return reverse('dashboard-home', kwargs={})

    def get_queryset(self):
        return NeedPost.objects.filter().order_by(
            '-priority', 'date_posted')
