from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.redirect_to_auth, name="Home"),
    path('list/', views.list_object.as_view(), name="List_all"),
    path('calendario/', views.calendario_list),
    path('calendario/<int:pk>', views.calendar_detail),
    path('deportistas/', views.deportista_list),
    #path('deportistas/<int:pk>', views.deportist_detail),
    #url(r'adduser/$', views.add_user, name='addUser'),
    #path('calendario/', views.calendario_list),
]
