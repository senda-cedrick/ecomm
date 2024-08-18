from django.urls import path
from .views import home,products,singleproduct,store
urlpatterns = [
    path('',home,name='home'),
    path('products/',products, name='products'),
    path('singleproduct/',singleproduct, name='singleproduct'),
    path('store/',store, name='store'),
]