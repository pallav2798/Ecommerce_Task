from . import views
from django.urls import path

urlpatterns=[
        path('index/',views.index, name='index'),
        path('signup/',views.signup_view,name='signup'),
        path('update_item/',views.updateitem,name='update_item'),
        path('cart/',views.cart,name='carts'),
        path('email/',views.email,name='email'),
        path('register/',views.signup,name='register'),
        path('',views.login_view,name='login'),
        path('check/',views.login,name='check_user'),
        path('search/',views.search,name='search')
]