from deck import BaseDeck


class BasePlayer(object):
    def __init__(self, player_id):
        self.id = player_id
        self.victory_point = 0
        self.hand = BaseDeck()
        self.tableau = BaseDeck()
        self.phase_privilege = []
        self.military = 0

    def select_phase_privilege(self):
        """ raw input """
        self.phase_privilege.append(1)

    def verify_phase_cards(self):
        pass

    def draw_cards(self, game_deck, draw_count=1, keep_count=1):
        temp_deck = BaseDeck()
        for _ in range(draw_count):
            temp_deck.add_cards(game_deck.pop_card())

        # bypass the prompt if all drawn cards are kept
        if draw_count == keep_count:
            for _ in range(keep_count):
                self.hand.add_cards(temp_deck.pop_card())

        else:
            keep = 0
            while keep < keep_count:
                self.hand.add_cards(temp_deck.remove_cards_prompt())

                keep += 1
        game_deck.discard_pile.extend(temp_deck.deck)

    def place_to_tableau(self, reduce_cost):
        """ """
        card_to_place = self.hand.remove_cards_prompt(number=1)
        cards_to_pay = self.hand.remove_cards_prompt(number=card_to_place[0].cost - reduce_cost)
        self.tableau.add_cards(card_to_place)

    def explore(self, game_deck):
        """"""
        draw_count = 2
        keep_count = 1

        if 1 in self.phase_privilege:
            draw_count += 1
            keep_count += 1

        for card in self.hand.deck:
            if card.has_explore_power:
                draw_count += card.draw_extra
                keep_count += card.keep_extra

        for card in self.tableau.deck:
            if card.has_explore_power:
                draw_count += card.draw_extra
                keep_count += card.keep_extra

        self.draw_cards(game_deck, draw_count, keep_count)


    def develop(self):
        """
        select development from hand
        pay cost
        remove from hand and place on board
        :return:
        """
        reduce_cost = 0
        if 2 in self.phase_privilege:
            reduce_cost += 1

        for card in self.hand.deck:
            if card.has_develop_power:
                reduce_cost += card.reduce_cost

        for card in self.tableau.deck:
            if card.has_develop_power:
                reduce_cost += card.reduce_cost

        # TODO: check card to place is a development
        self.place_to_tableau(reduce_cost=reduce_cost)

    def settle(self):
        """
        activate card powers
        select settle
        pay cost
        place on board

        """

    def trade(self):
        pass

    def consume(self):
        pass

    def produce(self):
        for card in self.hand:
            if card.is_windfall == False:
                card.has_production = True

