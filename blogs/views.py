from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404 ,render
from blogs.models import Blog, Category, Comment
from django.db.models import Q


# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status = "Published", category = category_id)
    try:
        category = Category.objects.get(id=category_id)
    except:
        #redirect the user to home
        return redirect('home')
    # category = get_object_or_404(category,id=category_id)
     
    context = {
        "posts":posts,
        "category":category
    }
    return render(request, 'post_by_category.html',context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    # Comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    
    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)

def search(request):
    keywords = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keywords) | Q(short_description__icontains=keywords) | Q(blog_body__icontains=keywords) ,status="Published")
    context={
        'blogs': blogs,
        'keywords' : keywords,
    }
    return render(request, 'search.html', context)
