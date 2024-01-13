import json
from django.db import models
from datetime import timedelta
from django.contrib.auth.models import *
from UAA.models import *

class UserDetails(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    bod = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    photo = models.FileField(upload_to='Photo', null=True, blank=True)
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "User Detail"
        db_table = "User Detail"

class Country(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(UserDetails, related_name='created_countries', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_countries', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Country"
        db_table = "Country"

class Region(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete= models.CASCADE)
    created_by = models.ForeignKey(UserDetails, related_name='created_regions', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_regions', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Region"
        db_table = "Region"

class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete= models.CASCADE)
    created_by = models.ForeignKey(UserDetails, related_name='created_district', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_district', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "District"
        db_table = "District"

class Ward(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete= models.CASCADE)
    created_by = models.ForeignKey(UserDetails, related_name='created_ward', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_ward', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ward"
        db_table = "Ward"
    
class AssetType(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(UserDetails, related_name='created_type', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_type', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Asset Type"
        db_table = "Asset Type"


    
class AssetCategory(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(UserDetails, related_name='created_category', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_category', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Asset Category"
        db_table = "Asset Category"
        
class Asset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(AssetCategory, on_delete= models.CASCADE)
    created_by = models.ForeignKey(UserDetails, related_name='created_asset', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_asset', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class AssetDescriptionType(models.Model):
    name = models.CharField(max_length=100)
    type = models.TextField()
    asset = models.ForeignKey(Asset, on_delete= models.CASCADE)
    created_by = models.ForeignKey(UserDetails, related_name='created_asset_description_type', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_asset_description_type', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        
class AssetUse(models.Model):
    name = models.CharField(max_length=100)
    asset = models.ForeignKey(Asset, on_delete= models.CASCADE)
    created_by = models.ForeignKey(UserDetails, related_name='created_use', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_use', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Asset Use"
        db_table = "Asset Use"
        
class AssetStatus(models.Model):
    name = models.CharField(max_length=100)
    asset = models.ForeignKey(Asset, on_delete= models.CASCADE)
    created_by = models.ForeignKey(UserDetails, related_name='created_asstatus', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_asstatus', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Asset Status"
        db_table = "Asset Status"
        
class PaymentStatus(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Payment Status"
        db_table = "Payment Status"
        
class OwnershipType(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ownership Type"
        db_table = "Ownership Type"
        
class AssetRole(models.Model):
    name = models.CharField(max_length=100)
    asset = models.ForeignKey(Asset, on_delete= models.CASCADE)
    created_by = models.ForeignKey(UserDetails, related_name='created_rotype', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_rotype', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Asset Role"
        db_table = "Asset Role"
       
class AssetDetail(models.Model):
    owner = models.CharField(max_length=100)
    location = models.TextField()
    on_sales = models.BooleanField(default = False)
    needs_tenants = models.BooleanField(default = True)
    amount_per_type = models.BigIntegerField(default= 50000)
    time_duration = models.BigIntegerField(default= 3) #in months
    asset_description = models.JSONField(default = [])
    number_asset_present = models.BigIntegerField(default=1)
    is_house = models.BooleanField(default = False)
    is_tower = models.BooleanField(default = False)
    ward = models.ForeignKey(Ward, on_delete= models.CASCADE, null= True)
    type = models.ForeignKey(AssetType, on_delete= models.CASCADE) # normal, master, rooms only, rooms with sebule
    ownership = models.ForeignKey(OwnershipType, on_delete= models.CASCADE)  # company or indvidual
    asset = models.ForeignKey(Asset, on_delete= models.CASCADE) # house, land, cars etc
    asset_status = models.ForeignKey(AssetStatus, on_delete= models.CASCADE) # DEVELOPMENT, FNISHING, OLD ETC
    asset_use = models.ForeignKey(AssetUse, on_delete= models.CASCADE) # settlemt, farming, bussiness
    paynent = models.ForeignKey(PaymentStatus, on_delete= models.CASCADE) # full payed or not for goverment taxes
    created_by = models.ForeignKey(UserDetails, related_name='created_detail', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_detail', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner
    
    @property
    def assetusers(self):
        asset = AssetDetail.objects.filter(id = self.id).first()
        users = AssetUser.objects.filter(asset = asset)
        return users
    
    def loaded_discription(self):
        house_asset = Asset.objects.get_or_create(name = 'houses')
        asset_detail = AssetDetail.objects.filter(id = self.id)
        house_details = HouseDetail.objects.filter(asset = asset_detail.first())
        if house_details.exists():
            neede_tenant = False
            for house_detail in house_details:
                if not house_detail.have_tenant:
                    neede_tenant = True
            house_details.update(needs_tenants = neede_tenant)
                
        if asset_detail.first().asset.id == house_asset[0].id:
            asset_detail.update(is_house = True)
        return json.loads(self.asset_description)
    
    class Meta:
        verbose_name = "Asset Detail"
        db_table = "Asset Detail"
    
class AssetMaintance(models.Model):
    name = models.CharField(max_length=100)
    mainannce_date = models.DateField()
    is_maintained = models.BooleanField(default = False)
    reason = models.TextField(null = True, blank = True)
    maintained_by = models.JSONField(null = True, blank = True)
    asset = models.ForeignKey(AssetDetail, on_delete= models.CASCADE)
    created_by = models.ForeignKey(UserDetails, related_name='created_type_maintanance', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_type_maintanance', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Asset maintinance"
        db_table = "Asset maintinance"


class HouseDetail(models.Model):
    house_number = models.CharField(max_length=100)
    have_tenant = models.BooleanField(default = False)
    payment_status = models.BooleanField(default = True)
    tenant = models.JSONField(null =True, blank=True)
    owner = models.JSONField(null =True, blank=True)
    asset = models.ForeignKey(AssetDetail, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "House Detail"
        db_table = "House Detail"

class AssetDescriptionType(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Asset Description Type"
        db_table = "Asset Description Type"

class AssetUserDescription(models.Model):
    name = models.CharField(max_length=100)
    type = models.TextField()
    is_required = models.BooleanField(default= True)
    description_type = models.ForeignKey(AssetDescriptionType, null = True, on_delete= models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete= models.CASCADE)
    created_by = models.ForeignKey(UserDetails, related_name='created_asset_user_description_type', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_asset_user_description_type', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Asset User Description"
        db_table = "Asset User Description"

class AssetUser(models.Model):
    full_name = models.CharField(max_length=100)
    description = models.JSONField()
    role = models.ForeignKey(AssetRole, on_delete= models.CASCADE)
    asset = models.ForeignKey(AssetDetail, on_delete= models.CASCADE)
    created_by = models.ForeignKey(UserDetails, related_name='created_asuser', on_delete=models.CASCADE)
    update_by = models.ForeignKey(UserDetails, related_name='updated_asuser', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    def loaded_description(self):
        user_data =  json.loads(self.description)
        return user_data
    
    class Meta:
        verbose_name = "Asset User"
        db_table = "Asset User"
    