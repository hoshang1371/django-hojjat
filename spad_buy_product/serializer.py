from rest_framework import serializers

from spad_eshop_order.models import OrderDetail
from spad_eshop_products.models import Product

class OrderProductSerializerForListOfbuy(serializers.ModelSerializer):
    class Meta:
        #ToDO
        model = OrderDetail
        # fields = '__all__'
        fields = ('id','count')

#! product order detail delete
class OrderProductDeleteListOfBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'
