from django.conf.urls import url
from django.urls import include
from rest_framework import routers

import application.api.configuration.config as config

router = routers.DefaultRouter()
router.register(r'configs', config.ViewSet)

api_urls = [
    url(r'api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
]
