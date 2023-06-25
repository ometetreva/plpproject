from django.urls import path
from .views import * #signup, process_form, login, home, logout, product_details, add_to_cart, cart, decrease_quantity, increase_quantity

urlpatterns = [
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
    path('process_form/', process_form, name='process_form'),
    path('home/', home, name='home'),
    path('logout/', logout, name='logout'),
    path('product/<int:id>', product_details, name='product_details'),
    path('add_to_cart/<int:id>', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('decrease_quantity/<int:id>', decrease_quantity, name='decrease_quantity'),
    path('increase_quantity/<int:id>', increase_quantity, name='increase_quantity'), 
    path('remove/<int:id>', remove, name='remove')
]