from django.urls import path
from django.urls import path
from .views import UserLoginView,LogoutView,UserRegisterView,ProfileView,StudentUserProfile,protected_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # path('register/teacher/', RegisterTeacherView.as_view(), name='register_teacher'),
    path('student/register/', UserRegisterView.as_view(), name='register_student'),
    path('student/profile/', StudentUserProfile.as_view(), name='student_profile'),
     path('student/login/', UserLoginView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='user_profile'),
     path('protected/',protected_view, name='protected'),
    
    
    
]

