from django.shortcuts import render
from .models import Score
from .forms import ScoreForm

def home(request):
    title = 'Home'
    scores = Score.objects.all()
    form = ScoreForm()
    if request.method == 'POST':
        if 'save' in request.POST:
            form = ScoreForm(request.POST)
            form.save()
        
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            score = Score.objects.get(id=pk)
            score.delete()

    return render(request,'score/home.html', {
        'scores': scores,
        'title': title,
        'form': form
    })


