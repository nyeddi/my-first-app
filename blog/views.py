from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def post_list(request):
     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
     return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    '''try:
        post = Post.objects.filter(published_date__lte=timezone.now()).filter(pk=pk)
    except:
        raise Http404("Post does not published")'''  
    return render(request, 'blog/post_detail.html', {'post': post})
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required(login_url='/admin/')
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull =True).order_by('create_date')
    return render(request,'blog/post_drafts.html',{'posts':posts})
    
def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:blog.views.post_detail', pk=pk)
    
def post_remove(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:blog.views.post_list')
    