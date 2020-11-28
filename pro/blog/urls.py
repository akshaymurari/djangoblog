from django.urls import path
from . import views
urlpatterns = [
    path('',views.fun,name="home"),
    path('reg',views.reg,name="reg"),
    path('login',views.login,name="login"),
    path('addposts',views.addposts,name="addp"),
    path('addpost',views.addpost,name="addpp"),
    path('logout',views.fun,name="addp11"),
    path('delete',views.dell,name="addp2w"),
    path('page',views.page,name="page"),
]