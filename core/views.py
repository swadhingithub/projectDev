from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema, renderer_classes
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
# from .models import Team, Project, DefenseBoard, Report, Schedule, Comment
# from .froms import TeamSerializer, ProjectSerializer, DefenseBoardSerializer, ReportSerializer, ScheduleSerializer, CommentSerializer
# from rest_framework.schemas import AutoSchema
# from rest_framework.views import APIView 
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# @api_view(['GET', 'POST'])
# @renderer_classes([BrowsableAPIRenderer, JSONRenderer])
# def team_list(request):
#     if request.method == 'GET':
#         teams = Team.objects.all()
#         serializer = TeamSerializer(teams, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TeamSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
# @api_view(['GET', 'PUT', 'DELETE'])
# @renderer_classes([BrowsableAPIRenderer, JSONRenderer])
# def team_detail(request, pk):
#     try:
#         team = Team.objects.get(pk=pk)
#     except Team.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TeamSerializer(team)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TeamSerializer(team, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         team.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
      
# @api_view(['GET', 'POST'])
# @renderer_classes([BrowsableAPIRenderer, JSONRenderer])
# def project_list(request):
#     if request.method == 'GET':
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      


# @api_view(['GET', 'PUT', 'DELETE'])
# @renderer_classes([BrowsableAPIRenderer, JSONRenderer])
# def project_detail(request, pk):
#     try:
#         project = Project.objects.get(pk=pk)
#     except Project.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProjectSerializer(project)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProjectSerializer(project, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         project.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
      
      
# @api_view(['GET', 'POST'])
# @renderer_classes([BrowsableAPIRenderer, JSONRenderer])
# def defenseboard_list(request):
#     if request.method == 'GET':
#         defenseboards = DefenseBoard.objects.all()
#         serializer = DefenseBoardSerializer(defenseboards, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = DefenseBoardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
# @api_view(['GET', 'PUT', 'DELETE'])
# @renderer_classes([BrowsableAPIRenderer, JSONRenderer])
# def defenseboard_detail(request, pk):
#     try:
#         defenseboard = DefenseBoard.objects.get(pk=pk)
#     except DefenseBoard.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DefenseBoardSerializer(defenseboard)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = DefenseBoardSerializer(defenseboard, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         defenseboard.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
      
# @api_view(['GET', 'POST'])
# @renderer_classes([BrowsableAPIRenderer, JSONRenderer])
# def report_list(request):
#     if request.method == 'GET':
#         reports = Report.objects.all()
#         serializer = ReportSerializer(reports, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ReportSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
# @api_view(['GET', 'PUT', 'DELETE'])
# @renderer_classes([BrowsableAPIRenderer, JSONRenderer])

# def report_detail(request, pk):
#     try:
#         report = Report.objects.get(pk=pk)
#     except Report.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ReportSerializer(report)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ReportSerializer(report, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         report.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
      

# @api_view(['GET', 'POST'])
# @renderer_classes([BrowsableAPIRenderer, JSONRenderer])
# def schedule_list(request):
#     if request.method == 'GET':
#         schedules = Schedule.objects.all()
#         serializer = ScheduleSerializer(schedules, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ScheduleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

# @api_view(['GET', 'PUT', 'DELETE'])
# @renderer_classes([BrowsableAPIRenderer, JSONRenderer])
# def schedule_detail(request, pk):
#     try:
#         schedule = Schedule.objects.get(pk=pk)
#     except Schedule.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ScheduleSerializer(schedule)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ScheduleSerializer(schedule, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         schedule.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
      

# class CommentList(ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
    
#     def get_queryset(self):
#         return Comment.objects.filter(user=self.request.user)


# class CommentDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     lookup_field = "id"
#     lookup_url_kwarg = "id"
#     def get_queryset(self):
#         return Comment.objects.filter(user=self.request.user)
    
    
# from django.contrib.auth import authenticate, login
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import viewsets
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import User,Profile
# from .userserilazer import UserSerializer
# from rest_framework import serializers
# from .models import User



# class UserRegistrationView(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer
#     def create(self,serializer):
#         try:
#             user = serializer.save()
#             Profile.objects.create(user=user)
            
#             return Response({'message': 'User registered successfully'})
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
# class UserLoginView(viewsets.ModelViewSet):
    
    
#     def post(self, request):
        
#         username=serializers.CharField()
#         password=serializers.CharField(write_only=True)
#         try :
        

#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 refresh = RefreshToken.for_user(user)
#                 token = str(refresh.access_token)

#                 return Response({'token': token, 'refresh': str(refresh)})
#             else:
#                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            
            
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



# class LogoutView(APIView):
#     def post(self, request):
#         try:
#             refresh_token = request.data['refresh']
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response({'message': 'User logged out successfully'})
        
#         except Exception as e:
#             return Response({'error': 'Invalid token',
#                              'log':f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
        


# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from rest_framework_simplejwt import api_settings
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import User
# from .userserilazer import UserSerializer, LoginSerializer

# class UserRegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserLoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = serializer.validated_data['user']
#         token = api_settings.JWT_ENCODE_HANDLER({
#             'user_id': user.id,
#             'email': user.email,
#         })

#         response = Response({'token': token, 'user': UserSerializer(user).data})
#         response.set_cookie('jwt', token)
#         return response

# class UserLogoutView(generics.GenericAPIView):
#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request):
#         response = Response({'message': 'Logged out successfully'})
#         response.delete_cookie('jwt')
#         return response
    
from rest_framework import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings 

from rest_framework import generics, permissions,viewsets
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from .models import User
from .userserilazer import UserSerializer,LoginSerilizer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .customsuth import studentauthenticate
from django.contrib.auth import authenticate
from rest_framework_simplejwt.exceptions import TokenError
from Students.studentserilizer import StudentProfileSerializer as ProfileSerializer
from Students.models import StudentProfile


# class UserRegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
   
# class Login(generics.GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user=serializer.validated_data['user']
#         token=RefreshToken.for_user(user)
#         return Response({
#             'user':UserSerializer(user).data,
#             'token':str(token.access_token)
#         })
# class UserLogoutView(APIView):
    
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request):
#         request.user.auth_token.delete()
#         return Response({'message': 'Logged out successfully'})

# class UserDashboardView(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = UserSerializer

#     def get_object(self):
#         return self.request.user
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

 
class TokenStore(serializers.Serializer):
    token = serializers.CharField()
    refresh_token = serializers.CharField()

class UserLoginView(generics.GenericAPIView):
    serializer_class = LoginSerilizer
    permission_classes = [permissions.AllowAny]


    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user is not None:
                token = RefreshToken.for_user(user)
                response = Response({
                    'user': UserSerializer(user).data,
                    'token': str(token.access_token),
                    'refresh': str(token),
                })
                response.set_cookie('jwt', str(token.access_token), httponly=True)
                return response
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


## Here is the logout Serilizer
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            serializers = LogoutSerializer(data=request.data)
            if serializers.is_valid():
                refresh_token = serializers.validated_data['refresh']
                try:
                    token = RefreshToken(refresh_token)
                    token.blacklist()
                except TokenError:
                    return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
                return Response({'message': 'User logged out successfully'})
            else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': 'Invalid token', 'log': f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
          

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class=UserSerializer
    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        try:
            profile = StudentProfile.objects.get(user=instance)
            profile_serializer = ProfileSerializer(profile)
        except StudentProfile.DoesNotExist:
            profile_serializer = None

        data = serializer.data
        if profile_serializer:
            data.update(profile_serializer.data)
        
        return Response(data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        # Update user data
        user_serializer = self.get_serializer(instance, data=request.data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        
        profile_data = request.data.get('profile')
        if profile_data:
            try:
                profile = StudentProfile.objects.get(user=instance)
                profile_serializer = ProfileSerializer(profile, data=profile_data, partial=True)
            except StudentProfile.DoesNotExist:
                profile_serializer = ProfileSerializer(data=profile_data, partial=True)
                profile_serializer.is_valid(raise_exception=True)
                profile_serializer.save(user=instance)

            profile_serializer.is_valid(raise_exception=True)
            profile_serializer.save()

        return Response({
            'user': user_serializer.data,
            'profile': profile_serializer.data
        }, status=status.HTTP_200_OK)


class StudentUserProfile(generics.RetrieveUpdateAPIView):
    serializer_class=ProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes=(permissions.IsAuthenticated,)
    def get_object(self):
        return self.request.user.student_profile
    


class TokenObtainPairView(APIView):
    def post(self, request):
        refresh = RefreshToken.for_user(request.user)
        token = str(refresh.access_token)
        return Response({'token': token})
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': 'You are authenticated'})