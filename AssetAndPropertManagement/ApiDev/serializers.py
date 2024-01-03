from rest_framework.serializers import ModelSerializer
from AssetManagement.models import *

class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'


class AssetTypeSerializer(ModelSerializer):
    class Meta:
        model = AssetType
        fields = '__all__'
        
        
class AssetCategorySerializer(ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = '__all__'
        
class AssetSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class AssetDescriptionTypeSerializer(ModelSerializer):
    class Meta:
        model = AssetDescriptionType
        fields = '__all__'

class AssetUseSerializer(ModelSerializer):
    class Meta:
        model = AssetUse
        fields = '__all__'

class AssetRoleSerializer(ModelSerializer):
    class Meta:
        model = AssetRole
        fields = '__all__'

class AssetDetailSerializer(ModelSerializer):
    class Meta:
        model = AssetDetail
        fields = '__all__'

class AssetDescriptionTypeSerializer(ModelSerializer):
    class Meta:
        model = AssetDescriptionType
        fields = '__all__'

class AssetUserDescriptionSerializer(ModelSerializer):
    class Meta:
        model = AssetUserDescription
        fields = '__all__'

class AssetUserSerializer(ModelSerializer):
    class Meta:
        model = AssetUser
        fields = '__all__'