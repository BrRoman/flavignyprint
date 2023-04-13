""" apps/main/views.py """

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import EstimateForm


def home(request):
    """ Home page of main. """
    return render(
        request,
        'main/home.html',
        {},
    )


def estimate(request):
    """ Estimate view of main. """
    if request.method == 'POST':
        form = EstimateForm(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data)
            return HttpResponseRedirect(reverse('main:home'))

    else:
        form = EstimateForm()

    return render(
        request,
        'main/form.html',
        {
            'form': form,
        },
    )


def send_mail(data):
    """ Send an email with the data of the estimate. """
    pass
