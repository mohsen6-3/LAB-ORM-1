from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def posts_view(request : HttpRequest):
    return render(request, 'blog/posts_page.html')