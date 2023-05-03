from django.urls import path
from tasks.views import ListTasksView, CreateTasksView, \
    UpdateTasksView, DeleteTasksView, DetailTasksView


urlpatterns = [
    path('', ListTasksView.as_view(), name='list_tasks'),
    path('create/', CreateTasksView.as_view(), name='create_task'),
    path('<int:pk>/update/', UpdateTasksView.as_view(), name='update_task'),
    path('<int:pk>/delete/', DeleteTasksView.as_view(), name='delete_task'),
    path('<int:pk>/', DetailTasksView.as_view(), name='detail_task'),
]
