from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('todos', views.todos, name='todos'),
    path('update', views.update, name='updateTodos'),
    path('account', views.account, name='account'),
    path('login', views.login, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register')

]