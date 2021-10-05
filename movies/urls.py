from django.urls import path

from .views import (
    MovieDetailView,
    MovieRatingJsonView,
    SearchResultsListView,
    watchlistAddMovie,
    watchlistUpdateMovie,
    MovieAdvancedSearchTemplateView,
    MovieAdvancedSearchResultsByDirector)

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
    path(
        'advanced/search/',
        MovieAdvancedSearchTemplateView.as_view(),
        name='advanced_search'
    ),
    path(
        'advanced/search/results',
        MovieAdvancedSearchResultsByDirector.as_view(),
        name="advanced_results"
    ),
    path('rating/<int:pk>', MovieRatingJsonView.as_view(), name='rating'),
    path('save/', watchlistAddMovie, name='save'),
    path('update/', watchlistUpdateMovie, name='update')
]
