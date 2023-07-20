"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include,re_path

from django.conf import settings  # new
from django.conf.urls.static import static  # new

from BPage.views import topic_view,question_view,answer_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin', admin.site.urls),
    path('', topic_view,name="topic_view"),
    path('topic/<int:pk>/', question_view, name='question_view'),
    path('topic/<int:pk>/<int:ck>/answer/', answer_view, name='answer_view'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:  # new

    urlpatterns = urlpatterns + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)