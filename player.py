from deck import BaseDeck

class BasePlayer(object):
    def __init__(self, player_id):
        self.id = player_id
        self.victory_point = 0
        self.card_hand = []
        self.card_board = []
        self.phase_privilege = []
        self.military = 0

    def select_phase_privilege(self):
        """ raw input """
        self.phase_privilege.append(1)

    def verify_phase_cards(self):
        pass

    def explore(self, game):
        draw_count = 2
        select_count = 1

        if 1 in self.phase_privilege:
            draw_count += 1
            select_count += 1

        draw_cards = BaseDeck()
        for draw in range(draw_count):
            game.deck.check_card_count()
            draw_cards.deck.append(game.deck.pop())

        select = 0
        while select in range(select_count):
            input_card = input('choose from: {}'.format(draw_cards.deck_names()))

            if input_card in draw_cards:
                self.card_hand.append(input_card)
                self.draw_cards.deck.pop(input_card)
            else:
                print("""card is not available.
                choose from : {}""".format(draw_cards.deck_names()))

        game.deck.deck.append(self.draw_cards.deck)


    def develop(self):
        """
        activate card powers
        select development from hand
        pay cost
        remove from hand and place on board
        :return:
        """
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
        for card in self.card_hand:
            if card.is_windfall == False:
                card.has_production = True

