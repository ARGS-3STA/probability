from .cards import Cards  # Used in game 1
from .card import Card
from .dice import Dice  # Used in game 2


def game_1(times: int, pairs: int) -> dict[str, int]:  # {"a_wins": int, "b_wins": int}
    deck_list = []
    for _ in range(pairs):
        deck_list.append(Card(1))
        deck_list.append(Card(0))
    deck = Cards(deck_list)

    a_wins = 0
    b_wins = 0
    for _ in range(times):
        list_card = deck.draw_cards(amount=2)
        if list_card[0] == list_card[1]:
            b_wins += 1
        else:
            a_wins += 1
    return {"a_wins": a_wins, "b_wins": b_wins}


def game_2(amount: int) -> dict[str, int]:  # {"a_wins": 69, "b_wins": 21}
    # masse shit
    a_wins = 0
    b_wins = 0

    coin_1 = Dice(sides=2)
    coin_2 = Dice(sides=2)

    for _ in range(amount):
        if coin_1.coin() == coin_2.coin():
            a_wins += 1
        else:
            b_wins += 1

    return {"a_wins": a_wins, "b_wins": b_wins}


def game_3(
    amount: int, times: int
) -> dict[str, int]:  # {"house_wins": int, "player_wins": int }
    house_wins = 0
    player_wins = 0

    for _ in range(times):
        game = True

        house = amount
        player = amount

        dice_1 = Dice(sides=6)
        dice_2 = Dice(sides=6)

        while game:
            if dice_1.die() == dice_2.die():
                house -= 3
                player += 3
                # player += 1 not adding this because if the ods are equale, there are going to be some games that might last forever assuming the amount is large enough
            else:
                house += 1
                player -= 1
                # house += 1

            if player <= 0:
                game = False
                house_wins += 1
            elif house <= 0:
                game = False
                player_wins += 1

        return {"house_wins": house_wins, "player_wins": player_wins}
