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


class CountryView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = Country.objects.filter(pk=pk) 
        serializer = CountrySerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def retrieve_per_name(self,request, pk=None):
        patient_qrset = Country.objects.filter(name=pk) 
        serializer = CountrySerializer(patient_qrset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self,request, pk=None):
        qrset = Country.objects.filter(pk=pk)
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response('Unable to delete', status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def list(self,request):
        qrset = Country.objects.all()
        serializer = CountrySerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = Country.objects.filter(pk=pk).first() 
        serializer = CountrySerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = CountrySerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [Country(**item) for item in request.data]
            ss = Country.objects.bulk_create(bulk_data)
            Country_serializer = CountrySerializer(ss, many=True)
            return Response(Country_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RegionView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = Region.objects.filter(pk=pk) 
        serializer = RegionSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def retrieve_per_name(self,request, pk=None):
        patient_qrset = Region.objects.filter(name=pk) 
        serializer = RegionSerializer(patient_qrset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self,request, pk=None):
        qrset = Region.objects.filter(pk=pk)
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response('Unable to delete', status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def list(self,request):
        qrset = Region.objects.all()
        serializer = RegionSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = Region.objects.filter(pk=pk).first() 
        serializer = RegionSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = RegionSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [Region(**item) for item in request.data]
            ss = Region.objects.bulk_create(bulk_data)
            Region_serializer = RegionSerializer(ss, many=True)
            return Response(Region_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DistrictView(ViewSet):
    def retrieve(self,request, pk=None):
        region = Region.objects.get(id = pk)
        qrset = District.objects.filter(region=region) 
        serializer = DistrictSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def retrieve_per_name(self,request, pk=None):
        patient_qrset = District.objects.filter(name=pk) 
        serializer = DistrictSerializer(patient_qrset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self,request, pk=None):
        qrset = District.objects.filter(pk=pk)
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response('Unable to delete', status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def list(self,request):
        qrset = District.objects.all()
        serializer = DistrictSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = District.objects.filter(pk=pk).first() 
        serializer = DistrictSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = DistrictSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [District(**item) for item in request.data]
            ss = District.objects.bulk_create(bulk_data)
            District_serializer = DistrictSerializer(ss, many=True)
            return Response(District_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class WardView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = Ward.objects.filter(pk=pk) 
        serializer = WardSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def retrieve_per_name(self,request, pk=None):
        patient_qrset = Ward.objects.filter(name=pk) 
        serializer = WardSerializer(patient_qrset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self,request, pk=None):
        qrset = Ward.objects.filter(pk=pk)
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response('Unable to delete', status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def list(self,request):
        qrset = Ward.objects.all()
        serializer = WardSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = WardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = Ward.objects.filter(pk=pk).first() 
        serializer = WardSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = WardSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [Ward(**item) for item in request.data]
            ss = Ward.objects.bulk_create(bulk_data)
            Ward_serializer = WardSerializer(ss, many=True)
            return Response(Ward_serializer.data, status=status.HTTP_201_CREATED)
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
        # patient_qrset =  AssetDetail.objects.filter(full_name=pk) 
        patient_qrset =  AssetDetail.objects.all()
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

class AssetMaintanceView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = AssetMaintance.objects.filter(pk=pk) 
        serializer = AssetMaintanceSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def destroy(self,request, pk=None):
        qrset = AssetMaintance.objects.filter(pk=pk)
        qrset.delete()
        return Response("deleted", status=status.HTTP_200_OK)
    
    def list(self,request):
        qrset = AssetMaintance.objects.all()
        serializer = AssetMaintanceSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = AssetMaintanceSerializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            name = data.get('name', '')
            mainannce_date = data.get('mainannce_date', '')
            asset = data.get('asset', '')
            region = data.get('region', '')
            district = data.get('district', '')
            ward = data.get('ward', '')[0]

            print(region, district, ward)

            user = UserDetails.objects.last()
            asset_ditails_arr = []
            if ward :
                asset_detal = AssetDetail.objects.filter(ward = ward)
                # asset_detal = AssetDetail.objects.last()
                if asset_detal.exists():
                    for asset in asset_detal:
                        asset_ditails_arr.append(asset)
                    print(asset_ditails_arr)
            if asset_ditails_arr:
                for asset_detail_obj in asset_ditails_arr:
                    AssetMaintance.objects.get_or_create(name = name, mainannce_date = mainannce_date, asset = asset, created_by =user, update_by = user)
            asset_updated = AssetMaintance.objects.last()
            serializer = AssetMaintanceSerializer(asset_updated)
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        qrset = AssetMaintance.objects.filter(pk=pk).first()
        serializer = AssetMaintanceSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():

            data = request.data
            name = data.get('name', '')
            mainannce_date = data.get('mainannce_date', '')
            asset = data.get('asset', '')
            region = data.get('region', '')
            district = data.get('district', '')
            ward = data.get('ward', '')[0]

            print(region, district, ward)

            user = UserDetails.objects.last()
            asset_ditails_arr = []
            if ward :
                asset_detal = AssetDetail.objects.filter(ward = ward)
                # asset_detal = AssetDetail.objects.last()
                if asset_detal.exists():
                    for asset in asset_detal:
                        asset_ditails_arr.append(asset)
                    print(asset_ditails_arr)
            if asset_ditails_arr:
                for asset_detail_obj in asset_ditails_arr:
                    AssetMaintance.objects.update(name = name, mainannce_date = mainannce_date, asset = asset, created_by =user, update_by = user)
            asset_updated = AssetMaintance.objects.last()
            serializer = AssetMaintanceSerializer(asset_updated)
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def maintanance_feedback(self, request, pk=None):
        qrset = AssetMaintance.objects.filter(pk=pk)
        data = request.data
        name = data.get('name', qrset.first().name)
        maintaanance_date = data.get('maintaanance_date', qrset.first().mainannce_date)
        is_maintained = data.get('is_maintained', 0)
        reason = data.get('reason', '')
        maintained_by = data.get('maintained_by', [])


        if qrset.exists():
            qrset.update(mainannce_date = maintaanance_date, is_maintained = is_maintained, reason = reason, maintained_by = maintained_by)
            return Response("updated", status=status.HTTP_200_OK)
        return Response("not updated", status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = AssetMaintanceSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [AssetMaintance(**item) for item in request.data]
            lab = AssetMaintance.objects.bulk_create(bulk_data)
            lab_serializer = AssetMaintanceSerializer(lab, many=True)
            return Response(lab_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HouseDetailView(ViewSet):
    def retrieve(self,request, pk=None):
        qrset = HouseDetail.objects.filter(pk=pk) 
        serializer = HouseDetailSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    def retrieve_by_user(self, request):
        qrset = HouseDetail.objects.all()
        serializer = HouseDetailSerializer(qrset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self,request, pk=None):
        qrset = HouseDetail.objects.filter(pk=pk)
        qrset.delete()
        return Response("deleted", status=status.HTTP_200_OK)
    
    def list(self,request):
        qrset = HouseDetail.objects.all()
        serializer = HouseDetailSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):

        print(request.data)
        name = request.data['name']
        tenant = request.data['tenant']
        owner = request.data['owner']
        asset_id = request.data['asset'][0]
        house_number = request.data['house_number']
        asset = AssetDetail.objects.filter(id = asset_id).first()
        house = HouseDetail.objects.get_or_create(house_number = house_number[0], have_tenant = True, payment_status = True, tenant = tenant[0], owner = owner[0], asset = asset)
        print(" ccreated ok")
        serializer = HouseDetailSerializer(house[0])
        return Response(serializer.data, status=status.HTTP_201_CREATED)  
    
    def partial_update(self, request, pk=None):
        qrset = HouseDetail.objects.filter(pk=pk).first()
        serializer = HouseDetailSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = HouseDetailSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [HouseDetail(**item) for item in request.data]
            lab = HouseDetail.objects.bulk_create(bulk_data)
            lab_serializer = HouseDetailSerializer(lab, many=True)
            return Response(lab_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssetSummary(ViewSet):
    def retrieve_id(self,request, name='House'):
        asset = Asset.objects.filter(name = name).first()
        userDetail = AssetDetail.objects.filter(asset=asset)
        maintanace = AssetMaintance.objects.filter(asset = asset, is_maintained = False)
        number_assets = userDetail.count()
        # for maint in maintanace:
        #     if maint.maintanance_date_has_passed():
        #         asset_needs_maintanance += 1
        return Response({'number_asset':number_assets, 'number_asset_need_maintanance':maintanace.count()}, status=status.HTTP_200_OK) 
    
    def retrieve_by_category(self,request, name):
        category = AssetCategory.objects.filter(name = name).first()
        asset = Asset.objects.filter(name = 'houses', category=category).first()
        userDetail = AssetDetail.objects.filter(asset=asset)
        serialiizer = AssetDetailSerializer(userDetail, many=True)
        return Response(serialiizer.data, status=status.HTTP_200_OK) 
    