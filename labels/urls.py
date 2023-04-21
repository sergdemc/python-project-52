from django.urls import path
from labels import views


urlpatterns = [
    path('', views.ListLabelsView.as_view(), name='list_labels'),
    path('create/', views.CreateLabelsView.as_view(), name='create_label'),
    path('<int:label_id>/update/', views.UpdateLabelsView.as_view(), name='update_label'),
    path('<int:label_id>/delete/', views.DeleteLabelsView.as_view(), name='delete_label'),
]