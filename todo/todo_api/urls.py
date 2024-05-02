
# todo/todo_api/urls.py : API urls.py

from django.urls import path, include
from . import views
urlpatterns = [
    path('todolist/',views.TodoListApiView.as_view(),name="todo-list-view" ),
]