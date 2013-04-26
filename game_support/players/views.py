from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import (
    View,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from models import Player, Battle
from serializers import PlayerSerializer, BattleSerializer

class PlayerList(generics.ListCreateAPIView):
    """
    List all players, or create a new player.
    """
    model = Player
    serializer_class = PlayerSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Player
    serializer_class = PlayerSerializer
    permissions_classes = (permissions.IsAuthenticated,)


class BattleList(generics.ListCreateAPIView):
    model = Battle
    serializer_class = BattleSerializer
    permissions_classes = (permissions.IsAuthenticated)


class BattleDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Battle
    serializer_class = BattleSerializer
    permissions_classes = (permissions.IsAuthenticated)

class PlayerSearch(View):

    def dispatch(self, request, *args, **kwargs):
        search = request.GET.get('nickname')

        if search is None:
            return redirect(reverse('player-list'))

        try:
            player_id = Player.objects.filter(nickname=search)[0].id
        except IndexError:
            player_id = None

        if player_id is not None:
            return redirect(reverse('player-detail', kwargs={'pk': player_id}))
        else:
            return redirect(reverse('player-list'))





