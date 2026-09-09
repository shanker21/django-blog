from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard,name="dashboard"),
    path('categories/', views.categories, name='categories'),
    path('categories/add',views.add_category, name='addcategory'),
    path('categories/edit/<int:pk>/',views.edit_category, name='editcategory'),
    path('categories/delete/<int:pk>/',views.delete_category, name='deletecategory'),
    #blog
    path('posts/',views.posts, name='posts'),
    path('posts/add',views.add_post,name='addpost'),
    path('posts/edit/<int:pk>/',views.edit_post,name='editpost'),
    path('posts/delete/<int:pk>/',views.delete_post, name='deletepost'),
    #users
    path('users/',views.users,name='users'),
    path('user/add',views.add_user,name='adduser'),
    path('user/edit/<int:pk>/',views.edit_user,name='edituser'),
    path('user/delete/<int:pk>/',views.delete_user, name='deleteuser'),
]