from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.StockListView.as_view(), name='inventory'),
    path('apartados', views.ApartadoslistView.as_view(), name='apartados'),
    path('new', views.StockCreateView.as_view(), name='new-stock'),
     path('eliminados', views.EliminadosListView.as_view(), name='eliminados-list'),
    path('stock/<pk>/edit', views.StockUpdateView.as_view(), name='edit-stock'),
    path('stock/<pk>/apartar', views.StockApartarView.as_view(), name='apartar-stock'),
    path('stock/<pk>/delete', views.StockDeleteView.as_view(), name='delete-stock'),
    path('apartados/<pk>/delete', views.ApartarDeleteView.as_view(), name='delete-apartado'),
]