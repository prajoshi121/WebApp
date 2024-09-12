import random
from django.shortcuts import render
from datetime import datetime

def home(request):

    if request.method == 'POST':
        name = request.POST['name']
    else:
        name = 'guest'

    present = datetime.now()

    quotes = [

        "A room without books is like a body without a soul.",
        "Be the change that you wish to see in the world.",
        "If you tell the truth, you don't have to remember anything.",
        "A person who never made a mistake never tried anything new."
    ]

    random_quote = random.choice(quotes)

    information = {
        'current_datetime' : present,
        'Random_Quote' : random_quote,
        'name' : name
    }
    return render(request, "webapp/index.html", information)

