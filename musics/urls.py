from django.urls import path

from musics import views
urlpatterns=[
path('',views.main,name="main"),
path('index',views.index,name="index"),
path('regist', views.regist, name="regist"),
path('registrationsave', views.registrationsave, name="registrationsave"),
path('upload', views.upload, name="upload"),
path('logincode', views.logincode, name="logincode"),
path('savemusic', views.savemusic, name="savemusic"),
path('viewmusic', views.viewmusic, name="viewmusic"),
path('viewmysong', views.viewmysong, name="viewmysong"),
path('viewmyprivatesong', views.viewmyprivatesong, name="viewmyprivatesong"),
path('delete_music/<int:id>/', views.delete_music, name="delete_music"),
path('logout', views.logout, name="logout"),

]
