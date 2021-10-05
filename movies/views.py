from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, TemplateView

from .models import Movie, Person, Watchlist
from .utils import Rating

# Create your views here.


class SearchResultsListView(ListView):
    paginate_by = 12
    model = Movie
    context_object_name = 'movie_list'
    template_name = 'movies/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Movie.objects.filter(
            Q(title__icontains=query)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        saved_movies = Watchlist.objects.filter(
            user_id=self.request.user.id,
        )
        for movie in saved_movies:
            if movie.movie_id == self.get_object().id and \
               movie.seen is True:
                context['viewed'] = False
            elif movie.movie_id == self.get_object().id and \
                    movie.seen is False:
                context['viewed'] = True
        return context


class MovieRatingJsonView(DetailView):
    model = Movie

    def get_object(self, **kwargs):
        obj = Movie.objects.get(id=self.kwargs['pk'])
        return obj

    def get(self, request, pk):
        movie = self.get_object()
        rating = Rating(movie.title, str(movie.year)).get()
        return JsonResponse(rating)


class MovieAdvancedSearchTemplateView(TemplateView):
    template_name = 'movies/advanced_search.html'


class MovieAdvancedSearchResultsByDirector(ListView):
    model = Movie

    def get(self, request):
        results = list()
        if self.request.GET.get('by_director'):
            search = self.request.GET.get('by_director')
            directors = Person.objects.filter(name__contains=search.title())
            for director in directors:
                if Movie.objects.filter(directors=director.id).exists():
                    results.append(
                        {
                            "director": director.name,
                            "movies": list(
                                Movie.objects.filter(
                                    directors=director.id
                                ).values_list(
                                    'id', 'title', 'year', 'picture'
                                )
                            )
                        }
                    )
        elif self.request.GET.get('by_casting'):
            search = self.request.GET.get('by_casting')
            actors = Person.objects.filter(name__contains=search.title())
            for actor in actors:
                if Movie.objects.filter(casts=actor.id).exists():
                    results.append(
                        {
                            "actor": actor.name,
                            "movies": list(
                                Movie.objects.filter(
                                    casts=actor.id
                                ).values_list('id', 'title', 'year', 'picture')
                            )
                        }
                    )
        return JsonResponse(results, safe=False)


@login_required(login_url='account_login')
def watchlistAddMovie(request):
    user = request.user
    user_movie = Movie.objects.get(id=request.GET.get('movie'))
    if Watchlist.objects.filter(
        user_id=user.id,
        movie_id=user_movie.id,
        seen=False
    ).exists():
        return redirect(f'/movies/get/{user_movie.id}')
    else:
        query = Watchlist.objects.create(
            user=user,
            movie=user_movie,
            saved_date=datetime.now()
        )
        query.save()
        return redirect(f'/movies/get/{user_movie.id}')


@login_required(login_url='account_login')
def watchlistUpdateMovie(request):
    movie = Watchlist.objects.get(id=request.GET.get('id'))
    movie.seen = True
    movie.viewed_date = datetime.now()
    movie.save()
    return redirect('accounts')
