from django.urls import path
from workshop import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('reviewed/', views.ReviewedView.as_view(), name='reviewed_assignments'),
    path('invoiced/', views.InvoicedView.as_view(), name='invoiced_assignments'),
    path('management/', views.ManagementView.as_view(), name='management'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('order/<int:pk>/invoice/create/', views.CreateInvoiceView.as_view(), name='create_invoice'),
    path('order/<int:pk>/invoice/update/', views.UpdateInvoiceView.as_view(), name='update_invoice'),
    path('order/<int:pk>/invoice/delete/', views.delete_invoice, name='delete_invoice'),
    path('order/<int:pk>/create-guarantee/', views.create_guarantee, name='create_guarantee'),
]