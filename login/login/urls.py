
from django.contrib import admin
from django.conf.urls import url
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', auth_views.LoginView.as_view(template_name='login.html')),
]
