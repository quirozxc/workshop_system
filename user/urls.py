from django.urls import path
from user import views

urlpatterns = [
    path('list/', views.UserListView.as_view()),
    path('<int:pk>/detail/', views.UserDetailView.as_view()),
]