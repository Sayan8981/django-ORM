from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View, UpdateView, DeleteView, ListView
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import Student, Contact, Student_details
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
contact_template = 'blog_posts/contact.html'
contact_success_template ='blog_posts/contact_success.html'
contact_unsuccess_template = 'blog_posts/contact_unsuccess.html'
student_detail_template = 'blog_posts/student_details.html'

def post_list(request, template_name=student_list_template):
    student_list = Student.objects.all()
    #import pdb;pdb.set_trace()
    page = request.GET.get('page', 1)

<<<<<<< HEAD
    paginator = Paginator(student_list, 6)
=======
    paginator = Paginator(student_list, 10)
>>>>>>> db454fe800e03e71b84b01fe5c26642694a077d0
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, template_name, { 'students': students })
<<<<<<< HEAD
=======

# def pagination(request):
#     student_list = Student.objects.all()

>>>>>>> db454fe800e03e71b84b01fe5c26642694a077d0

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
    
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'    
    
def contact_view(request):
    if request.method == 'POST':
        try:
            form = ContactForm(request.POST)
            form.save()
            return render(request, contact_success_template)
        except Exception as e:
            return render(request, contact_unsuccess_template)    
    form = ContactForm()
    context = {'form': form}
    return render(request, contact_template, context)

def post_student_details(request, template_name=student_detail_template):
    student_data = Student_details.objects.all().order_by('id')
    # data = {}
    # data['object_list'] = student_data
    page = request.GET.get('page', 1)
    paginator = Paginator(student_data, 5)
    try:
        students = paginator.page(page)
        # import pdb;pdb.set_trace()
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, template_name, {'students': students})
    #return render(request, template_name, data)
    