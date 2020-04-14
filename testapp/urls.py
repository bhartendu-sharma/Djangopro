from django.urls import path
from testapp import views

urlpatterns = [
    path('about/',views.about),
    path('employees/',views.employees_info_views),
]
