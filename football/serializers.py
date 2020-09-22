from rest_framework import serializers

from .models import Standing, Team, Season


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class StandingSerializer(serializers.ModelSerializer):

    class _SeasonSerializer(serializers.ModelSerializer):
        class Meta:
            model = Season
            fields = ('id', 'title', 'startDate', 'endDate')

    class _TeamSerializer(serializers.ModelSerializer):
        class Meta:
            model = Season
            fields = ('id', 'alias')

    season = _SeasonSerializer(many=False, read_only=True)
    team = _TeamSerializer(many=False, read_only=True)

    class Meta:
        model = Standing
        fields = '__all__'
        depth = 2
