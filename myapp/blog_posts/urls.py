
from django.conf.urls import url
from django.contrib import admin
from blog_posts import views


urlpatterns = [
    url(r'^home$', views.post_list, name='post_list'),
    url(r'^new$', views.post_create, name='post_new'),
    # url(r'^post_edit/(\d+)$', views.post_update, name='post_edit'),
    # url(r'^post_delete/(\d+)$', views.post_delete, name='post_delete'),
]
