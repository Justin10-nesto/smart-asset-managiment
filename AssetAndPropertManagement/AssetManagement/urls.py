from django.urls import path
from . import views
urlpatterns = [

    path('assetTypeList', views.assetTypeList, name='assetTypeList'),
    path('assetTypeEdit/<str:id>', views.assetTypeEdit, name='assetTypeEdit'),
    path('assetTypeDelete/<str:id>', views.assetTypeDelete, name='assetTypeDelete'),

    path('assetCategoryList', views.assetCategoryList, name='assetCategoryList'),
    path('assetCategoryEdit/<str:id>', views.assetCategoryEdit, name='assetCategoryEdit'),
    path('assetCategoryDelete/<str:id>', views.assetCategoryDelete, name='assetCategoryDelete'),

    path('assetList', views.assetList, name='assetList'),
    path('assetEdit/<str:id>', views.assetEdit, name='assetEdit'),
    path('assetDelete/<str:id>', views.assetDelete, name='assetDelete'),
    
    path('assetUseList', views.assetUseList, name='assetUseList'),
    path('assetUseEdit/<str:id>', views.assetUseEdit, name='assetUseEdit'),
    path('assetUseDelete/<str:id>', views.assetUseDelete, name='assetUseDelete'),

    path('assetStatusList', views.assetStatusList, name='assetStatusList'),
    path('assetStatusEdit/<str:id>', views.assetStatusEdit, name='assetStatusEdit'),
    path('assetStatusDelete/<str:id>', views.assetStatusDelete, name='assetStatusDelete'),
    
    path('assetRoleList', views.assetRoleList, name='assetRoleList'),
    path('assetRoleEdit/<str:id>', views.assetRoleEdit, name='assetRoleEdit'),
    path('assetRoleDelete/<str:id>', views.assetRoleDelete, name='assetRoleDelete'),

    path('assetDetailList/<str:name>', views.assetDetailList, name='assetDetailList'),
    path('assetDetailEdit/<str:id>', views.assetDetailEdit, name='assetDetailEdit'),
    path('assetDetailDelete/<str:id>', views.assetDetailDelete, name='assetDetailDelete'),
]
