from AssetManagement.models import *

def assetData(request):
    asset_data = Asset.objects.all()
    return {'asset_data':asset_data}
