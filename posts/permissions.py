# posts/permissions.py
from rest_framework import permissions


class ISAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticated users only can see Listview
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # Always allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user