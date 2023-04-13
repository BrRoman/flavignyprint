""" apps/main/forms.py """

from django import forms


class EstimateForm(forms.Form):
    """ Form for estimate. """
    email = forms.EmailField(
        label='Mon adresse électronique :',
    )
