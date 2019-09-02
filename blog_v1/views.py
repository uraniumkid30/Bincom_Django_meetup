from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *
from .forms import *
def bloglist(request):
    all_blog_posts = Post.posts.all()
    paginator = Paginator(all_blog_posts,2)
    page = request.GET.get('page')
    blogposts = paginator.get_page((page))
    messages.info(request, 'this is a list of all blog posts')
    #context = {'posts':all_blog_posts}
    context = {'posts': blogposts,}

    return render(request,'blog_v1/bloglist.html',context=context)

def blogdetail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    context = {'post': post}
    return render(request, 'blog_v1/blogdetail.html', context=context)

def blogcreate(request):
    author, created = Author.objects.get_or_create(user=request.user)
    form = PostForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        print(author,created)
        form.instance.author = author
        form.save()
        return redirect('blog_v1:bloglist')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'blog_v1/blogcreate.html', context=context)

def blogupdate(request,slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():

        form.save()
        return redirect('blog_v1:bloglist')
    
    context = {'form': form}
    return render(request, 'blog_v1/blogupdate.html', context=context)