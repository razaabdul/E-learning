# from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsCourseAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow course owners to edit or delete their own courses,
    while allowing unauthenticated users read-only access.
    """
    def has_permission(self, request, view):
        # Allow GET, HEAD, or OPTIONS requests for unauthenticated users
        if request.method in permissions.SAFE_METHODS and not request.user.is_authenticated:
            return True
        
        # Allow authenticated users to perform any request
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow unauthenticated users read-only access
        if not request.user.is_authenticated:
            return True

        # Check if the user making the request is the owner of the course
        return obj.teacher == request.user
class IsSchoolAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.user_type in ['admin']
    

