from django.urls import path
from users.views import ListUsersView, RegisterUsersView, \
    UpdateUsersView, DeleteUsersView


urlpatterns = [
    path('', ListUsersView.as_view(), name='list_users'),
    path('create/', RegisterUsersView.as_view(), name='create_user'),
    path('<int:pk>/update/', UpdateUsersView.as_view(), name='update_user'),
    path('<int:pk>/delete/', DeleteUsersView.as_view(), name='delete_user'),
]
