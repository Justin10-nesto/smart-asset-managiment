from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from .models import *

class UserDetailsView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = UserDetails.objects.filter(pk=pk).first() 
        serializer = UserDetailsSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve_per_name(self,request, pk=None):
        patient_qrset =  UserDetails.objects.filter(full_name=pk) 
        serializer = UserDetailsSerializer(patient_qrset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self,request, pk=None):
        qrset = UserDetails.objects.filter(pk=pk) 
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response('Unable to delete', status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def create(self,request):
        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self,request):
        qrset = UserDetails.objects.all()
        serializer = UserDetailsSerializer(qrset, many=True, )
        # data = serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = UserDetailsSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [UserDetails(**item) for item in request.data]
            UserDetails = UserDetails.objects.bulk_create(bulk_data)
            UserDetails_serializer = UserDetailsSerializer(UserDetails, many=True)
            return Response(UserDetails_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = UserDetails.objects.filter(pk=pk).first() 
        serializer = UserDetailsSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssetDescriptionTypeView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = AssetDescriptionType.objects.filter(pk=pk) 
        serializer = AssetDescriptionTypeSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def retrieve_per_name(self,request, pk=None):
        patient_qrset = AssetDescriptionType.objects.filter(name=pk) 
        serializer = AssetDescriptionTypeSerializer(patient_qrset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self,request, pk=None):
        qrset = AssetDescriptionType.objects.filter(pk=pk)
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response('Unable to delete', status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def list(self,request):
        qrset = AssetDescriptionType.objects.all()
        serializer = AssetDescriptionTypeSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = AssetDescriptionTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = AssetDescriptionType.objects.filter(pk=pk).first() 
        serializer = AssetDescriptionTypeSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetDescriptionTypeSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [AssetDescriptionType(**item) for item in request.data]
            ss = AssetDescriptionType.objects.bulk_create(bulk_data)
            AssetDescriptionType_serializer = AssetDescriptionTypeSerializer(ss, many=True)
            return Response(AssetDescriptionType_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AssetUserDescriptionView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = AssetUserDescription.objects.filter(pk=pk) 
        serializer = AssetUserDescriptionSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def destroy(self,request, pk=None):
        qrset = AssetUserDescription.objects.filter(pk=pk) 
        qrset.delete()
        return Response("deleted", status=status.HTTP_200_OK)
    
    def list(self,request):
        qrset = AssetUserDescription.objects.all()
        serializer = AssetUserDescriptionSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = AssetUserDescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = AssetUserDescription.objects.filter(pk=pk).first()
        serializer = AssetUserDescriptionSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetTypeSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [AssetUserDescription(**item) for item in request.data]
            assetCategories =  AssetUserDescription.objects.bulk_create(bulk_data)
            AssetUserDescription_serializer = AssetUserDescriptionSerializer(assetCategories, many=True)
            return Response(AssetUserDescription_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AssetUserView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = AssetUser.objects.filter(pk=pk) 
        serializer = AssetUserSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def destroy(self,request, pk=None):
        qrset = AssetUser.objects.filter(pk=pk)
        qrset.delete()
        return Response("deleted", status=status.HTTP_200_OK)
    
    def list(self,request):
        qrset = AssetUser.objects.all()
        serializer = AssetUserSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = AssetUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = AssetUser.objects.filter(pk=pk).first()
        serializer = AssetUserSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetUserSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [AssetUser(**item) for item in request.data]
            lab = AssetUser.objects.bulk_create(bulk_data)
            lab_serializer = AssetUserSerializer(lab, many=True)
            return Response(lab_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssetDescriptionTypeView(ViewSet):
    def create(self, request):
        serializer = AssetDescriptionTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetDescriptionTypeSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [AssetDescriptionType(**item) for item in request.data]
            availabilities = AssetDescriptionType.objects.bulk_create(bulk_data)
            avail_serializer = AssetDescriptionTypeSerializer(availabilities, many=True)
        
            return Response(avail_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = AssetDescriptionType.objects.filter(pk=pk).first()
        serializer = AssetDescriptionTypeSerializer(
            instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        query = AssetDescriptionType.objects.all()
        serializer = AssetDescriptionTypeSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def retrieve(self, request, pk=None):
        details = AssetDescriptionType.objects.filter(pk=pk)
        serializer = AssetDescriptionTypeSerializer(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        details = AssetDescriptionType.objects.filter(pk=pk)
        details.delete()
        return Response("deleted", status=status.HTTP_200_OK)
    
class AssetUseView(ViewSet):
    def create(self, request):
        serializer = AssetUseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetUseSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [AssetUse(**item) for item in request.data]
            availabilities = AssetUse.objects.bulk_create(bulk_data)
            avail_serializer = AssetUseSerializer(availabilities, many=True)
        
            return Response(avail_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = AssetUse.objects.filter(pk=pk).first()
        serializer = AssetUseSerializer(
            instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        query = AssetUse.objects.all()
        serializer = AssetUseSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def retrieve(self, request, pk=None):
        details = AssetUse.objects.filter(pk=pk)
        serializer = AssetUseSerializer(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        details = AssetUse.objects.filter(pk=pk)
        details.delete()
        return Response("deleted", status=status.HTTP_200_OK)

class AssetDetailView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = AssetDetail.objects.filter(pk=pk).first() 
        serializer = AssetDetailSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve_per_name(self,request, pk=None):
        patient_qrset =  AssetDetail.objects.filter(full_name=pk) 
        serializer = AssetDetailSerializer(patient_qrset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self,request, pk=None):
        qrset = AssetDetail.objects.filter(pk=pk) 
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response('Unable to delete', status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def create(self,request):
        serializer = AssetDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self,request):
        qrset = AssetDetail.objects.all()
        serializer = AssetDetailSerializer(qrset, many=True, )
        # data = serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetDetailSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [AssetDetail(**item) for item in request.data]
            AssetDetail = AssetDetail.objects.bulk_create(bulk_data)
            AssetDetail_serializer = AssetDetailSerializer(AssetDetail, many=True)
            return Response(AssetDetail_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = AssetDetail.objects.filter(pk=pk).first() 
        serializer = AssetDetailSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssetTypeView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = AssetType.objects.filter(pk=pk) 
        serializer = AssetTypeSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def retrieve_per_name(self,request, pk=None):
        patient_qrset = AssetType.objects.filter(name=pk) 
        serializer = AssetTypeSerializer(patient_qrset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self,request, pk=None):
        qrset = AssetType.objects.filter(pk=pk)
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response('Unable to delete', status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def list(self,request):
        qrset = AssetType.objects.all()
        serializer = AssetTypeSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = AssetTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = AssetType.objects.filter(pk=pk).first() 
        serializer = AssetTypeSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetTypeSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [AssetType(**item) for item in request.data]
            ss = AssetType.objects.bulk_create(bulk_data)
            AssetType_serializer = AssetTypeSerializer(ss, many=True)
            return Response(AssetType_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AssetCategoryView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = AssetCategory.objects.filter(pk=pk) 
        serializer = AssetCategorySerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def destroy(self,request, pk=None):
        qrset = AssetCategory.objects.filter(pk=pk) 
        qrset.delete()
        return Response("deleted", status=status.HTTP_200_OK)
    
    def list(self,request):
        qrset = AssetCategory.objects.all()
        serializer = AssetCategorySerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = AssetCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = AssetCategory.objects.filter(pk=pk).first()
        serializer = AssetCategorySerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetTypeSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [AssetCategory(**item) for item in request.data]
            assetCategories =  AssetCategory.objects.bulk_create(bulk_data)
            AssetCategory_serializer = AssetCategorySerializer(assetCategories, many=True)
            return Response(AssetCategory_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssetView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = Asset.objects.filter(pk=pk) 
        serializer = AssetSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def destroy(self,request, pk=None):
        qrset = Asset.objects.filter(pk=pk)
        qrset.delete()
        return Response("deleted", status=status.HTTP_200_OK)
    
    def list(self,request):
        qrset = Asset.objects.all()
        serializer = AssetSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = Asset.objects.filter(pk=pk).first()
        serializer = AssetSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [Asset(**item) for item in request.data]
            lab = Asset.objects.bulk_create(bulk_data)
            lab_serializer = AssetSerializer(lab, many=True)
            return Response(lab_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssetDescriptionTypeView(ViewSet):
    def create(self, request):
        serializer = AssetDescriptionTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetDescriptionTypeSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [AssetDescriptionType(**item) for item in request.data]
            availabilities = AssetDescriptionType.objects.bulk_create(bulk_data)
            avail_serializer = AssetDescriptionTypeSerializer(availabilities, many=True)
        
            return Response(avail_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = AssetDescriptionType.objects.filter(pk=pk).first()
        serializer = AssetDescriptionTypeSerializer(
            instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        query = AssetDescriptionType.objects.all()
        serializer = AssetDescriptionTypeSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def retrieve(self, request, pk=None):
        details = AssetDescriptionType.objects.filter(pk=pk)
        serializer = AssetDescriptionTypeSerializer(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        details = AssetDescriptionType.objects.filter(pk=pk)
        details.delete()
        return Response("deleted", status=status.HTTP_200_OK)
    
class AssetUseView(ViewSet):
    def create(self, request):
        serializer = AssetUseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetUseSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [AssetUse(**item) for item in request.data]
            availabilities = AssetUse.objects.bulk_create(bulk_data)
            avail_serializer = AssetUseSerializer(availabilities, many=True)
        
            return Response(avail_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = AssetUse.objects.filter(pk=pk).first()
        serializer = AssetUseSerializer(
            instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        query = AssetUse.objects.all()
        serializer = AssetUseSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def retrieve(self, request, pk=None):
        details = AssetUse.objects.filter(pk=pk)
        serializer = AssetUseSerializer(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        details = AssetUse.objects.filter(pk=pk)
        details.delete()
        return Response("deleted", status=status.HTTP_200_OK)

class AssetRoleView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = AssetRole.objects.filter(pk=pk) 
        serializer = AssetRoleSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def destroy(self,request, pk=None):
        qrset = AssetRole.objects.filter(pk=pk)
        qrset.delete()
        return Response("deleted", status=status.HTTP_200_OK)
    
    def list(self,request):
        qrset = AssetRole.objects.all()
        serializer = AssetRoleSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = AssetRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = AssetRole.objects.filter(pk=pk).first()
        serializer = AssetRoleSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetRoleSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [AssetRole(**item) for item in request.data]
            lab = AssetRole.objects.bulk_create(bulk_data)
            lab_serializer = AssetRoleSerializer(lab, many=True)
            return Response(lab_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
