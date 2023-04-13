""" apps/main/forms.py """

from django import forms


class EstimateForm(forms.Form):
    """ Form for estimate. """
    name = forms.CharField(
        label='Nom :',
        max_length=255,
        error_messages={
            'required': 'Ce champ est obligatoire.',
        },
    )
