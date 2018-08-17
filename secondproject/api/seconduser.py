from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from secondproject.models.online import Register, Orders


class FirstpageResource(ModelResource):
    class Meta:
        collection_name = "data"
        queryset = Register.objects.all()
        resource_name = 'register221'
        authorization = Authorization()


class SecondpageResource(ModelResource):
    class Meta:
        collection_name = "data"
        queryset = Orders.objects.all()
        resource_name = 'order256'
        authorization = Authorization()
