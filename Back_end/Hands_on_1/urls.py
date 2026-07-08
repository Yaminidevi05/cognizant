from django.contrib import admin  # type: ignore[import]
from django.urls import path, include  # type: ignore[import]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
]