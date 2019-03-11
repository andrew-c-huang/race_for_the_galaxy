from player import BasePlayer
from deck import GameDeck
import numpy as np

class RaceForTheGalaxy(object):
    def __init__(self, player_number=2, card_sets=['base']):
        self.player_number = player_number
        self.players = []
        self.card_sets = card_sets
        self.round = 0
        self.phase_selected = None
        self.phase = None
        self.deck = None
        self.victory_point_pool = None

    def create_game(self):
        if self.player_number == 2:
            self.victory_point_pool = 30

        self.create_players()
        self.create_deck()

    def create_players(self):
        for player_id in np.arange(1, self.player_number + 1):
            self.players.append(BasePlayer(player_id))

    def create_deck(self):
        self.deck = GameDeck(self.card_sets)


    def check_phase_complete(self):
        """
        verify that all players have completed potential actions or decided to pass
        :return:
        """
        pass

    def move_phase(self):
        """
        increment phase after all players complete action
        :return:
        """
        phase_info = {1: 'explore',
                      2: 'develop',
                      3: 'settle',
                      4: 'trade',
                      5: 'consume',
                      6: 'produce'}

        self.phase += 1

    def check_game_end_conditions(self):
        """
        At the end of each round, check 12 cards or zero victory points
        :return:
        """
        pass


    def victory_point_count(self):
        pass


    def report_victory_point_count(self):
        """

        :return:
        """
        pass

    def declare_winner(self):
        pass

