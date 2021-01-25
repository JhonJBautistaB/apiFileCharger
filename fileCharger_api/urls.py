from django.urls import path
from fileCharger_api import views

urlpatterns = [
    path('v1/dataset/<str:filename>', views.DatasetView.as_view()),    
    path('v1/dataset/', views.DatasetView.as_view()),
    path('v1/rows/', views.RowsView.as_view()),
]
