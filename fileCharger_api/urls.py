from django.urls import path
from fileCharger_api import views

urlpatterns = [
    path('FileCharger/<str:filename>', views.DatasetView.as_view()),    
]
