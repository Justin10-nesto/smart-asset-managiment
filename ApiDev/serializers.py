from rest_framework.serializers import ModelSerializer
from AssetManagement.models import *

class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'
        depth = 4

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        depth = 4

class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
        depth = 4

class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'
        depth = 4

class WardSerializer(ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'
        depth = 4

class AssetTypeSerializer(ModelSerializer):
    class Meta:
        model = AssetType
        fields = '__all__'
        depth = 4
        
class AssetCategorySerializer(ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = '__all__'
        depth = 4

class AssetSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'
        depth = 4

class AssetDescriptionTypeSerializer(ModelSerializer):
    class Meta:
        model = AssetDescriptionType
        fields = '__all__'
        depth = 4

class AssetUseSerializer(ModelSerializer):
    class Meta:
        model = AssetUse
        fields = '__all__'
        depth = 4

class AssetRoleSerializer(ModelSerializer):
    class Meta:
        model = AssetRole
        fields = '__all__'
        depth = 4

class AssetDetailSerializer(ModelSerializer):
    class Meta:
        model = AssetDetail
        fields = '__all__'
        depth = 4

class AssetDescriptionTypeSerializer(ModelSerializer):
    class Meta:
        model = AssetDescriptionType
        fields = '__all__'
        depth = 4

class AssetUserDescriptionSerializer(ModelSerializer):
    class Meta:
        model = AssetUserDescription
        fields = '__all__'
        depth = 4

class AssetUserSerializer(ModelSerializer):
    class Meta:
        model = AssetUser
        fields = '__all__'
        depth = 4

class AssetMaintanceSerializer(ModelSerializer):
    
    class Meta:
        model = AssetMaintance
        fields = '__all__'
        depth = 4

    # def save(self, data):
    #     name = data.get('name', '')[0]
    #     mainannce_date = data.get('mainannce_date', '')[0]
    #     asset = data.get('asset', '')[0]
    #     region = data.get('region', '')[0]
    #     district = data.get('district', '')[0]
    #     ward = data.get('ward', '')[0]

    #     print(region, district, ward)

    #     user = UserDetails.objects.last()
    #     asset_ditails_arr = []
    #     if region != '':
    #         if district != '':
    #             if ward != '':
    #                 asset_detal = AssetDetail.objects.filter(ward = ward)
    #                 if asset_detal.exists():
    #                     for asset in asset_detal:
    #                         asset_ditails_arr.append(asset)
    #             else:
    #                 wards = Ward.objects.filter(district = district)
    #                 if wards.exists():
    #                     for ward_dt in wards:
    #                         district_ward_det = AssetDetail.objects.filter(ward = ward_dt)
    #                         if district_ward_det.exists():
    #                             for district_ward in district_ward_det:
    #                                 asset_ditails_arr.append(district_ward)
    #         else:
    #             districts = District.objects.filter(region = region)
    #             if districts.exists():
    #                 for district in districts:
    #                     wards = Ward.objects.filter(district = district)
    #                     if wards.exists():
    #                         for ward_dt in wards:
    #                             district_ward_det = AssetDetail.objects.filter(ward = ward_dt)
    #                             if district_ward_det.exists():
    #                                 for district_ward in district_ward_det:
    #                                     asset_ditails_arr.append(district_ward)
    #     print(asset_ditails_arr)
    #     if asset_ditails_arr:
    #         for asset_detail_obj in asset_ditails_arr:
    #             AssetMaintance.objects.get_or_create(name = name, mainannce_date = mainannce_date, asset = asset, created_by =user, update_by = user)
    #     asset_updated = AssetMaintance.objects.last()
    #     return asset_updated
    

class HouseDetailSerializer(ModelSerializer):
    class Meta:
        model = HouseDetail
        fields = '__all__'
        depth = 4
