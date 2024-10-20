from rest_framework import serializers
from .models import Team, Project, DefenseBoard, Report, Schedule, Comment
from django.contrib.auth.models import User

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["teamname", "teamleader", "teammembers","credit","supervisor"]
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["type", "title", "description", "objectives", "motivation", "area_of_work", "supervisor_choices", "team", "status"]


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields=[""]

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields=["team","defence_date","defence_time","defence_venue","status"]
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields=["comment","commented_by","commented_on"]


class DefenseBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefenseBoard
        fields=["admin","faculty","date","time"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","role"]
