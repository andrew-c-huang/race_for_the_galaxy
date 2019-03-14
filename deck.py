import numpy as np


class BaseDeck(object):
    def __init__(self):
        self.deck = []

    def card_names(self):
        return [card.name for card in self.deck]

    def card_from_name(self, name):
        for card in self.deck:
            if card.name == name:
                return card

    def pop_card(self):
        return self.deck.pop()

    def add_card(self, card):
        self.deck.append(card)

    def remove_card_prompt(self):
        while True:
            select_card = input('choose from: {}'.format(self.card_names()))

            if select_card in self.card_names():
                card = self.card_from_name(select_card)
                self.deck.remove(card)
                return card

            else:
                print("""card is not available.
                    choose from : {}""".format(self.card_names()))

class GameDeck(BaseDeck):
    def __init__(self, card_sets):
        super(GameDeck, self).__init__()
        self.discard_pile = []
        self.card_sets = card_sets
        self.create_cards()

    @staticmethod
    def card_factory(class_name):
        """instantiate a card class given a string"""
        import cards
        cls = getattr(cards, class_name)
        return cls()

    def create_cards(self):
        # create the cards
        for card_set in self.card_sets:
            for card in CARD_SET_LOOKUP[card_set]:
                self.add_card(self.card_factory(card))
        self.shuffle()

    def shuffle(self):
        np.random.shuffle(self.deck)

    def replenish_card_supply_if_exhausted(self):
        if not self.deck:
            self.deck = self.discard_pile.copy()
            self.shuffle()
            self.discard_pile = None

    def pop_card(self):
        self.replenish_card_supply_if_exhausted()
        return self.deck.pop()

CARD_SET_LOOKUP = {'base': ['SecludedWorld', 'WarriorRace', 'ExpeditionForce', 'InvestmentCredits']}
