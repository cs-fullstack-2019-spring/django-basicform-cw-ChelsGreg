from django.urls import path
from . import views


urlpatterns = [
    path("addFive/<int:accountID>", views.addFive, name="addFive"),
    path("printAccount/", views.printAccount, name="printAccount"),
    path("", views.index, name="index"),
]