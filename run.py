from game import RFTG

if __name__ == "__main__":
    r = RFTG()
    print('creating new game, 2 players')
    r.create_game()

    print('\n cards in card supply')
    print(r.card_supply.card_names())

    # getting explore to work
    print('\n player 1, draw card to create a hand')
    r.players[1].draw_cards(r.card_supply, draw_count=3, keep_count=3)
    #
    # print('\n new card supply should have one less card')
    # print(r.card_supply.card_names())
    # print('player 1 hand')
    # print(r.players[1].hand.card_names())
    # print('cards in discard')
    # print(len(r.card_supply.discard_pile))

    # explore

    r.players[1].explore(r.card_supply)

    print('\n player 1 hand')
    print(r.players[1].hand.card_names())


    # development
    r.players[1].develop()
