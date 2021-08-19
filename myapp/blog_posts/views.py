from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm


from .models import Student
# Create your views here.


class PostsForm(ModelForm):
    class Meta:
        model = Student
        fields = ['id', 'roll_no', 'name', 'stud_class', 'department']


def post_list(request, template_name='blog_posts/post_list.html'):
    posts = Student.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)


def post_create(request, template_name='blog_posts/post_form.html'):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'form': form})


def post_update(request, pk, template_name='blog_posts/post_form.html'):
    post = get_object_or_404(blog_posts, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'form': form})


def post_delete(request, pk, template_name='blog_posts/post_delete.html'):
    post = get_object_or_404(Student, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('Student:post_list')
    return render(request, template_name, {'object': post})