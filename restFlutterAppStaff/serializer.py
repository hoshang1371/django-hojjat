from rest_framework import serializers
from spad_eshop_products.models import Product
# from django.contrib.auth.models import User
from spad_account.models import User

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

from rest_framework.authtoken.models import Token

# from rest_framework.authtoken.models import Token

#Token.objects.filter(pk="0703e9e4e6a24cfce15b26a7fa0544de3c8101ea").exists()  



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

class CheckTokenSerializer(serializers.Serializer):
    token = serializers.EmailField(label=_("token"))

    def validate(self, attrs):
        token = attrs.get('token')
        checked = Token.objects.filter(pk=token).exists()
        attrs['checked'] = checked
        return attrs


class MyAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password",),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            #user2 = User.objects.get(email=email)
            user2 = User.objects.get(Q(username__iexact=email) | Q(email__iexact=email) & Q(is_active=True) & Q(is_staff=True))
            #user = authenticate(request=self.context.get('request'),email=email, password=password)
            user = authenticate(username=user2.username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                #msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
            
        attrs['user'] = user
        return attrs




class SearchProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'