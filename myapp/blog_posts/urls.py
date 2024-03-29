
from django.urls import re_path as url
from blog_posts import views


urlpatterns = [
    url(r'^home$', views.post_list, name='post_list'),
    url(r'^update$', views.update_list, name='post_list'),
    url(r'^new$', views.post_create, name='post_new'),
    url(r'^search$', views.search_id.as_view(), name='search'),
    url(r'^update_record/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='update_record'),
    url(r'^delete_record/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='delete_record'),
    url(r'^contact/', views.contact_view, name='contact'),
    url(r'^student_details/', views.post_student_details, name='student_details'),
]