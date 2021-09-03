from django import forms
from .models import Expert


class ExpertForm(forms.ModelForm):

    class Meta:
        model = Expert
        fields = ('expertname','qualification','dob','doj','hospital','country','state','city')
        labels = {
            'expertname': 'ExpertName',
            'qualification': 'Qualification',
            'dob': "Date Of Birth",
            'doj': 'Date of Joining',
            'hospital': 'Hospital',
            'country': 'Country',
            'state': 'State',
            'city': 'City',

        }
    def __init__(self,*args,**kwargs):
        super(ExpertForm, self).__init__(*args,**kwargs)
        self.fields['qualification'].empty_label = 'Select'
        self.fields['city'].required = False
