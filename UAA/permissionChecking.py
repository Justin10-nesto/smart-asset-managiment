from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from AssetManagement.models import *

def permission_required(permissions):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.id:
                userDetail =    UserDetails.objects.filter(user = request.user)
                if userDetail.exists():
                    for permission in permissions:
                        if request.user.has_perm(permission):
                            
                            return view_func(request, *args, **kwargs)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    return redirect('UserDetailPage')

            else:
                return redirect('loginPage')
        return wrapper

    return decorator
