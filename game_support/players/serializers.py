from django.forms import widgets
from rest_framework import serializers
from players.models import Player, Battle

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player

class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
