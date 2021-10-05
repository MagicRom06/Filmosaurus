from django.http.response import JsonResponse
from django.views.generic import TemplateView

from movies.models import Movie

# Create your views here.


class HomePageView(TemplateView):
    """
    displaying home page
    """
    template_name = 'home/home.html'


def autocomplete(request):
    """
    view used to displaying autocomplete suggestions
    when user type a movie in the home search bar
    """
    if 'term' in request.GET:
        qs = Movie.objects.filter(
            title__istartswith=request.GET.get('term')
        )[:5]
        titles = list()
        for movie in qs:
            titles.append(
                {
                    'id': movie.id,
                    'title': movie.title,
                    'pic': movie.picture,
                    'year': movie.year
                }
            )
        return JsonResponse(titles, safe=False)
