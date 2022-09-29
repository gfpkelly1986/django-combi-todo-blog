"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from todo import views
# get_todo_list, add_item, edit_item, 
# PostList, PostDetail, PostLike, toggle_item
urlpatterns = [
    path('admin/', admin.site.urls),
    # The blank string is for the home page,
    # change when combining projects together.
    path('', views.get_todo_list, name='get_todo_list'),
    path('summernote/', include('django_summernote.urls')),
    path('add/', views.add_item, name='add_item'),
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('toggle/<item_id>', views.toggle_item, name='toggle'),
    path('delete/<item_id>', views.delete_item, name='delete'),
    path('todo/templates/index.html/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('accounts/', include('allauth.urls')),
]
