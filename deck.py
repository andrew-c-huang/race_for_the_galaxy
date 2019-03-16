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

    def add_cards(self, card):
        if type(card) != list:
            card = [card]
        self.deck.extend(card)

    def remove_cards_prompt(self, number=1):
        card_list = []
        cards_removed = 0
        while cards_removed < number:
            select_card = input('choose from: {}'.format(self.card_names()))

            if select_card in self.card_names():
                card = self.card_from_name(select_card)
                self.deck.remove(card)
                card_list.append(card)
                cards_removed += 1

            else:
                print("""card is not available.
                    choose from : {}""".format(self.card_names()))

        return card_list

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
                self.add_cards(self.card_factory(card))
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


CARD_SET_LOOKUP = {'base': ['SecludedWorld', 'WarriorRace', 'ExpeditionForce', 'InvestmentCredits',
                            'InterstellarBank', 'ReplicantRobots']}
