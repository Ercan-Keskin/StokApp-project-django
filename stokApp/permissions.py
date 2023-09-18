from rest_framework import permissions



class IsStaffOrReadOnly(permissions.IsAdminUser):
#Sadece staff kullanıcıların PUT, POST ve DELETE işlemlerini yapmasına izin verir.

    def has_permission(self, request, view):
 # GET, HEAD veya OPTIONS isteklerine her zaman izin ver
        if request.method in permissions.SAFE_METHODS:
            return True
 # Diğer işlemlerde sadece staff kullanıcılara izin ver
        return bool(request.user and request.user.is_staff)
# --------------------------------------------------------------

    

class IsOwnerOrReadOnlyComment(permissions.BasePermission):
    #Kullanıcı kendi işlemlerini düzenleyebilir.
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: 
            return True
        return bool(obj.user == request.user)
