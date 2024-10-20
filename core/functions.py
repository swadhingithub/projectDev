import random 
import string



def create_defence_id():
    return 'de'.join(random.choices(string.ascii_uppercase + string.digits, k=6))
  
def create_report_id():
    return 're'.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def create_project_id():
    return 'pr'.join(random.choices(string.ascii_uppercase + string.digits, k=6))
  
def create_team_id():
    return 'te'.join(random.choices(string.ascii_uppercase + string.digits, k=6))
  

# def get_user_role(user):
#     if user.is_superuser:
#         return 'admin'
#     if hasattr(user, 'student'):
#         return 'student'
#     if hasattr(user, 'faculty'):
#         return 'faculty'
#     return 'user'

# def get_user_by_username(username):
#     try:
#         return User.objects.get(username=username)
#     except User.DoesNotExist:
#         return None
# def get_user_by_email(email):
#     try:
#         return User.objects.get(email=email)
#     except User.DoesNotExist:
#         return None
    
# def get_user_by_id(id):
#     try:
#         return User.objects.get(id=id)
#     except User.DoesNotExist:
#         return None