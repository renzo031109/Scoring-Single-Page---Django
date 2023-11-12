from django.shortcuts import render
from .models import Score
from .forms import ScoreForm

def home(request):
    form = ScoreForm()
    title = 'Home'
    scores = Score.objects.all()
    return render(request,'score/home.html', {
        'scores': scores,
        'title': title,
        'form': form
    })
