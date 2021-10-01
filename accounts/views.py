from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from movies.models import Watchlist


# Create your views here.

class AccountsListView(LoginRequiredMixin, ListView):
    model = Watchlist
    context_object_name = 'watchlist'
    template_name = 'accounts/accounts.html'

    def get_queryset(self):
        return Watchlist.objects.filter(
            user=self.request.user
        )
