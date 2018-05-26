from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('student',views.index,name="student"),
    path('login/',views.LOGIN,name="login"),
    path('job/',views.Job,name="job"),
    path('comp/',views.Compny,name="comp"),
    path('clg/',views.CLG,name="clg"),
    path('ser/',views.search,name='ser')
]

