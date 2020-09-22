# Generated by Django 3.0.5 on 2020-09-13 07:13

from django.db import migrations, models
import djongo.models.fields
import football_mongo.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('alias', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('country_code', models.CharField(blank=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.CharField(blank=True, max_length=50)),
                ('season', models.CharField(blank=True, max_length=50)),
                ('week', models.CharField(blank=True, max_length=50)),
                ('stadium', models.CharField(blank=True, max_length=200)),
                ('match_date', models.CharField(blank=True, max_length=40)),
                ('match_time', models.CharField(blank=True, max_length=10)),
                ('referee', models.CharField(blank=True, max_length=200)),
                ('referee_assist_1st', models.CharField(blank=True, max_length=200)),
                ('referee_assist_2nd', models.CharField(blank=True, max_length=200)),
                ('host', djongo.models.fields.EmbeddedField(model_container=football_mongo.models.Host)),
                ('guest', djongo.models.fields.EmbeddedField(model_container=football_mongo.models.Host)),
                ('missed_penalties', djongo.models.fields.ArrayField(model_container=football_mongo.models.MissedPenalties, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('alias', models.CharField(blank=True, max_length=25)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('team', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('alias', models.CharField(blank=True, max_length=50)),
                ('year', models.IntegerField()),
                ('league', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Standing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.CharField(blank=True, max_length=50)),
                ('season', models.CharField(blank=True, max_length=50)),
                ('week', models.IntegerField(blank=True)),
                ('detail', djongo.models.fields.ArrayField(model_container=football_mongo.models.Standing_Detail, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(blank=True, max_length=150, primary_key=True, serialize=False)),
                ('alias', models.CharField(blank=True, max_length=50)),
                ('logo', models.CharField(blank=True, max_length=150)),
                ('season', models.CharField(blank=True, max_length=50)),
                ('league', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
