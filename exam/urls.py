from django.urls import path
from exam import views


urlpatterns = [
    path('showtest/',views.showTest),
]