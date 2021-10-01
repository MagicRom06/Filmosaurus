from django.urls import path

from .views import \
    SearchResultsListView, \
    MovieDetailView, \
    watchlistAddMovie, \
    watchlistUpdateMovie

urlpatterns = [
    path(
        'search/', SearchResultsListView.as_view(),
        name='search_results'
    ),
    path(
        'get/<int:pk>',
        MovieDetailView.as_view(),
        name='movie_detail'
    ),
    path('save/', watchlistAddMovie, name='save'),
    path('update/', watchlistUpdateMovie, name='update')
]
