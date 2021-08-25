from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
import re
from django.views.generic import View, UpdateView
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import Student
# Create your views here.


# class PostsForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'roll_no', 'stud_class', 'department']

def post_list(request, template_name='blog_posts/post_list.html'):
    posts = Student.objects.all()
    #import pdb;pdb.set_trace()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def update_list(request, template_name='blog_posts/student_record_edit.html'):
    posts = Student.objects.all()
    #import pdb;pdb.set_trace()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def post_create(request, template_name='blog_posts/post_form.html'):
    flag = True
    if request.method == 'POST':
        name = request.POST['name']
        roll_no = request.POST['roll_no']
        stud_class = request.POST['stud_class']
        department = request.POST['department']

        record = Student.objects.all()
        for data in record:
            if data.name == name:
                messages.error(request, 'Name already exists!')                 
                flag = False
                break
            elif type(eval(roll_no)) != int:
                messages.error(request, 'Roll no should contains numbers!')                 
                flag = False
                break
            elif type(eval(stud_class)) != int:
                messages.error(request, 'Stud_class should contains numbers!')
                flag = False
                break
            elif re.findall('[0-9]+', department):
                messages.error(request, 'Department should contains name of the department like <Science/Commerce....>!')
                flag = False
                break 
        if not messages or flag == True:
            user = Student(name = name, roll_no = roll_no, stud_class = stud_class, department = department)
            user.save()    
    return render(request, template_name)

class search_id(View):
    
    def post(self, request):
        if request.method == 'POST':
            posts = Student.objects.filter(pk = request.POST.get('search'))
            if posts.exists():
                data = {}
                data['object_list'] = posts
                return render(request, 'blog_posts/post_list.html', data)
            else:
                return render(request, 'blog_posts/post_list.html')
class StudentUpdateView(UpdateView):
    model = Student
    template_name = "blog_posts/student_update_record_form.html"
    fields = ['name', 'roll_no', 'stud_class', 'department']
    slug_field = "id"
    success_url ="/blog_posts/home"
        
# def post_update(request, pk, template_name='student_record_edit.html'):
#     post = get_object_or_404(Student, pk=pk)
#     form = PostsForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('blog_posts:post_list')
#     return render(request, template_name, {'form': form})

# def post_delete(request, pk, template_name='post_delete.html'):
#     post = get_object_or_404(Student, pk=pk)
#     if request.method=='POST':
#         post.delete()
#         return redirect('Student:post_list')
#     return render(request, template_name, {'object': post})