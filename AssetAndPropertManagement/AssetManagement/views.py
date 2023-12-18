from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import transaction
from AssetManagement.models import *
from UAA.permissionChecking import permission_required

@transaction.atomic()
@permission_required(['AssetManagement.add_assettype', 'AssetManagement.view_assettype'])
def assetTypeList(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = UserDetails.objects.get(user = request.user)
        AssetType.objects.create(name = name, created_by = user, update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    assetType_info = AssetType.objects.all()
    context = {'assetType_info':assetType_info,}
    return render(request, 'AssetManagement/list-assetType.html', context)

@transaction.atomic()
@permission_required(['AssetManagement.change_assettype'])
def assetTypeEdit(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        content = AssetType.objects.filter(id = id)
        user = UserDetails.objects.get(user = request.user)
        content.update(name = name, update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@transaction.atomic()
@permission_required(['AssetManagement.delete_assettype'])
def assetTypeDelete(request, id):
    AssetType.objects.filter(id= id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@transaction.atomic()
@permission_required(['AssetManagement.add_assetcategory', 'AssetManagement.view_assetcategory'])
def assetCategoryList(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = UserDetails.objects.get(user = request.user)
        AssetCategory.objects.create(name = name, created_by = user, update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    assetCategory_info = AssetCategory.objects.all()
    context = {'assetCategory_info':assetCategory_info,}
    return render(request, 'AssetManagement/list-assetCategory.html', context)

@transaction.atomic()
@permission_required(['AssetManagement.change_assetcategory'])
def assetCategoryEdit(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        content = AssetCategory.objects.filter(id = id)
        user = UserDetails.objects.get(user = request.user)
        content.update(name = name, update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@transaction.atomic()
@permission_required(['AssetManagement.delete_assetcategory'])
def assetCategoryDelete(request, id):
    AssetCategory.objects.filter(id= id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@transaction.atomic()
@permission_required(['AssetManagement.add_asset', 'AssetManagement.view_asset'])
def assetList(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        category = AssetCategory.objects.get(id = category_id)

        user = UserDetails.objects.get(user = request.user)
        Asset.objects.create(name = name, description= description, category = category, created_by = user, update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    asset_info = Asset.objects.all()
    categories = AssetCategory.objects.all()
    context = {'asset_info':asset_info, 'categories':categories}
    return render(request, 'AssetManagement/list-asset.html', context)

@transaction.atomic()
@permission_required(['AssetManagement.change_asset'])
def assetEdit(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        category = AssetCategory.objects.get(id = category_id)

        user = UserDetails.objects.get(user = request.user)
        content = Asset.objects.filter(id = id)
        content.update(name = name, description= description, category = category, update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@transaction.atomic()
@permission_required(['AssetManagement.delete_asset'])
def assetDelete(request, id):
    Asset.objects.filter(id= id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@transaction.atomic()
@permission_required(['AssetManagement.add_assetuse', 'AssetManagement.view_assetuse'])
def assetUseList(request):
    if request.method == "POST":
        name = request.POST.get('name')
        asset_id = request.POST.get('asset')
        asset = Asset.objects.get(id = asset_id)
        user = UserDetails.objects.get(user = request.user)
        AssetUse.objects.create(name = name, asset= asset, created_by = user, update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    asset_info = AssetUse.objects.all()
    assets = Asset.objects.all()
    context = {'asset_info':asset_info, 'assets':assets}
    return render(request, 'AssetManagement/list-assetUse.html', context)

@transaction.atomic()
@permission_required(['AssetManagement.change_assetuse'])
def assetUseEdit(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        asset_id = request.POST.get('asset')
        asset = Asset.objects.get(id = asset_id)
        user = UserDetails.objects.get(user = request.user)
        content = AssetUse.objects.filter(id = id)
        content.update(name = name, asset= asset,  update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@transaction.atomic()
@permission_required(['AssetManagement.delete_assetuse'])
def assetUseDelete(request, id):
    AssetUse.objects.filter(id= id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@transaction.atomic()
@permission_required(['AssetManagement.add_assetstatus', 'AssetManagement.view_assetstatus'])
def assetStatusList(request):
    if request.method == "POST":
        name = request.POST.get('name')
        asset_id = request.POST.get('asset')
        asset = Asset.objects.get(id = asset_id)
        user = UserDetails.objects.get(user = request.user)
        AssetStatus.objects.create(name = name, asset= asset, created_by = user, update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    asset_info = AssetStatus.objects.all()
    assets = Asset.objects.all()
    context = {'asset_info':asset_info, 'assets':assets}
    return render(request, 'AssetManagement/list-assetStatus.html', context)

@transaction.atomic()
@permission_required(['AssetManagement.change_assetstatus'])
def assetStatusEdit(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        asset_id = request.POST.get('asset')
        asset = Asset.objects.get(id = asset_id)
        user = UserDetails.objects.get(user = request.user)
        content = AssetStatus.objects.filter(id = id)
        content.update(name = name, asset= asset,  update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@transaction.atomic()
@permission_required(['AssetManagement.delete_assetstatus'])
def assetStatusDelete(request, id):
    AssetStatus.objects.filter(id= id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@transaction.atomic()
@permission_required(['AssetManagement.add_assetrole', 'AssetManagement.view_assetrole'])
def assetRoleList(request):
    if request.method == "POST":
        name = request.POST.get('name')
        asset_id = request.POST.get('asset')
        asset = Asset.objects.get(id = asset_id)
        user = UserDetails.objects.get(user = request.user)
        AssetRole.objects.create(name = name, asset= asset, created_by = user, update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    asset_info = AssetRole.objects.all()
    assets = Asset.objects.all()
    context = {'asset_info':asset_info, 'assets':assets}
    return render(request, 'AssetManagement/list-assetRole.html', context)

@transaction.atomic()
@permission_required(['AssetManagement.change_assetrole'])
def assetRoleEdit(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        asset_id = request.POST.get('asset')
        asset = Asset.objects.get(id = asset_id)
        user = UserDetails.objects.get(user = request.user)
        content = AssetRole.objects.filter(id = id)
        content.update(name = name, asset= asset,  update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@transaction.atomic()
@permission_required(['AssetManagement.delete_assetrole'])
def assetRoleDelete(request, id):
    AssetRole.objects.filter(id= id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@transaction.atomic()
@permission_required(['AssetManagement.add_assetdetail', 'AssetManagement.view_assetdetail'])
def assetDetailList(request, name):
    asset_info = Asset.objects.get(name = name)
    if request.method == "POST":
        owner = request.POST.get('owner')
        location = request.POST.get('location')
        description = request.POST.get('description')
        number_asset_present = request.POST.get('number_asset_present')
        type_id = request.POST.get('type')
        ownership_id = request.POST.get('ownership')
        asset_status_id = request.POST.get('asset_status')
        assets_use_id = request.POST.get('assets_use')
        payment_status_id = request.POST.get('payment_status')
        owner = request.POST.get('owner')
        payment_status = request.POST.get('payment_status')
        asset_id = request.POST.get('asset')
        
        type = AssetType.objects.get(id = type_id)
        ownership = OwnershipType.objects.get(id = ownership_id)
        asset_status = AssetStatus.objects.get(id = asset_status_id)
        assets_use= AssetUse.objects.get(id = assets_use_id)
        payment= PaymentStatus.objects.get(id = payment_status_id)
        user = UserDetails.objects.get(user = request.user)
        
        AssetDetail.objects.create(owner = owner, location= location, asset_description= description, type= type, ownership= ownership, asset= asset_info, asset_status= asset_status, asset_use= assets_use, paynent= payment, created_by = user, update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    payment_status_arry = ['Pending', 'Completed', 'Not Paid']
    for payment in payment_status_arry:
        payment_state = PaymentStatus.objects.get_or_create(name = payment, )
        
    ownership_status_arry = ['Private', 'Organization', 'partnership']
    for ownership in ownership_status_arry:
        ownership_state = OwnershipType.objects.get_or_create(name = ownership, )
        
    types = AssetType.objects.all()
    ownerships = OwnershipType.objects.all()
    asset_status= AssetStatus.objects.all()
    payment_status= PaymentStatus.objects.all()
    assets_uses = AssetUse.objects.filter(asset = asset_info)
    assets_details = AssetDetail.objects.filter(asset = asset_info)

    context = {'asset':asset_info, 'assets_details':assets_details, 'types':types, 'assets_uses':assets_uses, 'asset_status':asset_status, 'ownerships':ownerships, 'payment_status':payment_status}
    return render(request, 'AssetManagement/list-assetDetail.html', context)

@transaction.atomic()
@permission_required(['AssetManagement.change_assetdetail'])
def assetDetailEdit(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        asset_id = request.POST.get('asset')
        asset = Asset.objects.get(id = asset_id)
        user = UserDetails.objects.get(user = request.user)
        content = AssetDetail.objects.filter(id = id)
        content.update(name = name, asset= asset,  update_by = user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@transaction.atomic()
@permission_required(['AssetManagement.delete_assetdetail'])
def assetDetailDelete(request, id):
    AssetDetail.objects.filter(id= id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

