from rest_framework import viewsets  # type: ignore[reportMissingImports]
try:
    from rest_framework.decorators import action  # type: ignore[reportMissingImports]
except Exception:
    # Fallback noop decorator for environments where DRF isn't available
    def action(*args, **kwargs):
        def _decorator(func):
            return func
        return _decorator
from rest_framework.response import Response  # type: ignore[reportMissingImports]

from .models import Course, Student, Enrollment
from .serializers import (
    CourseSerializer,
    StudentSerializer,
    EnrollmentSerializer,
)


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])

    def students(self, request, pk=None):

        course = self.get_object()

        students = Student.objects.filter(
            enrollments__course=course
        )

        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()

    serializer_class = StudentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):

    queryset = Enrollment.objects.all()

    serializer_class = EnrollmentSerializer