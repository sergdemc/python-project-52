from django.urls import path
from tasks import views


urlpatterns = [
    path('', views.ListTasksView.as_view(), name='list_tasks'),
    path('create/', views.CreateTasksView.as_view(), name='create_task'),
    path('<int:task_id>/update/', views.UpdateTasksView.as_view(), name='update_task'),
    path('<int:task_id>/delete/', views.DeleteTasksView.as_view(), name='delete_task'),
    path('<int:task_id>/', views.DetailTasksView.as_view(), name='detail_task'),
]
