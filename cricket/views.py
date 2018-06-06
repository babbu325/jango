from django.http import Http404
from django.shortcuts import render
from .models import Team


def index(request):
    all_teams = Team.objects.all()
    contaxt = {'all_teams': all_teams}
    return render(request, 'cricket/index.html', contaxt)


def detail(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        raise Http404("No team with this id...")
    return render(request, 'cricket/detail.html', {'team_id': team})
