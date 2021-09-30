from django.urls import path
from .views import AccountsTemplateView

urlpatterns = [
    path('', AccountsTemplateView.as_view(), name="accounts"),
]
