from django.urls import path

from apps import views

# from apps.views import send_email_view

urlpatterns = [
    path('', views.post_list_view, name='list_list'),
    path('detail/<uuid:pk>/', views.post_detail_view, name='post-list'),
]