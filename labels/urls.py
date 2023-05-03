from django.urls import path
from labels.views import ListLabelsView, CreateLabelsView, \
    UpdateLabelsView, DeleteLabelsView


urlpatterns = [
    path('', ListLabelsView.as_view(), name='list_labels'),
    path('create/', CreateLabelsView.as_view(), name='create_label'),
    path('<int:pk>/update/', UpdateLabelsView.as_view(), name='update_label'),
    path('<int:pk>/delete/', DeleteLabelsView.as_view(), name='delete_label'),
]
