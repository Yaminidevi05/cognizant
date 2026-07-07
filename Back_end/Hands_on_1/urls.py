from django.urls import path  # type: ignore[import]

from .views import hello_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),
]