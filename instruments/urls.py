from django.urls import path
from .views import InstrumentListView, InstrumentDetailView

urlpatterns = [
    path('',InstrumentListView.as_view()),
    path('<int:pk>/',InstrumentDetailView.as_view()),
]
