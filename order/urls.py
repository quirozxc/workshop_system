from django.urls import path
from order import views

urlpatterns = [
    path('create/', views.CreateRepairOrderView.as_view(), name='create_order'),
    path('<int:pk>/update/', views.UpdateRepairOrderView.as_view(), name='update_order'),
]