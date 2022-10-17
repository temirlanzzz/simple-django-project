from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('this/all/', views.getProducts),
    path('this/create/', views.createProduct),
    path('this/<str:pk>/update/', views.updateProduct),
    path('this/<str:pk>/delete/', views.deleteProduct),
    path('this/<str:pk>/', views.getProduct),
    path('countries/', views.getCountries),
    path('countries/create/', views.createCountry),
    path('countries/<str:pk>/update/', views.updateCountry),
    path('countries/<str:pk>/delete/', views.deleteCountry),
    path('countries/<str:pk>/', views.getCountry),
]