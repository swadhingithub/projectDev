"""
URL configuration for ProjectDev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.schemas import SchemaGenerator

schema_view = get_schema_view(
   openapi.Info(
      title="PIMS SYSTEM OF DAFFOFIL INTERNATIONAL UNIVERSITY",
      default_version='Beta 1.0',
      description="""
      This is the API documentation for the PIMS system of Daffodil International University.
      
        The PIMS system is a system that is used to manage the information of the students, teachers, courses, and other related information of the university.
        API made by @swadhinbiswas
      
      
      """,
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="swadhinbiswas.cse@gmail.com"),
      license=openapi.License(name="Closed Lincese"),
    
    
      
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[],
)

urlpatterns = [
    path('accounts/login/', admin.site.urls),
    path('api/v1/', include('core.urls')),
    path('api/v1/', include('Students.urls')),

  
    path('swagger/<format>/', schema_view.with_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
