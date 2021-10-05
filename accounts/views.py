from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.contrib.auth import get_user_model

from movies.models import Watchlist

# Create your views here.


class AccountsListView(LoginRequiredMixin, ListView):
    """
    Displaying accounts page with watchlist
    """
    model = Watchlist
    context_object_name = 'watchlist'
    template_name = 'accounts/accounts.html'

    def get_queryset(self):
        return Watchlist.objects.filter(
            user=self.request.user
        )


class EmailUpdateView(LoginRequiredMixin, UpdateView):
    """
    view used to change the user email adress
    """
    model = get_user_model()
    template_name = 'accounts/email_update.html'
    fields = ['email']
    success_url = reverse_lazy('accounts')
