from django.urls import path

from .views import (MovieDetailView, MovieRatingJsonView,
                    SearchResultsListView, watchlistAddMovie,
                    watchlistUpdateMovie)

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
    path('rating/<int:pk>', MovieRatingJsonView.as_view(), name='rating'),
    path('save/', watchlistAddMovie, name='save'),
    path('update/', watchlistUpdateMovie, name='update')
]
