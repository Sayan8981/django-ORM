from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
import re
from django.views.generic import View, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import Student
# Create your views here.


# class PostsForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'roll_no', 'stud_class', 'department']
student_update_record_template = "blog_posts/student_update_record_form.html" 
student_list_template = 'blog_posts/post_list.html'
student_record_edit_template = 'blog_posts/student_record_edit.html'
student_record_create_template = 'blog_posts/post_form.html'
student_record_delete_template = "blog_posts/student_record_delete.html"
reverse_success_url = "/blog_posts/home"

def post_list(request, template_name=student_list_template):
    posts = Student.objects.all()
    #import pdb;pdb.set_trace()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def update_list(request, template_name=student_record_edit_template):
    posts = Student.objects.all()
    #import pdb;pdb.set_trace()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def post_create(request, template_name=student_record_create_template):
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
        try:    
            if not messages or flag == True:
                user = Student(name = name, roll_no = roll_no, stud_class = stud_class, department = department)
                user.save()
        except Exception as error:
            messages.error(request, str(error))            
    return render(request, template_name)
class search_id(View):
    
    def post(self, request):
        if request.method == 'POST':
            posts = Student.objects.filter(pk = request.POST.get('search'))
            if posts.exists():
                data = {}
                data['object_list'] = posts
                return render(request, student_record_edit_template, data)
            else:
                return render(request, student_list_template)           
class StudentUpdateView(UpdateView):
    model = Student
    template_name = student_update_record_template
    fields = ['name', 'roll_no', 'stud_class', 'department']
    slug_field = "id"
    success_url = reverse_success_url
    
class StudentDeleteView(DeleteView):
    # specify the model you want to use
    model = Student
    template_name = student_record_delete_template
    success_url = reverse_success_url