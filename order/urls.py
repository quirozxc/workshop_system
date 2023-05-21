from django.urls import path
from order import views

urlpatterns = [
    path('create/', views.RepairOrderView.as_view(), name='create_order'),
]