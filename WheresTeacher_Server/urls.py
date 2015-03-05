from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from WheresTeacher_Server.quickstart import views
from snippets import views

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
