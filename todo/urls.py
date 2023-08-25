from django.urls import path
from . import views


urlpatterns = [
    # path('create',views.CreateTodoApiView.as_view(), name='create-todo'),
    path('',views.TodoApiView.as_view(), name='todos'),
    path('<int:id>',views.TodoDetailView.as_view(), name='todo'),
    # path('list',views.TodoListApiView.as_view(), name='list-todo'),
    
]
