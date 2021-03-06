"""mysite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from firstapp import views as firstapp_views  
from django.views.generic.base import TemplateView

news_urlpatterns = [
	url(r'^news1/([0-9]{4})/$', firstapp_views.news1)
]

print_urlpatterns = [
    url(r'^templatedef/$', firstapp_views.templatedef),
    url(r'^printerdef/$', firstapp_views.printerdef),
    url(r'^templatelist/$', firstapp_views.templatelist),
    url(r'^printerlist/$', firstapp_views.printerlist)
]

autocomplete_urlpatterns = [
    url(r'^customlist/$', firstapp_views.customlist)
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', firstapp_views.login),
    url(r'^print/', include(print_urlpatterns)),
    url(r'^autocomplete/', include(autocomplete_urlpatterns)),
    # url(r'^$', firstapp_views.index),
    # url(r'^news/', include(news_urlpatterns)),
    url(r'^$',TemplateView.as_view(template_name="index.html"))
]
