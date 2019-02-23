"""csgradnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from event import views
from news import views
from alumnee import views

#for static root upload
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$',views.home,name='index'),


    #the error loading events view,was solved by assigning a view called
    #event in views of graduator app
    url(r'^events/$', views.eventview, name='event'),

    #event in views of graduator app
    url(r'^news/$', views.newsview, name='news'),

        #/alumnee/      (all graduators are listed)
    url(r'^alumnees/$' , views.alumnees, name='alumnees'),

    url(r'^register/$' , views.register_view, name='alumnees'),

    url(r'^login/$' , views.login_view, name='alumnees'),

    # /alumnees/001  (single detailed response of individual graduator)
    url(r'^alumnees/(?P<alumnee_id>[0-9]+)/$', views.alumnee_details, name='detail'),

    # /alumnees/001/portfolio  (single detailed response of individual graduator)
    url(r'^alumnees/(?P<alumnee_id>[0-9]+)/portfolio$', views.alumnee_portfolio, name='detail'),

    # /alumnees/001/documents  (single detailed response of individual graduator)
    url(r'^alumnees/(?P<alumnee_id>[0-9]+)/documents$', views.alumnee_documents, name='detail')
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
