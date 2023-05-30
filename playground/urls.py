from django.urls import path
from.import views

urlpatterns = [
    path('login/',views.landing_page,name='landing_page'),
    path('login_page/', views.login_page, name='login_page')
]
