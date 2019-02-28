from django.conf.urls import re_path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from . import views


router = DefaultRouter()
router.register('house', views.HouseViewSet)

urlpatterns = [
    re_path(r'', include(router.urls)),
    re_path(r'^docs/', include_docs_urls(title='House API')),
]
