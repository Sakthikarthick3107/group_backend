from django.urls import path
from .views import CollegeEventView , RegisterView

urlpatterns = [
    path('college-events/' , CollegeEventView.as_view() , name="College Events"),
    path('event-registration/' , RegisterView.as_view() , name="RegisterPage")
]
