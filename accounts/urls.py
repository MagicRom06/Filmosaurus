from django.urls import path

from .views import AccountsListView, EmailUpdateView

urlpatterns = [
    path('', AccountsListView.as_view(), name="accounts"),
    path('update/<int:pk>/', EmailUpdateView.as_view(), name="update"),
]
