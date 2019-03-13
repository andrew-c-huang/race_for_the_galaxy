from deck import BaseDeck


class BasePlayer(object):
    def __init__(self, player_id):
        self.id = player_id
        self.victory_point = 0
        self.hand = []
        self.tableau = []
        self.phase_privilege = []
        self.military = 0

    def select_phase_privilege(self):
        """ raw input """
        self.phase_privilege.append(1)

    def verify_phase_cards(self):
        pass

    def draw_cards(self, game_deck, draw_count=1, keep_count=1):
        temp_deck = BaseDeck()
        for draw in range(draw_count):
            game_deck.replenish_card_supply_if_exhausted()
            temp_deck.card_supply.append(game_deck.card_supply.pop())

        if draw_count == 1:
            self.hand.append(game_deck.card_supply.pop())

        else:
            keep = 0
            while keep < keep_count:
                select_card = temp_deck.first_card_matching_string()
                self.hand.append(select_card)
                temp_deck.card_supply.pop(select_card)

        game_deck.discard_pile.extend(temp_deck.card_supply)

    def explore(self, game_deck):
        """"""
        draw_count = 2
        keep_count = 1

        if 1 in self.phase_privilege:
            draw_count += 1
            keep_count += 1

        for card in self.hand:
            if card.has_explore_power:
                draw_count += card.draw_extra
                keep_count += card.keep_extra

        self.draw_cards(game_deck, draw_count, keep_count)


    def develop(self):
        """
        activate card powers
        select development from hand
        pay cost
        remove from hand and place on board
        :return:
        """
        card_name = 'secluded_world'
        self.hand.pop()
        pass

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

