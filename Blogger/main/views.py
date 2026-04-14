from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blog.models import Post
# Create your views here.
def home_view(request : HttpRequest):
    posts = Post.objects.all()
    return render(request, 'main/home_page.html', {'posts': posts})