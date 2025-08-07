from django import forms

class CocktailSearchForm(forms.Form):
    query=forms.CharField(label='Search for a cocktail or indegrient',max_length=100)
