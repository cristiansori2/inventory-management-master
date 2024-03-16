from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.StockListView.as_view(), name='inventory'),
    path('apartados', views.ApartadoslistView.as_view(), name='apartados'),
    path('cadenas', views.CadenaslistView.as_view(), name='cadenas-list'),
    path('anillos', views.AnilloslistView.as_view(), name='anillos-list'),

    path('aretes', views.AreteslistView.as_view(), name='aretes-list'),

    path('dijes', views.DijeslistView.as_view(), name='dijes-list'),

    path('pulsos', views.PulsoslistView.as_view(), name='pulsos-list'),

    path('piercing', views.PiercinglistView.as_view(), name='piercing-list'),




    path('new', views.StockCreateView.as_view(), name='new-stock'),
     path('eliminados', views.EliminadosListView.as_view(), name='eliminados-list'),
    path('stock/<pk>/edit', views.StockUpdateView.as_view(), name='edit-stock'),
    path('stock/<pk>/apartar', views.StockApartarView.as_view(), name='apartar-stock'),
    path('stock/<pk>/delete', views.StockDeleteView.as_view(), name='delete-stock'),
    path('apartados/<pk>/delete', views.ApartarDeleteView.as_view(), name='delete-apartado'),
]