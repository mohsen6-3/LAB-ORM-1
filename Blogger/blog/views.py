from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.
def posts_view(request : HttpRequest):

    if request.method == 'POST':
        new_post = Post(title=request.POST['title'],
            content=request.POST['content'],
            is_published=request.POST.get('is_published', False),
            published_at=request.POST.get('published_at', None))
        if "image" in request.FILES:
            new_post.image = request.FILES["image"]
        new_post.save()
    

        return redirect('main:home_view')

    return render(request, 'blog/posts_page.html')

def post_detail_view(request : HttpRequest, post_id : int):

    post = Post.objects.get(pk=post_id)
    print(post.title)
    return render(request, 'blog/post_detail.html',{'post': post})

def post_update_view(request : HttpRequest, post_id : int):

    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        if "image" in request.FILES:
            post.image = request.FILES["image"]
        post.save()
       

        return redirect('blog:post_detail_view', post_id=post.id)

    return render(request, 'blog/post_update.html', {'post': post})

def post_delete_view(request : HttpRequest, post_id : int):

    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('main:home_view')