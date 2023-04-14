from django.urls import path
from statuses import views


urlpatterns = [
    path('', views.ListStatusesView.as_view(), name='list_statuses'),
    path('create/', views.CreateStatusesView.as_view(), name='create_status'),
    path('<int:status_id>/update/', views.UpdateStatusesView.as_view(), name='update_status'),
    path('<int:status_id>/delete/', views.DeleteStatusesView.as_view(), name='delete_status'),
]
