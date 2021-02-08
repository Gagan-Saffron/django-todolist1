from django.urls import path
from django.contrib import admin
from .views import home_view,delete_task_view,done_task_view,delete_done_view

urlpatterns=[
    path('delete_task/<int:task_id>/',delete_task_view,name='delete'),
    path('done_task/<int:task_id>/',done_task_view,name='done'),
    path('delete_done/<int:task_id>/',delete_done_view,name='delete_done'),
]
