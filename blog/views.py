from django.shortcuts import render
from django.views import generic

# Create your views here.
from blog.models import *

class BlogIndex(generic.ListView):
    queryset = Post.objects.all()
    template_name = "home.html"
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = Post
    template_name = "post.html"
