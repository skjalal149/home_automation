from django.urls import path
from .views import ButtonView, ProgressBarView, ColorStatusView

urlpatterns = (
    path("button/<uid>", ButtonView.as_view(), name="Button View"),
    path("progress", ProgressBarView.as_view(), name="Progress Bar View"),
    path("color", ColorStatusView.as_view(), name="Color Status View"),
)
