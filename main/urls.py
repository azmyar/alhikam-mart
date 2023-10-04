from django.urls import path
from main.views import show_main, create_product, delete_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, add_stock, reduce_stock, edit_product


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),

    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),

    path('create-product', create_product, name='create_product'),
    path('delete-product/<int:id>', delete_product, name='delete_product'),
    path('add-stock/<int:id>', add_stock, name='add_stock'),
    path('reduce-stock/<int:id>', reduce_stock, name='reduce_stock'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),

    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
]