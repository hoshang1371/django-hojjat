from rest_framework import serializers

from post_information.models import PostAddress


#! product order delete
class PostAddressDeleteListOfBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAddress
        fields = '__all__'