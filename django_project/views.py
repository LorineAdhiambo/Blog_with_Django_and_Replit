from django.http import request
from django.shortcuts import render
import requests

def home(request):

    # USING APIS
    response = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random?language=en')
    data = response.json()
    results = data["text"] 

    response2 = requests.get('https://www.boredapi.com/api/activity')
    data2 = response2.json()
    results2 = data2["activity"]

    response3 = requests.get('https://dog.ceo/api/breeds/image/random')
    data3 = response3.json()
    results3 = data3["message"]
  
    if request.method == 'POST':
        photo = request.POST.get('photo')
    else:
        photo = None
   

    return render(request, 'templates/index.html', {
        'results': results,
        'results2': results2,
        'results3': results3,
        'photo': photo
    })


