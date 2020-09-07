from web_admin.models import StateModel,CityModel,CuisineModel
from django import forms

class StateForms(forms.ModelForm):
    class Meta:
        model =StateModel
        fields = '__all__'

class CityForms(forms.ModelForm):
    class Meta:
        model =CityModel
        fields = '__all__'

class CuisineForms(forms.ModelForm):
    # cusine_type=(('select','SELECT'),('bakery','BAKERY'),
    #              ('beverages','BEVERAGES'),
    #              ('resturants','RESTURANTS'))
    # type=forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=cusine_type))

    class Meta:
        model =CuisineModel
        fields = '__all__'