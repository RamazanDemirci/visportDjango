from django.db import models

# Create your models here.


class NationalLeague(models.Model):
    title = models.CharField(max_length=60)
    desc = models.CharField(max_length=400, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    title = models.CharField(max_length=60)
    alias = models.CharField(max_length=120, blank=True)
    full_name = models.CharField(max_length=60, blank=True)
    desc = models.CharField(max_length=400, blank=True)
    logo = models.CharField(max_length=120, blank=True)
    motto = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Season(models.Model):
    title = models.CharField(max_length=60)
    desc = models.CharField(max_length=400, blank=True)
    logo = models.CharField(max_length=120, blank=True)
    motto = models.CharField(max_length=120, blank=True)
    alias = models.CharField(max_length=120, blank=True)
    startDate = models.DateTimeField(auto_now_add=False)
    endDate = models.DateTimeField(auto_now_add=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class Match(models.Model):
#    host = models.CharField(max_length=60)
#    guest = models.CharField(max_length=60)
#    desc = models.CharField(max_length=400, blank=True)
#    referee = models.CharField(max_length=60, blank=True)
#    date = models.DateTimeField(auto_now_add=False)
#    startTime = models.TimeField(auto_now=False, auto_now_add=False)
#    created_at = models.DateTimeField(auto_now_add=True)
#
#    def __str__(self):
#        return self.host


# class Goal(model.Model):
#    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
#    minute = models.IntegerField(),
#    scored_player = models.ForeignKey(Player, on_delete=models.CASCADE),
#    assist_player = models.ForeignKey(Player, on_delete=models.CASCADE),
#    assist_type = models.CharField(max_length=60, blank=True),
#    goal_type = models.CharField(max_length=60, blank=True),


# class MissedPenalty(model.Model):
#    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
#    scored_player = models.ForeignKey(Player, on_delete=models.CASCADE),
#    goalkeeper = models.ForeignKey(Player, on_delete=models.CASCADE),
#    reason = models.CharField(max_length=60, blank=True),
#    result = models.CharField(max_length=60, blank=True),


# class Substitutions(model.Model):
#    match_id = models.ForeignKey(Match, on_delete=models.CASCADE),
#    player_in = models.ForeignKey(Player, on_delete=models.CASCADE),
#    player_out = models.ForeignKey(Player, on_delete=models.CASCADE),
#    reason = models.CharField(max_length=60, blank=True),


# class Card(model.Model):
#    match_id = models.ForeignKey(Match, on_delete=models.CASCADE),
#    player_in = models.ForeignKey(Player, on_delete=models.CASCADE),
#    card_type = models.CharField(max_length=60, blank=True),
#    reason = models.CharField(max_length=60, blank=True),


# class Player(model.Model):
#    name = models.CharField(max_length=120, blank=False),
#    title = models.CharField(max_length=120, blank=False),


# class Coach(model.Model):
#    name = models.CharField(max_length=120, blank=False),


# class Stadium(model.Model):
#    name = models.CharField(max_length=120, blank=False),


# class Week(models.Model):
#    season = models.ForeignKey(Season, on_delete=models.CASCADE)
#    currentMatchday = models.IntegerField()
#    standing = models.ForeignKey(Standing, on_delete=models.CASCADE)


class Standing(models.Model):
    position = models.IntegerField()
    playedGames = models.IntegerField()
    won = models.IntegerField()
    draw = models.IntegerField()
    lost = models.IntegerField()
    points = models.IntegerField()
    goalsFor = models.IntegerField()
    goalsAgainst = models.IntegerField()
    goalDifference = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.playedGames.value_to_string()
