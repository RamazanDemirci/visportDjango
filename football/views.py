from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import TeamSerializer, StandingSerializer, SeasonSerializer
from .models import Standing, Team


# Create your views here.


class Seasons(APIView):
    def get(self, request, format=None):
        season_list = Season.objects.all()
        serializer = SeasonSerializer(season_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SeasonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StandingTable(APIView):

    def get(self, request, format=None):
        if 'playedGames' in request.data:
            standing_list = Standing.objects.filter(
                playedGames=request.data['playedGames'])
            serializer = StandingSerializer(standing_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # standing_list = Standing.objects.all()
        # serializer = StandingTableSerializer(standing_list, many=True)
        # return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StandingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StandingDetail(APIView):
    def get_object(self, id):
        try:
            return Standing.objects.filter(id=id)
        except expression as identifier:
            raise Http404

    def get(self, request, id, format=None):
        standing_list = Standing.objects.filter(
            playedGames=id)
        serializer = StandingSerializer(standing_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        pass

    def delete(self, request, id, format=None):
        standing_row = self.get_object(id)
        standing_row.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeamList(APIView):
    def get(self, request, format=None):
        team_list = Team.objects.all()
        serializer = TeamSerializer(team_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetail(APIView):
    def get(self, request, format=None):
        team = Team.objects.all()
        serializer = TeamSerializer(standing_list, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        pass

    def delete(self, request, format=None):
        pass


class Player(APIView):
    def get(self, request, format: None):
        pass

    def put(self, request, format: None):
        pass

    def delete(self, request, format: None):
        pass


class Matches(APIView):
    def get(self, request, format: None):
        pass

    def put(self, request, format: None):
        pass

    def delete(self, request, format: None):
        pass


class Events(APIView):
    def get(self, request, format: None):
        pass

    def put(self, request, format: None):
        pass

    def delete(self, request, format: None):
        pass
