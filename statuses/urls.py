from django.urls import path
from statuses.views import ListStatusesView, CreateStatusesView, \
    UpdateStatusesView, DeleteStatusesView


urlpatterns = [
    path('', ListStatusesView.as_view(), name='list_statuses'),
    path('create/', CreateStatusesView.as_view(), name='create_status'),
    path('<int:pk>/update/', UpdateStatusesView.as_view(), name='update_status'),
    path('<int:pk>/delete/', DeleteStatusesView.as_view(), name='delete_status'),
]
