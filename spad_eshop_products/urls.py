from django.urls import path
#from django.urls.conf import include
from .views import (products ,ProductList,ProductListByCategory,
                    products_categories_partial,product_detail,
                    SearchProductsView)

urlpatterns = [
    path('products-function', products),
    path('products', ProductList.as_view()),
    path('products/<productId>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
    path('products_categories_partial',products_categories_partial, name='products_categories_partial'),
    path('products/<category_name>', ProductListByCategory.as_view()),

]