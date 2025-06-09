from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('task-list/', views.TaskListView.as_view(), name='task-list'),
    path('task/add/', views.TaskCreateView.as_view(), name='task-add'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task-edit'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]

urlpatterns += [
    path('api/tasks/', api_views.TaskListCreateAPI.as_view(), name='api-task-list-create'),
    path('api/tasks/<int:pk>/', api_views.TaskRetrieveUpdateDeleteAPI.as_view(), name='api-task-detail'),
]