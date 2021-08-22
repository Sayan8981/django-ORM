
from django.conf.urls import url
from blog_posts import views


urlpatterns = [
    url(r'^home$', views.post_list, name='post_list'),
    url(r'^new$', views.post_create, name='post_new'),
    url(r'^search$', views.search_id.as_view(), name='search'),
    ]
