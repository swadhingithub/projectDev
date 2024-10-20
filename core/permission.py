from rest_framework import permissions  


class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to only allow admin users to access.
    """

    def has_permission(self, request, view):
        return request.user.role == 'admin'
      

class IsSuperviser(permissions.BasePermission):
    """
    Custom permission to only allow super admin users to access.
    """

    def has_permission(self, request, view):
        return request.user.role == 'superviser'
      
class IsStudent(permissions.BasePermission):
    """
    Custom permission to only allow student users to access.
    """

    def has_permission(self, request, view):
        return request.user.role == 'student'
      
class IsFaculty(permissions.BasePermission):
    """
    Custom permission to only allow faculty users to access.
    """

    def has_permission(self, request, view):
        return request.user.role == 'faculty'
      
class IsTeamLeader(permissions.BasePermission):
    """
    Custom permission to only allow team leader users to access.
    """

    def has_permission(self, request, view):
        return request.user.role == 'teamleader'
      
      
class IsTeamMember(permissions.BasePermission):
    """
    Custom permission to only allow team member users to access.
    """

    def has_permission(self, request, view):
        return request.user.role == 'teammember'
      
      
class IsDefenseBoard(permissions.BasePermission):
    """
    Custom permission to only allow defense board users to access.
    """

    def has_permission(self, request, view):
        return request.user.role == 'defenseboard'
      
class IsPermitedUser(permissions.BasePermission):
    """
    Custom permission to only allow permited user users to access.
    """

    def has_permission(self, request, view):
        return request.user.role == 'permiteduser'
      

  