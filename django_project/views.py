from django.http import request
from django.shortcuts import render
import requests

def home(request):

    # USING APIS
    response = requests.get('https://api.github.com/events')
    data = response.json()
    results = data[0]["payload"] 

    response2 = requests.get('https://www.boredapi.com/api/activity')
    data2 = response2.json()
    results2 = data2["activity"]

    response3 = requests.get('https://dog.ceo/api/breeds/image/random')
    data3 = response3.json()
    results3 = data3["message"]

    return render(request, 'templates/index.html', {'results': results, 'results2': results2, 'results3': results3})