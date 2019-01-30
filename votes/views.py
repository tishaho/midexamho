from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Candidate
from .models import Position
from .models import Vote
from .forms import CandidateForm
from .forms import PositionForm
from django.utils import timezone

# Create your views here.
def index(request):
    context = {}
    candidates = Candidate.objects.all()
    context['candidates'] = candidates
    return render(request, 'index.html', context)


def candidate_detail(request, candidate_id):
    context = {}
    context['candidate'] = Candidate.objects.get(id=candidate_id)
    return render(request, 'candidate_detail.html', context)


def candidate_create(request):
    context = {}
    form = CandidateForm()

    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')

    return render(request, 'candidate_create.html', {'form': form})


def candidate_update(request, candidate_id):
    context = {}
    candidates = Candidate.objects.get(id=candidate_id)
    candidate_id = Candidate.objects.get(id=candidate_id)

    if request.method == 'POST':
        form = CandidateForm(request.POST, instance=candidates)
        if form.is_valid():
            form.save()
            return HttpResponse('Candidate updated')
        else:
            context['form'] = form
            return render(request, 'candidate_update.html', context)
    else:
        context['form'] = CandidateForm(instance=candidates)
        return render(request, 'candidate_update.html', context)


def position_create(request):
    context = {}
    form = PositionForm()

    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')

    return render(request, 'position_create.html', {'form': form})

def vote(request, candidate_id):
    context = {}
    candidate  = Candidate.objects.get(id=candidate_id)
    candidate.candidates.all().count()
    return redirect('votes:index')

    return render(request, 'index.html', context)
