"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Player, Battle


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class ModelTests(TestCase):

    def test_player_repr(self):

        player = Player(nickname='philip')
        self.assertEqual(str(player), 'philip')

    def test_battle_repr(self):
        player1 = Player(nickname='philip')
        player2 = Player(nickname='chris')
        battle = Battle(attacker=player1, defender=player2, winner=player2)

        self.assertEqual(str(battle), 'philip v. chris')
