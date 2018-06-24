from django.conf.urls import url
from . import views


app_name = 'df_user'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register_handle/$', views.register_handler, name='register_handler'),
    url(r'^register_exist/$', views.register_exist),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_handler/$', views.login_handler, name='login_handler'),

]
