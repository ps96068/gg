# -*- coding: utf-8 -*-
from django.urls import path
from .views import home, ListaDetail, ListaCreate, ListaUpdate, ListaDelete

urlpatterns = [
    path('detail/<int:pk>/', ListaDetail.as_view(), name='detail'),
    path('add/', ListaCreate.as_view(), name='create'),
    path('update/<int:pk>/',ListaUpdate.as_view(), name='update'),
    path('delete/<int:pk>/',ListaDelete.as_view(), name='delete'),
    path('', home, name='home'),

]
