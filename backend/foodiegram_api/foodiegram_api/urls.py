from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), # new
    path('api-auth/', include('rest_framework.urls')),  # new
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')), # new
    path('api/v1/rest-auth/registration/', # new
          include('dj_rest_auth.registration.urls')),
]
