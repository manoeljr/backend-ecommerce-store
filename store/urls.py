from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('api/v1/', views.ProductListView.as_view(), name='store_home'),
]
