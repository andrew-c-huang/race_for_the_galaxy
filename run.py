from game import RFTG

if __name__ == "__main__":
    r = RFTG()
    r.create_game()

    print('hi')

    print('\n')
    print(r.card_supply.deck_names())
    r.players[1].draw_cards(r.card_supply, draw_count=1, keep_count=1)

    print('new card supply')
    print(r.card_supply.deck_names())
    print(r.players[1].hand)

    # print('\n')
    # print(r.card_supply)
    # r.players[1].draw_cards(r.card_supply)
    # print(r.players[1].hand)