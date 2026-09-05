from django.shortcuts import redirect, get_object_or_404 ,render
from blogs.models import Blog, Category


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