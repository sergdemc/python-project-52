from django.urls import path
from users import views


urlpatterns = [
    path('', views.ListUsersView.as_view(), name='list_users'),
    path('create/', views.RegisterUsersView.as_view(), name='create_user'),
    path('<int:user_id>/update/', views.UpdateUsersView.as_view(), name='update_user'),
    path('<int:user_id>/delete/', views.DeleteUsersView.as_view(), name='delete_user'),
]
