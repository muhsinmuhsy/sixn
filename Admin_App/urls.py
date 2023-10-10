from django.urls import path
from Admin_App.views import *

urlpatterns = [

    # --------------------------------------- Sales Manager --------------------------------------- #
    path('salesmanager/list/', salesmanager_list, name='salesmanager-list'),
    path('salesmanager/add/', salesmanager_add, name='salesmanager-add'),
    path('salesmanager/<int:salesmanager_id>/edit/', salesmanager_edit, name='salesmanager-edit'),
    path('salesmanager/<int:salesmanager_id>/delete/', salesmanager_delete, name='salesmanager-delete'),
    path('salesmanager/<int:salesmanager_id>/image/', salesmanager_image, name='salesmanager-image'),

    # --------------------------------------- Purchase Manager --------------------------------------- #
    path('purchasemanager/list/', purchasemanager_list, name='purchasemanager-list'),
    path('purchasemanager/add/', purchasemanager_add, name='purchasemanager-add'),
    path('purchasemanager/<int:purchasemanager_id>/edit/', purchasemanager_edit, name='purchasemanager-edit'),
    path('purchasemanager/<int:purchasemanager_id>/delete/', purchasemanager_delete, name='purchasemanager-delete'),
    path('purchasemanager/<int:purchasemanager_id>/image/', purchasemanager_image, name='purchasemanager-image'),

    # --------------------------------------- Brand --------------------------------------- #
    path('brand/list/', brand_list, name='brand-list'),
    path('brand/add/', brand_add, name='brand-add'),
    path('brand/<int:brand_id>/edit/', brand_edit, name='brand-edit'),
    path('brand/<int:brand_id>/delete/', brand_delete, name='brand-delete'),

    # --------------------------------------- Product --------------------------------------- #
    path('brand/<int:brand_id>/product/list/', product_brand_list, name='product-brand-list'),
    path('brand/<int:brand_id>/product/add/', product_brand_add, name='product-brand-add'),
    path('brand/<int:brand_id>/product/<int:product_id>/edit/', product_brand_edit, name='product-brand-edit'),
    path('brand/<int:brand_id>/product/<int:product_id>/delete/', product_brand_delete, name='product-brand-delete'),

    # --------------------------------------- Product --------------------------------------- #
    path('distributor/list/', distributor_list, name='distributor-list'),
    path('distributor/add/', distributor_add, name='distributor-add'),
    path('distributor/<int:distributor_id>/edit/', distributor_edit, name='distributor-edit'),
    path('distributor/<int:distributor_id>/delete/', distributor_delete, name='distributor-delete'),



]