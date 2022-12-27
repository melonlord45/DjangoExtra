from django.urls import path
from todofeature.views import todo_list_view, todo_add_view


app_name = "todofeature"
urlpatterns = [
    path("", todo_list_view, name="todo_list"),
    path("todo-add/", todo_add_view, name="todo_add"),
]
