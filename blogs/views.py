from django.shortcuts import redirect, get_object_or_404 ,render
from blogs.models import Blog, Category
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
    try:
        single_blog = Blog.objects.filter(slug=slug, status = "Published")
        print(single_blog)
    except:
        return redirect('home')
    context = {
        "single_blog": single_blog,
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