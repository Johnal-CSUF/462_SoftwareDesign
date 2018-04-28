"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import view
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^test$', view.hello, name='hello'),#path('admin/', admin.site.urls),
    url(r'^items$', view.items, name='items'),
    url(r'^bugs$', view.bugs, name='bugs'),
    url(r'^addBug$', view.addBug, name='addBug'),
    url(r'^deleteBug$', view.deleteBug, name='deleteBug'),
    url(r'^customer$', view.customer, name='customer'),
    url(r'^addCustomer$', view.addCustomer, name='addCustomer'),
    url(r'^deleteCustomer$', view.deleteCustomer, name='deleteCustomer'),
    url(r'^addItem$', view.addItem, name='addItem'),
    url(r'^deleteItem$', view.deleteItem, name='deleteItem'),
	url(r'^search$', view.search, name='search'),
    url(r'^addTransaction$', view.addTransaction, name='addTransaction'),
    url(r'^deleteTransaction$', view.deleteTransaction, name='deleteTransaction'),
    url(r'^transaction$', view.transaction, name='transaction'),
    url(r'^$', view.home, name='home'),
    #url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    #url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    #url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', view.login_view, name='login'),
	url(r'^homepage$', view.homepage, name='homepage'),
	url(r'^login/$', view.register, name='register'),
    url(r'^logout/$', view.logout_view, name='logout'),
    url(r'^admin/', admin.site.urls),
	
]
