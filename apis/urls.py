from django.urls import path, include

from apis import views

app_name = 'apis'

urlpatterns = [
    path('', views.index),
    path('calculate/', views.calculate)
]
