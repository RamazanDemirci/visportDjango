from rest_framework import serializers
from .models import Match, Host, Goal, Card, Change, Player, Pos, Person, League, Season, Team, Standing, Standing_Detail, MissedPenalties


class PosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    pos = PosSerializer(many=False)

    class Meta:
        model = Player
        fields = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class ChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Change
        fields = '__all__'


class MissedPenaltiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissedPenalties
        fields = '__all__'


class HostSerializer(serializers.ModelSerializer):
    goals = GoalSerializer(many=True)
    #cards = CardSerializer(many=True)
    #changes_in = ChangeSerializer(many=True)
    #changes_out = ChangeSerializer(many=True)
    #players = PlayerSerializer(many=True)

    class Meta:
        model = Host
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    host = HostSerializer(many=False)
    #guest = HostSerializer(many=False)
    #missed_penalties = MissedPenaltiesSerializer(many=False)

    class Meta:
        model = Match
        fields = '__all__'


class FixtureHostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Host
        fields = ('name', 'score')


class FixtureSerializer(serializers.ModelSerializer):
    host = FixtureHostSerializer(many=False)
    guest = FixtureHostSerializer(many=False)

    class Meta:
        model = Match
        fields = ('match_date', 'match_time', 'stadium', 'host', 'guest')

    def to_representation(self, instance):
        return {
            'date': instance.match_date,
            'time': instance.match_time,
            'stadium': instance.stadium,
            'host': instance.host['name'],
            'h_score': instance.host['score'],
            'guest': instance.guest['name'],
            'g_score': instance.guest['score'],
        }


class Standing_DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standing_Detail
        fields = '__all__'


class StandingSerializer(serializers.ModelSerializer):
    detail = Standing_DetailSerializer(many=True)

    class Meta:
        model = Standing
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class LeagueSerializer(serializers.ModelSerializer):

    class Meta:
        model = League
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Season
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'
