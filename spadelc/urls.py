"""spadelc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import (home_page, products_order_partial ,UpdateCrudUser ,DeleteCrudUser 
                    ,products_number_all_order_partial ,DeleteCrudUserAll,
                    CreateOneOrder,about_page_footer ,about_page_header,about_page,
                    products_category)


from spadelc import settings

urlpatterns = [
    path('', home_page),
    path('about-us',about_page),
 #   path('login', login),
    path('',include('spad_account.urls')),
    path('',include('spad_eshop_products.urls')),
    path('admin/', admin.site.urls),
    path('', include('spad_eshop_order.urls')),

    path('api/',include('restFlutterAppStaff.urls')),
    path('buy/',include('spad_buy_product.urls')),
    
    path('products_order_partial',products_order_partial, name='products_order_partial'),
    path('products_number_all_order_partial',products_number_all_order_partial, 
        name='products_number_all_order_partial'),

    path('products_category',products_category, 
        name='products_category'),
        
    path('about_page_footer',about_page_footer, 
        name='about_page_footer'),
    path('about_page_header',about_page_header, 
        name='about_page_header'),
    path('', include('spad_eshop_contact.urls')),
    path('ajax/crud/update/',  UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('ajax/crud/delete/',  DeleteCrudUser.as_view(), name='crud_ajax_delete'),   
    path('ajax/crud/delete/all',  DeleteCrudUserAll.as_view(), 
        name='crud_ajax_delete_all'),
    path('ajax/crud/create/OneProduct',  CreateOneOrder.as_view(), name='crud_ajax_create_one'),

    path('', include('social_django.urls', namespace='social')),

    #! drf
    #path('api-auth/', include('rest_framework.urls'))

]

urlpatterns += [
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
