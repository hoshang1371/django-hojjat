from rest_framework import serializers
from spad_eshop_products.models import Product
# from django.contrib.auth.models import User
from spad_account.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = [
        #     'title', 'code', 'place', 'number', 'price', 'active',
        # ]
        fields = "__all__"
        #exclude = ["image"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"