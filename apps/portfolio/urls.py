from django.urls import path

from . import views

urlpatterns = [
    path('1',views.admindiplo , name ='admindiplo'  ),
    path('2',views.abakiller , name ='abakiller'  ),
    path('3',views.ultrastalker , name ='ultrastalker'  ),
]