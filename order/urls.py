from django.urls import path
from order import views

urlpatterns = [
    path('create/', views.CreateRepairOrderView.as_view(), name='create_order'),
    path('<int:pk>/update/', views.UpdateRepairOrderView.as_view(), name='update_order'),
    path('<int:pk>/mark_as_reviewed', views.mark_as_reviewed, name='mark_as_reviewed'),
    path('<int:pk>/mark_as_returned', views.mark_as_returned, name='mark_as_returned'),
]