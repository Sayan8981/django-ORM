from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class Student(models.Model):
    roll_no = models.PositiveIntegerField(blank=False, unique=True)
    name = models.CharField(blank = False, max_length = 40, unique=True)
    stud_class = models.PositiveIntegerField()
    department = models.CharField(blank = False, max_length=40)
    
    class Meta:
        managed = True
        ordering = ['id', 'name', 'roll_no', 'stud_class', 'department']
            
    def __str__(self):
        return self.name
    
    # def get_post_url(self):
    #     return reverse('post_edit', kwargs={'pk': self.pk})
    
class Student_details(models.Model):
    mob_no = PhoneNumberField(blank=False, help_text='Contact phone number', unique=True)
    address = models.CharField(max_length = 40)
    father_name = models.CharField(blank = False, max_length = 20, unique=True)
    mother_name = models.CharField(max_length = 20, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name = 'student_details')  
    
    class meta:
        managed = True
        ordering = ['student', 'mob_no', 'father_name', 'mother_name', 'address']
        #unique_together = ( 'mob_no', 'father_name', 'mother_name', 'address')
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_mob_no_range",
                check=models.Q(mob_no__range=(0, 10)),
            ),
        ]
        
    def __str__(self):
        return f"{self.father_name}, {self.mob_no} , {self.mother_name}, {self.address}"
    
class Student_Subject(models.Model):
    subject = models.CharField(blank = False, max_length = 20)
    student = models.OneToOneField(Student, on_delete=models.CASCADE,related_name = 'student_subject')
    
    class Meta:
        managed = True
        ordering = ['student', 'subject',]
    
    def __str__(self):
        return self.subject
   
class Book_list(models.Model):
    book_name = models.CharField(blank = True, max_length = 30)
    student = models.ManyToManyField(Student, related_name = 'book_list')
    class Meta:
        managed = True
        ordering = ['book_name']
    
    def __str__(self):
        return self.book_name  
    
class Contact(models.Model):
    email = models.EmailField(blank = True, unique=True)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank = True)
    
    class Meta:
        managed = True
        ordering = ['email']

    def __str__(self):
        return self.email      
    
    
        
