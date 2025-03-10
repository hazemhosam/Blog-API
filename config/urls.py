"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework_simplejwt import views
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title= 'Todo API',
        default_version='v1',
        description='API documentation for Todo'
    ),
    public=True,
    authentication_classes=(JWTAuthentication,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('djoser.urls')),
    path('auth/token/', views.TokenObtainPairView.as_view(), name="jwt-create"),
    path('auth/token/refresh/', views.TokenRefreshView.as_view(), name="jwt-refresh"),
    path('auth/token/verify/', views.TokenVerifyView.as_view(), name="jwt-verify"),
    path('api/',include('post.urls')),
    path('api/swagger/',schema_view.with_ui('swagger',cache_timeout=0),
         name='schema-swagger-ui'),
]
