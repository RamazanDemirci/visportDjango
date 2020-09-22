# from django.db import models

from djongo import models
from django import forms
# from .models import File

# Create your models here.

isMigrate = False


class League(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    alias = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=200, blank=True)
    country_code = models.CharField(max_length=5, blank=True)


class Season(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    alias = models.CharField(max_length=50, blank=True)
    year = models.IntegerField()
    league = models.CharField(max_length=50)


class Person(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    alias = models.CharField(max_length=25, blank=True)
    title = models.CharField(max_length=100, blank=True)
    team = models.CharField(max_length=50, blank=True)


class Team(models.Model):
    name = models.CharField(max_length=150, blank=True, primary_key=True)
    alias = models.CharField(max_length=50, blank=True)
    logo = models.CharField(max_length=150, blank=True)
    season = models.CharField(max_length=50, blank=True)
    league = models.CharField(max_length=50, blank=True)


class Standing_Detail(models.Model):
    position = models.IntegerField(blank=True, primary_key=True)
    team = models.CharField(max_length=150, blank=True)
    playedGames = models.IntegerField(blank=True)
    won = models.IntegerField(blank=True)
    draw = models.IntegerField(blank=True)
    lost = models.IntegerField(blank=True)
    points = models.IntegerField(blank=True)
    goalsFor = models.IntegerField(blank=True)
    goalsAgainst = models.IntegerField(blank=True)
    goalDifference = models.IntegerField(blank=True)

    class Meta:
        abstract = isMigrate


class Standing(models.Model):
    league = models.CharField(max_length=50, blank=True)
    season = models.CharField(max_length=50, blank=True)
    week = models.IntegerField(blank=True)
    detail = models.ArrayField(
        model_container=Standing_Detail, null=True
    )


class Pos(models.Model):
    px = models.FloatField(blank=True, primary_key=True)
    py = models.FloatField(blank=True, null=True)

    class Meta:
        abstract = isMigrate


class Change(models.Model):
    player = models.CharField(max_length=200, blank=True, primary_key=True)
    minutes = models.CharField(max_length=20, blank=True, null=True)
    reason = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = isMigrate


class Goal(models.Model):
    player = models.CharField(max_length=200, blank=True, primary_key=True)
    minutes = models.CharField(max_length=20, blank=True, null=True)
    goal_type = models.CharField(max_length=50, blank=True, null=True)
    goal_type_detail = models.CharField(max_length=50, blank=True, null=True)
    assist = models.CharField(max_length=200, blank=True, null=True)
    assist_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = isMigrate


class Card(models.Model):
    player = models.CharField(max_length=200, blank=True, primary_key=True)
    minutes = models.CharField(max_length=20, blank=True, null=True)
    card_type = models.CharField(max_length=50, blank=True, null=True)
    reason = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = isMigrate


class Player(models.Model):
    name = models.CharField(max_length=200, blank=True, primary_key=True)
    forma_no = models.IntegerField(blank=True, null=True)
    pos = models.EmbeddedField(model_container=Pos, null=True)

    class Meta:
        abstract = isMigrate


class MissedPenalties(models.Model):
    minutes = models.CharField(max_length=20, blank=True, primary_key=True)
    scorer = models.CharField(max_length=200, blank=True, null=True)
    reason = models.CharField(max_length=50, blank=True, null=True)
    keeper = models.CharField(max_length=200, blank=True, null=True)
    keeper_role = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = isMigrate


class Host(models.Model):
    name = models.CharField(max_length=150, blank=True, primary_key=True)
    score = models.CharField(max_length=10, blank=True, null=True)
    coach = models.CharField(max_length=200, blank=True, null=True)
    logo = models.CharField(max_length=150, blank=True, null=True)
    line_up = models.CharField(max_length=100, blank=True, null=True)
    goals = models.ArrayField(model_container=Goal, null=True)
    cards = models.ArrayField(model_container=Card, null=True)
    changes_in = models.ArrayField(model_container=Change, null=True)
    changes_out = models.ArrayField(model_container=Change, null=True)
    players = models.ArrayField(model_container=Player, null=True)

    class Meta:
        abstract = isMigrate


class Match(models.Model):
    league = models.CharField(max_length=50, blank=True)
    season = models.CharField(max_length=50, blank=True)
    week = models.CharField(max_length=50, blank=True)
    stadium = models.CharField(max_length=200, blank=True)
    match_date = models.CharField(max_length=40, blank=True)
    match_time = models.CharField(max_length=10, blank=True)
    referee = models.CharField(max_length=200, blank=True)
    referee_assist_1st = models.CharField(max_length=200, blank=True)
    referee_assist_2nd = models.CharField(max_length=200, blank=True)
    host = models.EmbeddedField(model_container=Host)
    guest = models.EmbeddedField(model_container=Host)
    missed_penalties = models.ArrayField(
        model_container=MissedPenalties, null=True)
