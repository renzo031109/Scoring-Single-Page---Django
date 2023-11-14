from django.shortcuts import render
from .models import Score
from .forms import ScoreForm

def home(request):
    form = ScoreForm()
    scores = Score.objects.all()
    title = 'Home'
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = ScoreForm(request.POST)
            else:
                score = Score.objects.get(id=pk)
                form = ScoreForm(request.POST, instance=score)
            form.save()
            form = ScoreForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            score = Score.objects.get(id=pk)
            score.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            score = Score.objects.get(id=pk)
            form = ScoreForm(instance=score)
    return render(request, 'score/home.html', {
        'form': form,
        'title': title,
        'scores': scores
    })