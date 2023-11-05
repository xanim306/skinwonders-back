from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS




class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        # return request.user.id==1
        return request.user.is_authenticated
        # return request.user.is_superuser
    
    # def has_object_permission(self, request, view, obj):
    #     # Read permissions are allowed to any request,
    #     # so we'll always allow GET, HEAD or OPTIONS requests.
    #     if request.method in SAFE_METHODS:
    #         return True

    #     # Instance must have an attribute named `owner`.
    #     return obj.user == request.user
    