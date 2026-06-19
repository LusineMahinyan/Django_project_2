from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import (
    UserViewSet,
    RegisterView,
    PaymentViewSet,
)
from materials.views import (
    CourseViewSet,
    LessonViewSet,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"payments", PaymentViewSet)
router.register(r"courses", CourseViewSet)
router.register(r"lessons", LessonViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),

    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Регистрация
    path("api/register/", RegisterView.as_view(), name="register"),

    # API
    path("api/", include(router.urls)),
    
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
