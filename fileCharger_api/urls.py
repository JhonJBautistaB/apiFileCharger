from django.urls import path
from fileCharger_api import views

urlpatterns = [
    path('apiFileCharger/', views.ApiFileChargerView.as_view()),    
]
