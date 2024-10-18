from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('todos', views.todos, name='todos'),
    path('todos/update', views.update, name='updateTodos'),
    path('account', views.account, name='account')

]