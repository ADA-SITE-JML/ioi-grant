from django import forms
from . import models


class GraphsModelForm(forms.ModelForm):
    class Meta:
        model = models.Graphs
        exclude = []