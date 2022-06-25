from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView

# Create your views here.

class PostListView(ListView):
    model = Post

def PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

def PostDetailView(DetailView):
    model = Post

def PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")


def PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

