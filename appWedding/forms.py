from django import forms
from .models import EntryForm

class EntryFormForm(forms.ModelForm):

    class Meta:
        model   = EntryForm
        fields  = [
                   "attendance",
                   "nameFamily",
                   "nameFirst",
                   "nameHFamily",
                   "nameHFirst",
                   "telNumber",
                   "email",
                   "postalCode",
                   "prefecture",
                   "building",
                   "city",
                   "streetAddress",
                   "allergy",
                   "bus"
                   ]