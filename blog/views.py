from django.shortcuts import render, get_object_or_404, redirect
from .models import post
from django.utils import timezone
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post_detl = get_object_or_404(post, pk=pk)
    return render(request,'blog/post_detail.html',{'post_detl':post_detl})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:    
        form = PostForm()
    return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request, pk):
    post_detl = get_object_or_404(post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post_detl)
        if form.is_valid():
            post_detl = form.save(commit=False)
            post_detl.author = request.user
            post_detl.published_date = timezone.now()
            post_detl.save()
            return redirect('post_detail', pk=post_detl.pk)
    else:
        form = PostForm(instance=post_detl)
    return render(request, 'blog/post_edit.html', {'form': form})