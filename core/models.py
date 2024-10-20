# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from . import create_defence_id,create_report_id,create_project_id,create_team_id


# class User(AbstractUser):
#   Role_Choices = [
#     ("superadmin", "Super Admin"),
#     ("admin", "Admin"),
#     ('faculty', 'Faculty'),
#     ('student', 'Student'),
#   ]
  
#   role = models.CharField(max_length=20, choices=Role_Choices)
#   universitymail = models.EmailField(max_length=254, unique=True)
  


# class PermitedUser(models.Model):
#   class DefenseBoard(models.Model):
#     admin = models.ForeignKey(
#         'core.User',
#         related_name='admin_defenseboards',  # Unique related_name for admin
#         on_delete=models.CASCADE
#     )
#     faculty = models.ForeignKey(
#         'core.User',
#         related_name='faculty_defenseboards',  # Unique related_name for faculty
#         on_delete=models.CASCADE
#     )
    
# class Team(models.Model):
#     teamid=models.CharField(max_length=20,primary_key=True)
#     teamname=models.CharField(max_length=100)
#     teamleader=models.ForeignKey(User,related_name="team_leader",on_delete=models.CASCADE)
#     teammembers=models.ManyToManyField(User,related_name="team_members")
#     credit=models.IntegerField()
#     supervisor=models.ForeignKey(User,related_name="supervisor",on_delete=models.CASCADE)
    
#     def save_teamid(self,*args,**kwargs):
#         self.teamid=create_team_id()
#         super(Team,self).save(*args,**kwargs)
        
#     def __str__(self):
#         return self.teamname,self.teamid
      

# class Project(models.Model):
#     PROJECT_TYPE_CHOICES = [
#         ('research', 'Research-based'),
#         ('project', 'Project-based')
#     ]
#     projectid=models.CharField(max_length=20,primary_key=True)
#     type = models.CharField(max_length=10, choices=PROJECT_TYPE_CHOICES)
#     title = models.CharField(max_length=255, null=True, blank=True)
#     description = models.TextField()
#     objectives = models.TextField()
#     motivation = models.TextField()
#     area_of_work = models.CharField(max_length=255)
#     supervisor_choices = models.ManyToManyField(User, limit_choices_to={'role': 'faculty'})
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     status = models.CharField(max_length=20, default='pending')
    
#     def save_projectid(self,*args,**kwargs):
#         self.projectid=create_project_id()
#         super(Project,self).save(*args,**kwargs)
        
#     def __str__(self):
#         return self.title,self.projectid

    

# class DefenseBoard(models.Model):
#     boardid=models.CharField(max_length=20,primary_key=True)
#     admin = models.ForeignKey(User, limit_choices_to={'role': 'admin'}, on_delete=models.CASCADE)
#     faculty = models.ManyToManyField(User, limit_choices_to={'role': 'faculty'})
#     date = models.DateField()
#     time = models.TimeField()
    
#     def save_boardid(self,*args,**kwargs):
#         self.boardid=create_defence_id()
#         super(DefenseBoard,self).save(*args,**kwargs)
    
#     def __str__(self):
#         return self.boardid

    


# class Report(models.Model):
#     reportid=models.CharField(max_length=20,primary_key=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     submitted_to = models.ForeignKey(User, related_name='reports_received', on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, default='pending')
    
#     def save_reportid(self,*args,**kwargs):
#         self.reportid=create_report_id()
#         super(Report,self).save(*args,**kwargs)
    


# class Schedule(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     defense_date = models.DateTimeField()
#     defence_venue = models.CharField(max_length=255)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
#     def __str__(self):
      
#         return self.team.teamname,self.project.title,self.defense_date,self.defence_venue
      

# class Comment(models.Model):
#     content = models.TextField()
#     commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     commented_on = models.ForeignKey(Report, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.content,self.commented_by.username
      
      
# class Notification(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, default='unread')
    
#     def __str__(self):
#         return self.title,self.user.username

from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
  
    def create_user(self,username,email, password=None, **extra_fields):
        """Create and return a regular User with an email and password."""
        try:
            if not email:
                raise ValueError(_('The Email field must be set'))
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        except Exception as e:
            raise ValueError(f"Error creating user: {str(e)}")    
    def create_superuser(self, username, email, password=None, **extra_fields):
        """Create and return a superuser with admin privileges."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    
   role=models.CharField(max_length=20,null=True,blank=True)


   base_user=UserManager()
  
   def __str__(self):
      return f'{self.username}-({self.role})'
  
  
  



  
 