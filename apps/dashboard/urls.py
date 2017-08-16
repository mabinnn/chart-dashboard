from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.covetfahion_index),
    url(r'^covetdashboard_1$', views.cf_dash1),
    url(r'^covetdashboard_2$', views.cf_dash2),
    url(r'^designhome$', views.designhome_index),
    url(r'^designdashboard_1$', views.design_dash1),
    url(r'^designdashboard_2$', views.design_dash2)
]
