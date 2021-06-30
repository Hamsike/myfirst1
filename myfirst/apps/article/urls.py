from django.urls import path

from . import views

app_name = 'article'
urlpatterns = [
    path('article/', views.index, name='index'),
    path('article/<int:article_id>/', views.detail, name='detail'),
    path('article/<int:article_id>/comm/', views.comm, name='comm'),
    path('', views.glav, name='glav')
]
