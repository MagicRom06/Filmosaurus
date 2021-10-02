from django.urls import path

from .views import AccountsListView

urlpatterns = [
    path('', AccountsListView.as_view(), name="accounts"),
]
