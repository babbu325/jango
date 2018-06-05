from django.http import HttpResponse
from .models import Team


def index(request):
    all_teams = Team.objects.all()
    html = ''
    for team in all_teams:
        url = '/cricket/' + str(team.id) + '/'
        html += '<a href = "' + url + '">' + team.Team_name + '</a> <br>'
    return HttpResponse(html)


def detail(request, team_id):
    return HttpResponse("<h1>Details fro the team id: " + str(team_id) + " </h1>")
