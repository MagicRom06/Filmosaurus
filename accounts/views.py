from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class AccountsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/accounts.html'
