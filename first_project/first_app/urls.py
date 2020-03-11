from django.conf.urls import url
from first_app import views

# TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup_view, name='signup'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^formpage/', views.formpage_view, name='formpage'),
]
