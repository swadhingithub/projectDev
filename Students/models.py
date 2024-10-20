from django.db import models
import requests
import datetime
from django.utils import timezone
# Create your models here.

from django.db import models

from core.models import User
from core import create_team_id, create_project_id, create_report_id
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings

class StudentProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name= 'student_profile')
    studentname=models.CharField(max_length=50,null=True,blank=True)
    student_id = models.CharField(max_length=50,null=True,unique=True)
    phone = models.CharField(max_length=50,null=True,blank=True)
    department = models.CharField(max_length=50,null=True )
    level = models.CharField(max_length=50,null=True)
    session = models.CharField(max_length=10,null=True)
    section = models.CharField(max_length=10,null=True)
    cgpa = models.FloatField(max_length=50, null=True, blank=True)
    address = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='student_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} {self.student_id} {self.department}"
      
    def get_student_information(self):
      
        url=f"https://ui-avatars.com/api/?name={self.user.username}"
        imageurl=requests.get(url)
      
        return {
            'student_id': self.student_id,
            'username': self.user.username,
            'email': self.user.email,
            'phone': self.phone,
            'department': self.department,
            'level': self.level,
            'session': self.session,
            'cgpa': self.cgpa,
            'address': self.address,
            'image': self.image.url if self.image else imageurl,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


class Team(models.Model):
    teamid = models.CharField(max_length=20, primary_key=True)
    teamname = models.CharField(max_length=100)
    teamleader = models.ForeignKey(User, related_name="team_leader", on_delete=models.CASCADE,null=True, blank=True)
    teammembers = models.ManyToManyField(User, related_name="team_members", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
        
    def __str__(self):
        return f"{self.teamname} ({self.teamid})"
    
    def get_team_information(self):
        return {
            'teamid': self.teamid,
            'teamname': self.teamname,
            'teamleader': self.teamleader.username,
            'teammembers': [member.username for member in self.teammembers.all()],
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            
        }

class TeamRequest(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invited_by')
    invited_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invited_user')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='pending')
    invitation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.invited_user.username} invited to {self.team.teamname}"
    
    def get_request_information(self):
        return {
            'team': self.team.teamname,
            'invited_by': self.invited_by.username,
            'invited_user': self.invited_user.username,
            'status': self.status,
            'invitation_date': self.invitation_date,
        }



class Project(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('research', 'Research-based'),
        ('project', 'Project-based')
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    projectid = models.CharField(max_length=20, primary_key=True)
    type = models.CharField(max_length=10, choices=PROJECT_TYPE_CHOICES)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    objectives = models.TextField(blank=True, null=True)
    motivation = models.TextField(blank=True, null=True)
    area_of_work = models.CharField(max_length=255, null=True, blank=True)
    supervisor_choices = models.ManyToManyField(User, limit_choices_to={'role': 'faculty'}, related_name='supervisor_choices', blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team')
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.projectid:
            self.projectid = create_project_id()
        super(Project, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.title} ({self.projectid})"
      
    def get_project_information(self):
        return {
            'projectid': self.projectid,
            'type': self.type,
            'title': self.title,
            'description': self.description,
            'objectives': self.objectives,
            'motivation': self.motivation,
            'area_of_work': self.area_of_work,
            'supervisor_choices': [supervisor.username for supervisor in self.supervisor_choices.all()],
            'team': self.team.teamname,
            'status': self.status,
        }
        
class Report(models.Model):
    reportid = models.CharField(max_length=20,null=True,blank=True)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    team= models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitted_by', null=True, blank=True)
    report_date = models.DateTimeField(auto_now_add=True)
    
    report = models.FileField(upload_to='project_reports', null=True, blank=True)
    
    status = models.CharField(max_length=20,choices=(('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')), default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Report for {self.project.title}"
    
    def get_report_information(self):
        return {
            'project': self.project.title,
            'report': self.report.url,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
        

class InviteUser(models.Model):
    id=models.UUIDField(primary_key=True,auto_created=True,editable=False)
    sendr=models.ForeignKey(User,related_name='sent_invitations',on_delete=models.CASCADE)
    reciver=models.ForeignKey(User,related_name='received_invitations',on_delete=models.CASCADE)
    team=models.ForeignKey(Team,on_delete=models.CASCADE,null=True,blank=True)
    status=models.CharField(max_length=20,choices=(('pending','Pending'),('accepted','Accepted'),('rejected','Rejected')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notifaction(models.Model):
    
    INVITATION = 'INVITATION'
    NEW_PROJECT = 'NEW_PROJECT'
    NEW_REPORT = 'NEW_REPORT'
    ALART= 'ALART'
    NOTIFICATION_TYPES = [
        (INVITATION, 'Invitation'),
        (NEW_PROJECT, 'New Project'),
        (NEW_REPORT, 'New Report'),
        (ALART, 'Alart'),
    ]
  
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id=models.IntegerField(primary_key=True)
    invite_id=models.UUIDField(null=True,blank=True)
    type=models.CharField(max_length=20,choices=NOTIFICATION_TYPES,null=True,blank=True)
    is_read=models.BooleanField(default=False,null=True,blank=True)
    other_data=models.JSONField(null=True,blank=True)
    other_id=models.CharField(max_length=20,null=True,blank=True)
    def __str__(self):
        return f"Nofifaction for {self.user.username}"
    
    def get_notification_information(self):
        return {
            'user': self.user.username,
            'message': self.message,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
    def find_all_notifications(self):
        return Notifaction.objects.filter(user=self.user)
