from .models import Team, Project, Report,TeamRequest,StudentProfile,InviteUser,Notifaction

from rest_framework import serializers

class StudentProfileSerializer(serializers.ModelSerializer):
    iamge_url=serializers.SerializerMethodField()
    class Meta:
        model = StudentProfile
        fields = ["student_id",
                  "studentname",
                  "phone",
                  "department",
                  "level", 
                  "session",
                  "section", 
                  "cgpa", 
                  "address", 
                  "image", 
                  "created_at",
                  "updated_at",
                  "iamge_url"]
    def get_iamge_url(self,obj):
           
           if obj.image :
               return obj.image.url
           else :
            return f"https://ui-avatars.com/api/?name={obj.user.username}"





class TeamSerializer(serializers.ModelSerializer):
    teamid=serializers.ReadOnlyField()
    
   
    class Meta:
        model=Team
        fields=("teamid","teamname",
                "teamleader","teammembers",
                "created_at",
                "updated_at")
        read_only_fields = ['created_at', 'updated_at']
    



class TeamRequestSerializer(serializers.ModelSerializer):
    
    invited_by=serializers.ReadOnlyField(source='invited_by.username')
    invited_user=serializers.CharField()
  
    teamid=serializers.ReadOnlyField(source='team.teamid')
    teamname=serializers.ReadOnlyField(source='team.teamname')
    class Meta:
        
        model = TeamRequest
        fields = ['teamid', 'teamname', 
                  'invited_by', 'invited_user', 
                  'status']
        
        read_only_fields = ['invited_by', 
                            'invited_at', 
                            'status',]
    
        

        

class ProjectSerializer(serializers.ModelSerializer):
    
    title=serializers.CharField( required=True)
    description=serializers.CharField( required=True)
    objectives=serializers.CharField( required=True)
    motivation=serializers.CharField( required=True)
    area_of_work=serializers.CharField( required=True)

    class Meta:
        model = Project
        fields = ["projectid",
                  "type",
                  "title",
                  "description",
                  "objectives",
                  "motivation",
                  "area_of_work",
                  "supervisor_choices",
                  "team",
                  "status",
                  "created_at",
                  "updated_at"]
        read_only_fields = ['created_at', 'updated_at', 'status', 'projectid','team']
        
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ["reportid",
                  "project","report",
                  "status","created_at",
                  "updated_at",
                  "report_date"]
        
        read_only_fields = ['created_at', 'updated_at','report_date','reportid','status','project']
        

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifaction
        fields = ("id",'invite_id',
                  'type','is_read',"user",
                  "message","created_at",
                  "updated_at","other_data",
                  "other_id")
        read_only_fields = ['created_at', 'updated_at']