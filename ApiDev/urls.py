
from django.urls import path
from .views import *

urlpatterns = [
  path('UserDetails',   UserDetailsView.as_view({
        'post':'create',
        'get':'list'
        })),
  path('UserDetails/name/<str:pk>',   UserDetailsView.as_view({
        'get':'retrieve_per_name'
        })),
  path('UserDetails/<str:pk>',   UserDetailsView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
        })),
 
  path('AssetUserDescription',   AssetUserDescriptionView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('AssetUserDescription/<str:pk>',   AssetUserDescriptionView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
        })), 
  path('Country',   CountryView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('Country/<str:pk>',   CountryView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
        })), 
  path('Region',   RegionView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('Region/<str:pk>',   RegionView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
        })), 
  path('District',   DistrictView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('District/<str:pk>',   DistrictView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get':'retrieve',
        })), 
  path('Ward',   WardView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('Ward/<str:pk>',   WardView.as_view({
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
        'post':'create'
        })), 
  path('AssetUserDescription/<str:pk>',   AssetUserDescriptionView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
        })), 
  path('AssetUser',   AssetUserView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('AssetUser/<str:pk>',   AssetUserView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get':'retrieve'
        })), 
  path('AssetRole', AssetRoleView.as_view({
        'post':'create',
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
        'post':'create',
        'get':'list'
        })),
  path('AssetDetail/name/<str:pk>',   AssetDetailView.as_view({
        'get':'retrieve_per_name'
        })),
  path('AssetDetail/<str:pk>',   AssetDetailView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get': "retrieve"
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
        'post':'create'
        })), 
  path('AssetUserDescription/<str:pk>',   AssetUserDescriptionView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
        })), 
  path('AssetUser',   AssetUserView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('AssetUser/<str:pk>',   AssetUserView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get':'retrieve'
        })),  

  path('Asset',   AssetView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('Asset/<str:pk>',   AssetView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get':'retrieve'
        })), 
  path('AssetType',   AssetTypeView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('AssetType/<str:pk>',   AssetTypeView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get':'retrieve'
        })), 
  path('HouseDetail',   HouseDetailView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('HouseDetail/<str:pk>',   HouseDetailView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get':'retrieve'
        })), 
  path('AssetMaintance',   AssetMaintanceView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('AssetMaintance/<str:pk>',   AssetMaintanceView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get':'retrieve',
        'post':'maintanance_feedback',
        })), 
  path('AssetCategory',   AssetCategoryView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('AssetCategory/<str:pk>',  AssetCategoryView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get':'retrieve'
        })), 

  path('AssetSummary/<str:name>',   AssetSummary.as_view({
        'get':'retrieve_id'
        })), 
  path('AssetSummary/category/<str:name>',   AssetSummary.as_view({
        'get':'retrieve_by_category'
        })),   
]
