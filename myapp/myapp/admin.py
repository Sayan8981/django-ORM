from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Book_list, Student, Student_Subject, Student_details

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_filter = ('name', 'stud_class', 'department')
    list_display = ('name', 'roll_no', 'stud_class', 'department')
    
@admin.register(Student_details)
class StudentDetailsAdmin(admin.ModelAdmin):
    list_filter = ('student__department', 'student__stud_class', 'student__roll_no')
    list_display = ('mob_no', 'father_name', 'mother_name', 'address')
    
@admin.register(Student_Subject)    
class StudentSubjectAdmin(admin.ModelAdmin):
    list_filter = ('student__name',)
    list_display = ('subject',)

@admin.register(Book_list)
class BookListAdmin(admin.ModelAdmin):
    list_filter = ('student__name',)
    list_display = ('book_name',)
