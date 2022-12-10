"""psuapp URL Configuration

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
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from rest_framework import routers
#импорты каталогов

from psu.views import HomePage, Search, FaqPage, CategorySearch, ProblemViewSet, FaqViewSet, ApplicationViewSet, UserViewSet
from contact.views import ContactViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'problem', ProblemViewSet)
router.register(r'faq', FaqViewSet)
router.register(r'contact',ContactViewSet)
router.register(r'application',ApplicationViewSet)
router.register(r'user',UserViewSet)
#router.register(r'admin', admin.site.urls)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'),name="login"),
    path('api/', include(router.urls)),
    path('',HomePage.as_view(), name = "main_page"),
    path('search/',Search.as_view(),name = "search"),
    path('category_search/',CategorySearch.as_view(), name = "category_search"),
    path('pr_category/<int:pr_id>/',FaqPage.as_view(),name="problem_detail"),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

