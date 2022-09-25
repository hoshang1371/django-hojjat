from django.urls import path

from spad_eshop_contact.views import contact_page

urlpatterns = [
    path('contact-us', contact_page),
]