from django.contrib import admin
from django.urls import path
from app18 import views as appv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',appv.index),
    path('meds/',appv.list_med),
    path('add_med/',appv.add_med,name="add_med"),
    path('pacientes/',appv.list_pacientes),
    path('add_pac/',appv.add_pac,name="add_pac"),

]
