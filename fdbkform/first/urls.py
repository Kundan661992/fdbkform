

# from django.conf.urls import url

from . import views
from django.urls import path

app_name = 'first'
urlpatterns = [
    path('', views.feedback_form, name='home'),
    # url('', views.feedback_form, name='home'),
]