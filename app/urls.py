from django.urls import path
from .views import PortfolioView, TestimonialView


urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial')
]