from django.contrib import admin
from django.urls import path
from .test_view import *
from redcap_database import test_view

urlpatterns = [path('admin/', admin.site.urls),
path('test_ui/', views.test_datalist, name='UI'),
path('test_ui/applied_science_engineering_edit.html/', views.applied_science_engineering, name='Applied_Science_Engineering'),
path('test_ui/architecture.html/', views.architecture, name='Architecture'),
path('test_ui/convocation_office.html/', views.convocation_office, name='Convocation_Office'),
path('test_ui/dlsph.html/', views.dala_lana_school_of_public_health, name='Dala_Lana_School_of_Public_Health'),]
