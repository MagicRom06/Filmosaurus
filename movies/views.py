from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from .models import Movie, Watchlist
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


class MovieRatingJsonView(DetailView):
    model = Movie

    def get_object(self, **kwargs):
        obj = Movie.objects.get(id=self.kwargs['pk'])
        return obj

    def get(self, request, pk):
        movie = self.get_object()
        rating = Rating(movie.title, str(movie.year)).get()
        return JsonResponse(rating)


@login_required(login_url='account_login')
def watchlistAddMovie(request):
    user = request.user
    user_movie = Movie.objects.get(id=request.GET.get('movie'))
    if Watchlist.objects.filter(
        user_id=user.id,
        movie_id=user_movie.id
    ).exists():
        return redirect(f'/movies/get/{user_movie.id}?alreadyexists=true')
    else:
        query = Watchlist.objects.create(
            user=user,
            movie=user_movie
        )
        query.save()
        return redirect(f'/movies/get/{user_movie.id}?add=true')


@login_required(login_url='account_login')
def watchlistUpdateMovie(request):
    movie = Watchlist.objects.get(id=request.GET.get('id'))
    movie.seen = True
    movie.save()
    return redirect('accounts')
