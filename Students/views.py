from django.shortcuts import render
from django.contrib.auth.models import User
from core import create_team_id,create_project_id,create_report_id
from rest_framework import viewsets, generics, permissions
from .models import Team, Project, Report, TeamRequest,Notifaction
from .studentserilizer import TeamSerializer, TeamRequestSerializer,NotificationSerializer,ProjectSerializer,ReportSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.authentication import JWTAuthentication




class CreateTeamview(generics.CreateAPIView):
   
   serializer_class = TeamSerializer
   authentication_classes = [JWTAuthentication]
   permission_classes = [permissions.IsAuthenticated]
   def perform_create(self, serializer):
       teamid=create_team_id()
       team=serializer.save(teamleader =self.request.user,teamid=teamid)
       team.teammembers.add(self.request.user)
       return Response({'message': 'Team created successfully',
                        'teamid': team.teamid,
                        'teamname': team.teamname,
                        'teamleader': team.teamleader.username,
                        'teammembers': team.teammembers.all(),
                        }, status=201)
   
   
        

class InviteTeamview(viewsets.ModelViewSet):
    serializer_class = TeamRequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self,request,*args,**kwargs):
        teamid=request.user.teamid
        team=Team.objects.get(teamid=teamid)
        invited_user=request.data.get('invited_user')
        try :
            if "@" in invited_user:
                invited_user=User.objects.get(email=invited_user)
            else:
                invited_user=User.objects.get(username=invited_user)
                
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=404)
        
      
        if Team.objects.filter(teammembers=invited_user).exists():
            return Response({'error': 'User is already in a team.'}, status=400)
        
        if TeamRequest.objects.filter(team=team,invited_user=invited_user).exists():
            return Response({'error': 'You have already sent an invitation to this user.'}, status=400)
        
        if team.teamleader == invited_user:
            return Response({'error': 'Team leader cannot invite themselves.'}, status=400)
        
        team_request=TeamRequest.objects.create(team=team,invited_by=request.user,invited_user=invited_user)
        
        notifacationmessage=f"{request.user.username} invited you to join {team.teamname}"
        notifaction=Notifaction.objects.create(user=invited_user,
                                               message=notifacationmessage,
                                               invite_id=team_request.id,
                                               other_data={'teamname':team.teamname,
                                                           'teamleader':team.teamleader.username},
                                               type=Notifaction.INVITATION)
        notifaction.save()
        
        
        
        return Response({'message': 'Invitation sent.',
                         'teamid': team.teamid,
                         'invite_id':team_request.id,
                         'teamname': team.teamname,
                         'invited_by': team_request.invited_by.username,
                         'invited_user': team_request.invited_user.username,
                         'status': team_request.status,
                         'invitation_date': team_request.invitation_date,
                         }, status=201)
        

class TeamRequestView(generics.ListAPIView):
    queryset = TeamRequest.objects.all()
    serializer_class = TeamRequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return TeamRequest.objects.filter(invited_user=self.request.user, status='pending')
    
        


        
    
    # def get_queryset(self):
    #     return TeamRequest.objects.filter(invited_user=self.request.user)
    

class AcceptTeamInvitationView(generics.UpdateAPIView):
    queryset = TeamRequest.objects.all() 
    
    serializer_class = TeamRequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def patch(self,request,*args,**kwargs):
        
        try :
            team_request=self.get_object()
            if team_request.invited_user != request.user:
                return Response({'error': 'You are not the invitee for this invitation.'}, status=403)
            
            action=request.data.get('action')
            
            if action not in ['accept', 'declined']:
                return Response({'error': 'Invalid action. Use "accept" or "reject".'}, status=400)
            
            if action == 'accept':
                team_request.status = 'accepted'
                team_request.team.teammembers.add(team_request.invited_user)
                team_request.save()
                return Response({'message': 'Team invitation accepted.',
                                'status': team_request.status}, status=200)
                
            elif action == 'declined':
                team_request.status = 'declined'
                team_request.save()
                return Response({'message': 'Team invitation declined.',
                                'status': team_request.status}, status=200)
                
            else:
                return Response({'error': 'Invalid action.'}, status=400)
        
        except TeamRequest.DoesNotExist:
            return Response({'error': 'Team invitation not found.'}, status=404)
        
class NotificationView(generics.ListAPIView):
    queryset = Notifaction.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return Notifaction.objects.filter(user=self.request.user)
    
    def patch(self,request,*args,**kwargs):
        try:
            notification=self.get_object()
            if notification.user != request.user:
                return Response({'error': 'You are not the owner of this notification.'}, status=403)
            
            notification.is_read = True
            notification.save()
            return Response({'message': 'Notification marked as read.',
                             'is_read': notification.is_read}, status=200)
        
        except Notifaction.DoesNotExist:
            return Response({'error': 'Notification not found.'}, status=404)
    
    

class UserTeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return Team.objects.filter(teammembers=self.request.user)
    
    def get(self,request,*args,**kwargs):
        queryset=self.get_queryset()
        serializer=TeamSerializer(queryset,many=True)
        return Response(serializer.data)
    
class ProjectView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        try:
            teams = Team.objects.filter(teamleader=self.request.user)
            if not teams.exists():
                return Response({'error': 'You are not a team leader.'}, status=403)
            else:
                team = teams.first()
           
            projectid=create_project_id()
            supervisor_choices=serializer.validated_data.get('supervisor_choices')
            if supervisor_choices:
                supervisor_choices=User.objects.filter(username__in=supervisor_choices)
                serializer.validated_data['supervisor_choices']=supervisor_choices
            else:
                serializer.validated_data['supervisor_choices']=[]
            
            project=serializer.save(team=team,
                                    projectid=projectid,
                                    status='pending',
                                    supervisor_choices=supervisor_choices)
            return Response({'message': 'Project created successfully.',
                            'projectid': project.projectid,
                            'type': project.type,
                            'title': project.title,
                            'description': project.description,
                            'objectives': project.objectives,
                            'motivation': project.motivation,
                            'area_of_work': project.area_of_work,
                            'supervisor_choices': [supervisor.username for supervisor in project.supervisor_choices.all()],
                            'team': project.team.teamname,
                            'status': project.status,
                            }, status=201)
        
        except Team.DoesNotExist:
            return Response({'error': 'Team not found.'}, status=404)
        


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return Project.objects.filter(team__teammembers=self.request.user)
    
    def get(self,request,*args,**kwargs):
        queryset=self.get_queryset()
        serializer=ProjectSerializer(queryset,many=True)
        return Response(serializer.data)
    
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return Project.objects.filter(team__teammembers=self.request.user)
    
    def patch(self,request,*args,**kwargs):
        try:
            project=self.get_object()
            if project.team.teamleader != request.user:
                return Response({'error': 'Only team leader can update the project.'}, status=403)
            
            serializer=self.get_serializer(project,data=request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
        except Project.DoesNotExist:
            return Response({'error': 'Project not found.'}, status=404)
    
    def delete(self,request,*args,**kwargs):
        try:
            project=self.get_object()
            if project.team.teamleader != request.user:
                return Response({'error': 'Only team leader can delete the project.'}, status=403)
            
            project.delete()
            return Response({'message': 'Project deleted successfully.'}, status=200)
        
        except Project.DoesNotExist:
            return Response({'error': 'Project not found.'}, status=404)
        


class ReportView(generics.CreateAPIView):
    serializer_class = ReportSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        reportid=create_report_id()
        projectid=self.request.user.projectid
        userid=self.request.user.id
        team=Team.objects.get(userid=userid)
        submitted_by=self.request.user
        teamid=team.teamid
        team=Team.objects.get(teamid=teamid)
        project=Project.objects.get(projectid=projectid)
        if project.team.teamleader != self.request.user:
            raise ValidationError('Only team leader can create a report.')
        
        report=serializer.save(
            reportid=reportid,
            project=project,
            submitted_by=submitted_by,
            team=team,
            status='pending'
        )
        return Response({'message': 'Report created successfully.',
                         'reportid': report.reportid,
                         'project': report.project.title,
                         'report': report.report,
                         'created_at': report.created_at,
                         }, status=201)
        
class ReportListView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        user=self.request.user.teamid
        team=Team.objects.get(teamid=user.teamid)
        return Report.objects.filter(team=team)
    
    def get(self):
        queryset=self.get_queryset()
        serializer=ReportSerializer(queryset,many=True)
        return Response(serializer.data)
    
class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        user=self.request.user.teamid
        team=Team.objects.get(teamid=user.teamid)
        return Report.objects.filter(team=team)
    
    def patch(self,request,*args,**kwargs):
        try:
            report=self.get_object()
            if report.submitted_by != request.user:
                return Response({'error': 'Only the submitter can update the report.'}, status=403)
            
            serializer=self.get_serializer(report,data=request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
        except Report.DoesNotExist:
            return Response({'error': 'Report not found.'}, status=404)
    
    def delete(self,request,*args,**kwargs):
        try:
            report=self.get_object()
            if report.submitted_by != request.user:
                return Response({'error': 'Only the submitter can delete the report.'}, status=403)
            
            report.delete()
            return Response({'message': 'Report deleted successfully.'}, status=200)
        
        except Report.DoesNotExist:
            return Response({'error': 'Report not found.'}, status=404)