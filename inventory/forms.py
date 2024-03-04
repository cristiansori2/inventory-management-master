from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    TYPE_CHOICES = [
        ('Cadenas', 'Cadenas'),
        ('Pulsos', 'Pulsos'),
        ('Anillos', 'Anillos'),
        ('Aretes', 'Aretes'),
        ('Piercing', 'Piercing'),
        ('Dijes', 'Dijes')
    ];
    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    

    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        #self.fields['quantity'].initial = 1  # Set initial value to 1
        self.fields['weight'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['kilate'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['type'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['picture'].widget.attrs.update({'class': 'form-control-file'})  # Example: Set class for styling file input
        self.fields['description'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})



    class Meta:
        model = Stock
        fields = ['name','type','weight','kilate','picture','description']