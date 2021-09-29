from django.urls import path

from .views import HomePageView, autocomplete

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('autocomplete/', autocomplete, name='autocomplete'),
]
