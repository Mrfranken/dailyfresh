from django.conf.urls import url
from . import views


app_name = 'df_user'
urlpatterns = [
    url(r'^register/$', views.register, name='register')
]