from django.urls import path, include  # type: ignore[reportMissingImports]
from rest_framework.routers import DefaultRouter  # type: ignore[reportMissingImports]

from .views import (
    CourseViewSet,
    StudentViewSet,
    EnrollmentViewSet,
)

router = DefaultRouter()

router.register(
    'courses',
    CourseViewSet
)

router.register(
    'students',
    StudentViewSet
)

router.register(
    'enrollments',
    EnrollmentViewSet
)

urlpatterns = [

    path('', include(router.urls)),

]