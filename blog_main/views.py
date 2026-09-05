from django.shortcuts import render

from blogs.models import Blog, Category

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('update_at')
    post = Blog.objects.filter(is_featured=False, status='Published')
    context = {
        'featured_posts': featured_posts,
        'post':post
    }
    return render(request, 'home.html',context)