from django.urls import path
from workshop import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('management/', views.ManagementView.as_view(), name='management'),
]