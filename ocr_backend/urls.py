from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="OCR Backend API",
      default_version='v1',
      description="This API allows us to perform testing on OCR API's",
      # terms_of_service="https://www.scvconsultants.com",
      contact=openapi.Contact(email="Mohammed.Rizwan@novigosolutions.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


userservice_patterns = ([
   path('users/', include('userservice.urls')),
], 'users')

urlpatterns = [
    path('accounts/login/', admin.site.urls),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    path('api/token/', include('tokenservice.urls')),
    path('api/', include(userservice_patterns, namespace="users")),
]
