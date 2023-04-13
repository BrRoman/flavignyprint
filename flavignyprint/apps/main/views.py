""" apps/main/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of main. """
    return render(
        request,
        'main/home.html',
        {},
    )


def form(request):
    """ Form view of main. """
    return render(
        request,
        'main/form.html',
        {},
    )
