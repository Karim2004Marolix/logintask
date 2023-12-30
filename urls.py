from django.urls import path,include
from .import views
urlpatterns = [
        path('',views.Registration,name='signup'),
        path('login/',views.login,name='login'),
        path('home/',views.home,name='home'),
]