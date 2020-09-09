from web_admin.models import StateModel,CityModel,CuisineModel
from django import forms

class StateForms(forms.ModelForm):
    class Meta:
        model =StateModel
        fields = '__all__'
        widgets={"name":forms.TextInput(attrs={"placeholder":"State Name"})}


class CityForms(forms.ModelForm):
    class Meta:
        model =CityModel
        fields = '__all__'


class CuisineForms(forms.ModelForm):

    class Meta:
        model =CuisineModel
        fields = '__all__'