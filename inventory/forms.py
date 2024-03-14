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
    def clean_sku(self):
        sku = self.cleaned_data['sku']
        # Adjust the query to exclude the current instance from the uniqueness check
        if self.instance and self.instance.pk:
            if Stock.objects.filter(sku=sku).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("This SKU already exists.")
        else:
            if Stock.objects.filter(sku=sku).exists():
                raise forms.ValidationError("This SKU already exists.")
        return sku

    

    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].required = False
        self.fields['sku'].required = False
        self.fields['sku'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})

        self.fields['fechaApartado'].required = False
        # self.fields['fechaApartado'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['date'].required = False
        self.fields['precioApartado'].required = False
        self.fields['precioApartado'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})    
        self.fields['apartadoPor'].required = False    
        self.fields['apartadoPor'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['weight'].required = False
        self.fields['weight'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['kilate'].required = False
        self.fields['kilate'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['price'].required = False
        self.fields['price'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['type'].required = False
        self.fields['type'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['picture'].widget.attrs.update({'class': 'form-control-file'})  # Example: Set class for styling file input
        self.fields['description'].required = False
        self.fields['description'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['telefono'].required = False
        self.fields['telefono'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'},required = False,null = True)
        self.fields['is_deleted'].initial = False 


   

    class Meta:
        model = Stock
        fields = ['name','type','weight','kilate','picture','description','quantity','is_deleted','date','precioApartado','apartadoPor','telefono','sku','price','fechaApartado']