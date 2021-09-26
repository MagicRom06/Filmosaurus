from django.urls import path
from .views import SearchResultsListView

urlpatterns = [
    path(
        'search/', SearchResultsListView.as_view(),
        name='search_results'
    )
]
