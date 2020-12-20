from django.urls import path
from .views import todo_list, todo_details, todo_create, todo_updated, todo_delete


app_name = 'todos'

urlpatterns = [
    path('', todo_list ),
    path('create/', todo_create ),
    path('<id>/', todo_details ),
    path('<id>/update/', todo_updated ),
    path('<id>/delete/', todo_delete),
]
