from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponse
from django.core.mail import send_mail

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

@login_required  
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#@login_required(login_url='/admin/') 
@login_required 
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

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull =True).order_by('create_date')
    return render(request,'blog/post_drafts.html',{'posts':posts})

@login_required     
def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:blog.views.post_detail', pk=pk)

@login_required         
def post_remove(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:blog.views.post_list')
    
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:blog.views.post_detail', pk=comment.post.pk) 

@login_required
def comment_remove(request,pk):
     comment = get_object_or_404(Comment, pk=pk)
     post_pk = comment.post.pk
     comment.delete()
     return redirect('blog:blog.views.post_detail', pk=post_pk)

def contact_us(request):
    if request.method == "POST":
       form = ContactForm(request.POST)
       if form.is_valid():   
             subject = form.cleaned_data['subject']
             message = form.cleaned_data['message']
             sender = form.cleaned_data['sender']
             cc_myself = form.cleaned_data['cc_myself']

             recipients = ['info@example.com']
             if cc_myself:
                 recipients.append(sender)

             #send_mail(subject, message, sender, recipients)
             #return redirect('/thanks/')
             return HttpResponse("Hi {} Thank You for Contacting Us ".format(sender))
    else:
        form = ContactForm()
    return render(request, 'blog/blog_contact.html', {'form': form})