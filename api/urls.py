
from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverView,name='api-overview'),
    path('list/', views.taskList,name='task'),
    path('detail/<str:pk>/', views.taskDetail,name='detail'),
    path('create/', views.taskCreate,name='Create'),
    path('update/<str:pk>/', views.taskUpdate,name='update'),
    path('delete/<str:pk>/', views.taskDelete,name='delete'),
]
