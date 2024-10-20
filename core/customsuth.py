
from .models import User  # Ensure you have imported the correct User model
from django.views.decorators.debug import sensitive_variables
          


@sensitive_variables('credentials')
def studentauthenticate(request=None,**credentials):
    getusername=credentials.get('username')
    getpassword=credentials.get('password')
    if getusername is None or getpassword is None:
        return None
    try:
        user=User.objects.get(username=getusername)
    except User.DoesNotExist:
        return None
    if user.check_password(getpassword):
        return user
    return None
def get_user(self,user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None
    
@sensitive_variables('credentials')
class CustomauthForTeacher:
  def authenticate(self,**credentials):
    getusername=credentials.get('username')
    getpassword=credentials.get('password')
    if getusername is None or getpassword is None:
        return None
    try:
        user=User.objects.get(username=getusername)
    except User.DoesNotExist:
        return None
    if user.check_password(getpassword):
        return user
    return None
  def get_user(self,user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None