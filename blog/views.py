from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from.forms import PostForm
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    frontend_text = {'posts': posts}
    return render(request, 'blog/post_list.html', frontend_text)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    frontend_text = {'post':post}
    return render(request, 'blog/post_detail.html', frontend_text)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        frontend_text = {'form': form}
    return render(request, 'blog/post_edit.html', frontend_text)
