from pathlib import Path
import os
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.shortcuts import render

from django.http.response import Http404, JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Match, Person, League, Season, Team, Standing
from .serializers import MatchSerializer, PersonSerializer, LeagueSerializer, SeasonSerializer, TeamSerializer, FixtureSerializer, StandingSerializer
from rest_framework.decorators import api_view

from django.core.files.storage import FileSystemStorage

from django.shortcuts import get_object_or_404


def get_obj_or_404(klass, *args, **kwargs):
    try:
        return klass.objects.get(*args, **kwargs)
    except klass.DoesNotExist:
        raise Http404

@api_view(['GET', 'POST'])
def league_list(request):
    if request.method == 'GET':
        items = League.objects.all()
        serializer = LeagueSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = LeagueSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def league_detail(request, pk):
    item = get_obj_or_404(League, name=pk)
    if request.method == 'GET':
        serializer = LeagueSerializer(instance=item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = LeagueSerializer(instance=item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        item.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def seasons(request):
    if request.method == 'GET':
        print('GET')
        league = request.query_params.get('league')
        seasons = Season.objects.all().filter(league=league)
        print(seasons)
        season_serializer = SeasonSerializer(seasons, many=True)
        if season_serializer.data != None:
            response = season_serializer.data
            return JsonResponse(response, status=status.HTTP_200_OK, safe=False)

        return JsonResponse({"status": "Resource not Found"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        print("POST")
        season_data = JSONParser().parse(request)
        season_serializer = SeasonSerializer(data=season_data)
        if season_serializer.is_valid():
            season_serializer.save()
            return JsonResponse(season_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(season_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def teams(request):
    if request.method == 'GET':
        name = request.data['name']
        name = name.lower().strip()
        inner_query = Team.objects.filter(
            name__contains=name).values('name', 'alias', 'logo', 'season', 'league')
        data = inner_query.first()
        if(data != None):
            return JsonResponse(data, status=status.HTTP_200_OK)
        return JsonResponse({"status": "Resource not Found"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        print("POST")
        team_data = JSONParser().parse(request)
        team_serializer = TeamSerializer(data=team_data)
        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse(team_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        print("PUT")
        team_data = JSONParser().parse(request)
        name = team_data["name"]
        alias = team_data["alias"]
        logo = team_data["logo"]
        season = team_data["season"]
        league = team_data["league"]

        inner_query = Team.objects.filter(
            name__contains=name).values('name')

        data = inner_query.first()
        if data != None:
            team_serializer = TeamSerializer(data=team_data)
            if team_serializer.is_valid():
                team_serializer.save()
                return JsonResponse(team_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def persons(request):
    if request.method == 'GET':
        # inner_query = Player.objects.filter(name__contains='Ch').values('name')
        # entries = Entry.objects.filter(blog__name__in=inner_query)
        name = request.data['name']
        # inner_query = Person.objects.filter(name=name).configure(
        #    cursor_type=CursorType.TAILABLE).iterator()

        # data = Person.find_one({'name': 'Fernando Andrade Dos Santos'})

        inner_query = Person.objects.filter(
            name__contains=name).values('name', 'alias')

        data = inner_query.first()
        if(data != None):
            return JsonResponse(data, status=status.HTTP_200_OK)
        return JsonResponse({"status": "Resource not Found"}, status=status.HTTP_400_BAD_REQUEST)
        # entries = Person.objects.filter(name__in=inner_query)
    elif request.method == 'POST':
        print("POST")
        person_data = JSONParser().parse(request)
        person_serializer = PersonSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def logos(request):
    if request.method == 'GET':
        filename = request.data['filename']

        data = None
        dirname = os.path.dirname(__file__)
        parent_directory = os.path.split(dirname)[0]
        filepath = os.path.join(parent_directory, 'media', f'{filename}.png')

        # filepath = Path(f"../media/{filename}.png")

        # filepath = f'D:/Google Drive/Tutorials/Python/RestApi/DjangoApi/visport{settings.MEDIA_URL}{filename}.png'
        with open(filepath, 'rb') as f:
            data = f.read()
        if data is not None:
            return HttpResponse(data, content_type='image/png')
        else:
            return JsonResponse({"err": "File download is failure"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        filename = request.data['filename']
        filename = f'{filename}.png'
        logo = request.FILES['logo']
        fs = FileSystemStorage()
        if fs.exists(filename) is not True:
            filenames = fs.save(filename, logo)
            uploaded_file_url = fs.url(filenames)
            print(uploaded_file_url)
            return JsonResponse({"filename": uploaded_file_url}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"info": "File already exist"}, status=status.HTTP_201_CREATED)
    return JsonResponse({"err": "File upload is failure"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def match_exist(request):
    if request.method == 'GET':
        # inner_query = Player.objects.filter(name__contains='Ch').values('name')
        # entries = Entry.objects.filter(blog__name__in=inner_query)

        stadium = request.data['stadium']
        match_date = request.data['match_date']
        match_time = request.data['match_time']
        # inner_query = Person.objects.filter(name=name).configure(
        #    cursor_type=CursorType.TAILABLE).iterator()

        # data = Person.find_one({'name': 'Fernando Andrade Dos Santos'})

        inner_query = Match.objects.filter(stadium__contains=stadium).filter(
            match_date__contains=match_date).filter(match_time__contains=match_time).values('referee')

        data = inner_query.first()
        if(data == None):
            return JsonResponse({"status": "not found"}, status=status.HTTP_200_OK)
        if(data != None):
            return JsonResponse(data, status=status.HTTP_200_OK)
        return JsonResponse({"status": "Resource not Found"}, status=status.HTTP_400_BAD_REQUEST)
        # entries = Person.objects.filter(name__in=inner_query)


@api_view(['GET'])
def matchByHost(request):
    if request.method == 'GET':
        print("GET3")
        league = request.query_params.get('league')
        season = request.query_params.get('season')
        week = request.query_params.get('week')
        host = request.query_params.get('host')

        matches = Match.objects.all().filter(
            league=league).filter(season=season).filter(week=week)
        match_data = None
        for i in range(len(matches)):
            if(matches[i].host['name'] == host):
                match_data = matches[i]
                break
        matches_serializer = MatchSerializer(match_data, many=False)
        response = matches_serializer.data
        return JsonResponse(response, safe=False)


@ api_view(['GET', 'POST', 'DELETE'])
def matches(request):
    if request.method == 'GET':
        league = request.query_params.get('league')
        season = request.query_params.get('season')
        week = request.query_params.get('week')

        matches = Match.objects.all().filter(league=league).filter(
            season=season).filter(week=week).filter(week=host).filter(week=guest)

        matches_serializer = MatchSerializer(matches, many=True)

        response = matches_serializer.data
        return JsonResponse(response, safe=False)

    elif request.method == 'POST':
        print("POST")
        match_data = JSONParser().parse(request)
        matches_serializer = MatchSerializer(data=match_data)
        if matches_serializer.is_valid():
            matches_serializer.save()
            return JsonResponse(matches_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(matches_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getLeagueAliasByName(m_name):
    league_item = League.objects.all().filter(name=m_name).first()
    league_serializer = LeagueSerializer(league_item, many=False)
    if league_serializer.data != None:
        return league_serializer.data['alias']
    else: return None

@api_view(['GET', 'POST'])
def image_view(request,  school_id, size):
    if request.method == 'GET':
        image = School.objects.get(school__pk=school_id).image
        resized_img = image #Handle resizing here

        return HttpResponse(resized_img, content_type="image/png")
    return JsonResponse(fixture_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@ api_view(['GET'])
def fixture(request):
    if request.method == 'GET':
        league = request.query_params.get('league')
        season = request.query_params.get('season')
        week = request.query_params.get('week')

        

        #league_alias = getLeagueAliasByName(league);
        league_alias = league
        if league_alias != None:
            matches = Match.objects.all().filter(league=league_alias).filter(season=season).filter(week=week)
            print(matches)
            fixture_serializer = FixtureSerializer(matches, many=True)
            if fixture_serializer.data != None:
                response = {
                    'league': league_alias,
                    'season': season,
                    'week': week,
                    'matches': fixture_serializer.data
                }
                return JsonResponse(response, safe=False)
        return JsonResponse(fixture_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET', 'POST', 'DELETE'])
def standing_all(request):
    if request.method == 'GET':
        league = request.data['league']
        season = request.data['season']

        standing = Standing.objects.all().filter(
            league__contains=league).filter(season__contains=season)

        standing_serializer = StandingSerializer(standing, many=True)
        if standing_serializer.data != None:
            response = standing_serializer.data
            return JsonResponse(response, safe=False)
        return JsonResponse(standing_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET', 'POST', 'DELETE'])
def standing(request):
    if request.method == 'GET':
        # league = request.data['league']
        # season = request.data['season']
        # week = request.data['week']

        league = request.query_params.get('league')
        season = request.query_params.get('season')
        week = request.query_params.get('week')

        standing = Standing.objects.all().filter(
            league=league).filter(season=season).filter(week=week)

        standing_serializer = StandingSerializer(standing, many=True)
        if standing_serializer.data != None:
            response = standing_serializer.data
            return JsonResponse(response, safe=False)
        return JsonResponse(standing_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        standing = JSONParser().parse(request)
        standing_serializer = StandingSerializer(data=standing)
        if standing_serializer.is_valid():
            inner_query = Standing.objects.filter(
                league=standing['league']).filter(season=standing['season']).filter(week=standing['week']).values('season')
            record = inner_query.first()
            if record == None:
                standing_serializer.save()
                return JsonResponse(standing_serializer.validated_data, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'status': 'record already exist'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(standing_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
