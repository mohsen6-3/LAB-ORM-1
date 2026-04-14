from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.
def posts_view(request : HttpRequest):

    if request.method == 'POST':
        new_post = Post(title=request.POST['title'], content=request.POST['content'], is_published=request.POST.get('is_published', False), published_at=request.POST.get('published_at', None))
        new_post.save()

    return render(request, 'blog/posts_page.html')