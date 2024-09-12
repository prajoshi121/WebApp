import random
from django.shortcuts import render
from datetime import datetime

def home(request):

    present = datetime.now()

    Quotes = [

        "A room without books is like a body without a soul.",
        "Be the change that you wish to see in the world.",
        "If you tell the truth, you don't have to remember anything.",
        "A person who never made a mistake never tried anything new."
    ]

    Random_Quote = random.choice(Quotes)


    Information = {
        'current_datetime' : present,
        'Random_Quote' : Random_Quote
    }
    return render(request, "webapp/index.html", Information)
