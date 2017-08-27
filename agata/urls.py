"""agata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from postsubjectivity import views

urlpatterns = [
	url(r'^$', views.index, name='root'),
	url(r'^sabrina/$', views.enter, name="enter"),
	url(r'^sabrina/home/$', views.home, name='home'),
	url(r'^sabrina/(?P<alias_id>[0-9]+)/home', views.contribute, name="contribute"),
	url(r'^sabrina/(?P<alias_id>[0-9]+)/latidos', views.latidos, name="latidos"),
	url(r'^sabrina/(?P<alias_id>[0-9]+)/oficial', views.oficial, name="oficial"),
	url(r'^sabrina/(?P<alias_id>[0-9]+)/incarnacions', views.incarnations, name="incarnations"),
    url(r'^admin/', admin.site.urls),
]
