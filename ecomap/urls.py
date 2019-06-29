from django.urls import path
from ecomap.views import base_wiev
from  ecomap.views import base_wiev,category_view,product_view
urlpatterns = [
    path('',base_wiev, name='base'),
]
