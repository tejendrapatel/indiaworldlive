"""Bloggers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blog.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('contact/', Contact, name = 'contact'),
    path('login/', Login, name = 'login'),
    path('signup/', Signup, name = 'signup'),
    path('logout/', Logout, name = 'logout'),
    path('fashion/', blog_pannel, name='fashion'),
    path('addblog/', Add_blog, name="addblog"),
    path('edit_detail/', Edit_detail, name="edit"),
    path('change_password/', Change_password, name="change"),
    path('video/',Video,name='video'),
    path('astro/',Astro,name='astro'),
    path('index/',inidex2,name='index'),
    path('like/<int:pid>/', Blog_Like, name='like'),
    path('blogdetail/<int:pid>/', Blog_detail, name='blogdetail'),
    path('blogcomment/<int:pid>/', Blog_Comment, name='blogcomment'),
    path('deleteblog/<int:pid>/', delete_blog, name='deleteblog'),
    path('categorypost/<int:cid>/', Category_post, name='categorypost'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
