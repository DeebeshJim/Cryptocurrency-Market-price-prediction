from django.urls import path
from . import views

urlpatterns =[
    
    path('', views.Landing_1, name='Landing_1'),
    path('Register_2/', views.Register_2, name='Register_2'),
    path('Login_3/', views.Login_3, name='Login_3'),
    path('Home_4', views.Home_4, name='Home_4'),
    path('bitcoin_report/', views.bitcoin_report, name='bitcoin_report'),
    path('litecoin_report/',views.litecoin_report,name='litecoin_report'),
    path('stellar_report/', views.stellar_report, name='stellar_report'),
    path('Deploy_7/', views.Deploy_7, name='Deploy_7'),
    path('Deploy_9/', views.Deploy_9, name='Deploy_9'),
    path('Deploy_10/', views.Deploy_10, name='Deploy_10'),
    path('bit_db/',views.bit_db,name='bit_db'),
    path('lite_db/',views.lite_db,name='lite_db'),
    path('ste_db/',views.ste_db,name='ste_db'),
    path('Logout/', views.Logout, name='Logout'),
    path('domain/',views.domain,name='domain'),
]