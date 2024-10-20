from .views import CreateTeamview,InviteTeamview,AcceptTeamInvitationView,NotificationView,UserTeamView,ProjectView,ReportView,ReportListView

from django.urls import path

# teamviewset=CreateTeamview.as_view(
#   {
#     'post':'create',
#     'get':'list'
    
#   }
# )

# inviteviewset=InviteTeamview.as_view(
#   {
#     'post':'create',
#     'get':'list'
    
#   }
# )

# acceptviewset=AcceptTeamInvitationView.as_view(
#   {
#     'post':'create',
#     'get':'list'
    
#   }
# )

urlpatterns = [ 
    path('student/team/', CreateTeamview.as_view()),
    path('student/team/invite/', InviteTeamview.as_view({'post': 'create'}), name='invite-team'),
    path('student/team/invite/<int:pk>/', AcceptTeamInvitationView.as_view()),
    path('student/team/', UserTeamView.as_view(), name='user-teams'),
    path('student/project/', ProjectView.as_view(),name= 'project'),
    path('student/report/', ReportView.as_view(),name= 'report'),
    path('student/report/list/', ReportListView.as_view(),name= 'report-list'),
    path('notifaction/', NotificationView.as_view(),name= 'notification'),
    
    
   
]

