from django.urls import path
from .views import RegisterView, TodoListCreateView, TodoDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ListAPI",
        default_version='v1',
        description="API documentation for ListAPI",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@listapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('todos/', TodoListCreateView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
