from django.urls import path
from user import views

urlpatterns = [
    path('change-password/', views.CustomPasswordChangeView.as_view(), name='change_password'),
]