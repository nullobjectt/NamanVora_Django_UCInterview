# cocktails/views.py
import requests
from django.shortcuts import render
from .forms import CocktailSearchForm

def search_cocktails(request):
    form = CocktailSearchForm(request.GET or None)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            results = data.get('drinks', [])

    return render(request, 'cocktails/search.html', {'form': form, 'results': results})
