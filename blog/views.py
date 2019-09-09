from django.shortcuts import render, get_object_or_404
from django.utils import timezone
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
