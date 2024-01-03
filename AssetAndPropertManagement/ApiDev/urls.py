
from django.urls import path
from .views import *

urlpatterns = [
  path('UserDetails',   UserDetailsView.as_view({
        'post':'create_in_builk_or_single',
        'get':'list'
        })),
  path('UserDetails/name/<str:pk>',   UserDetailsView.as_view({
        'get':'retrieve_per_name'
        })),
  path('UserDetails/<str:pk>',   UserDetailsView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
        })),
  path('AssetDescriptionType',   AssetDescriptionTypeView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('AssetDescriptionType/name/<str:pk>',   AssetDescriptionTypeView.as_view({
        'get':'retrieve_per_name',
        })), 
  path('AssetDescriptionType/<str:pk>',   AssetDescriptionTypeView.as_view({
        'patch':'partial_update',
        'delete':'destroy'
        })), 
  path('AssetUserDescription',   AssetUserDescriptionView.as_view({
        'get':'list',
        'post':'create_in_builk_or_single'
        })), 
  path('AssetUserDescription/<str:pk>',   AssetUserDescriptionView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
        })), 
  path('AssetUser',   AssetUserView.as_view({
        'get':'list',
        'post':'create_in_builk_or_single'
        })), 
  path('AssetUser/<str:pk>',   AssetUserView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get':'retrieve'
        })), 
  path('AssetRole', AssetRoleView.as_view({
        'post':'create_in_builk_or_single',
        'get':'list'
    })),
  path('AssetRole/<str:pk>', AssetRoleView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
    })),
  path('AssetRole/update/<str:pk>', AssetRoleView.as_view({
        'post':'update_slots_after_booked_slot',
        
    })),

    path('AssetDetail',   AssetDetailView.as_view({
        'post':'create_in_builk_or_single',
        'get':'list'
        })),
  path('AssetDetail/name/<str:pk>',   AssetDetailView.as_view({
        'get':'retrieve_per_name'
        })),
  path('AssetDetail/<str:pk>',   AssetDetailView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
        })),
  path('AssetDescriptionType',   AssetDescriptionTypeView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('AssetDescriptionType/name/<str:pk>',   AssetDescriptionTypeView.as_view({
        'get':'retrieve_per_name',
        })), 
  path('AssetDescriptionType/<str:pk>',   AssetDescriptionTypeView.as_view({
        'patch':'partial_update',
        'delete':'destroy'
        })), 
  path('AssetUserDescription',   AssetUserDescriptionView.as_view({
        'get':'list',
        'post':'create_in_builk_or_single'
        })), 
  path('AssetUserDescription/<str:pk>',   AssetUserDescriptionView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
        })), 
  path('AssetUser',   AssetUserView.as_view({
        'get':'list',
        'post':'create_in_builk_or_single'
        })), 
  path('AssetUser/<str:pk>',   AssetUserView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get':'retrieve'
        })),  

  path('Asset',   AssetView.as_view({
        'get':'list',
        'post':'create_in_builk_or_single'
        })), 
  path('Asset/<str:pk>',   AssetView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get':'retrieve'
        })),   
]
