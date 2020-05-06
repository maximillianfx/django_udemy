from django.urls import path, include
from .views import home, my_logout

urlpatterns = [
    path('',home, name = "home"),
    path('logout/',my_logout, name="my_logout")
]
