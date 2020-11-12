from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_jwt.views import obtain_jwt_token

schema_view = get_schema_view(
   openapi.Info(
      title="Foodigram API",
      default_version="v1",
      description="API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@admin.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), # new
    path('core/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),  # new
    path('token-auth/', obtain_jwt_token),
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')), # new
    path('api/v1/rest-auth/registration/', # new
          include('dj_rest_auth.registration.urls')),
    path('swagger/', schema_view.with_ui(  # new
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(  # new
        'redoc', cache_timeout=0), name='schema-redoc'),
]

