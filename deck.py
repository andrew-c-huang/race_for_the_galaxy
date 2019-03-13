import numpy as np


class BaseDeck(object):
    def __init__(self):
        self.card_supply = []

    def deck_names(self):
        return [card.name for card in self.card_supply]

    def first_card_matching_string(self):
        select_card = input('choose from: {}'.format(self.deck_names()))

        if select_card in self.deck_names():
            for card in self.card_supply:
                if card.name == select_card:
                    return card
        else:
            print("""card is not available.
                choose from : {}""".format(self.deck_names()))


class GameDeck(BaseDeck):
    def __init__(self, card_sets):
        super(GameDeck, self).__init__()
        self.discard_pile = []
        self.card_sets = card_sets
        self.create_cards()

    def card_factory(self, class_name):
        """instantiate a card class given a string"""
        import cards
        cls = getattr(cards, class_name)
        return cls()

    def create_cards(self):
        # create the cards
        for card_set in self.card_sets:
            for card in CARD_SET_LOOKUP[card_set]:
                self.card_supply.append(self.card_factory(card))
        self.shuffle()

    def shuffle(self):
        np.random.shuffle(self.card_supply)

    def replenish_card_supply_if_exhausted(self):
        if not self.card_supply:
            self.card_supply = self.discard_pile.copy()
            self.shuffle()
            self.discard_pile = None


CARD_SET_LOOKUP = {'base': ['SecludedWorld', 'WarriorRace', 'ExpeditionForce']}
