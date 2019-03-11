import numpy as np


class BaseDeck(object):
    def __init__(self):
        self.deck = []

    def deck_names(self):
        return [card.name for card in self.deck]


class GameDeck(BaseDeck):
    def __init__(self, card_sets):
        super(GameDeck, self).__init__()
        self.discard = None
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
                self.deck.append(self.card_factory(card))
        self.shuffle()

    def shuffle(self):
        np.random.shuffle(self.deck)

    def check_card_count(self):
        if not self.deck:
            self.deck = self.discard.copy()
            self.shuffle()
            self.discard = None


CARD_SET_LOOKUP = {'base': ['SecludedWorld', 'WarriorRace']}