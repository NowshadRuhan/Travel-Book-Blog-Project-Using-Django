from django.urls import path
from App_Login import views



app_name = 'App_Login'

urlpatterns = [
    path('sign-up/', views.signUp, name='signup'),
    path('sign-in/', views.signin, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('user/', views.user_profile, name='profile'),
    path('change-profile/', views.user_change, name='update'),
    path('password/', views.pass_change, name='password'),
    path('add-pro-pic/', views.add_pro_pic, name='addProPic'),
    path('change-pro-pic/', views.changeProPic, name='changeProPic'),
]
