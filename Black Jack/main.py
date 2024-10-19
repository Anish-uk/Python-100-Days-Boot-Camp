import random
import art
print(art.logo)


def pullout():
    player_card = random.choice(cards)
    players_cards.append(player_card)
    score = 0
    for i in range(len(players_cards)):
        score += players_cards[i]
    return score


def c_pullout():
    computer_card = random.choice(cards)
    computer_cards.append(computer_card)
    c_score = 0
    for i in range(len(computer_cards)):
        c_score += computer_cards[i]
    return c_score


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = True
while game_over:
    players_cards = []
    computer_cards = []
    option = input("Do you want to play a game of blackjack? 'y' or 'n': ")
    if option == 'y':
        pullout()
        game_score = pullout()
        print(f"Your cards:{players_cards}  Your score:{game_score}")
        c_scores = c_pullout()
        print(f"Computers card:{computer_cards}")
        game = input("Type 'y' to get a cart or Type 'n' to pass: ")
        if game == 'y':
            game_score = pullout()
            print(f"Your cards:{players_cards}  Your score:{game_score}")
            if game_score > 21:
                print("You Lose!")
                game_over = True
            else:
                while c_scores < 17:
                    c_scores = c_pullout()
                print(f"Computers cards:{computer_cards} Computer score:{c_scores}")
                if game_score > c_scores or c_scores > 21:
                    print("You Win!")
                    game_over = True
                else:
                    print("You Lose!")
                    game_over = True
        elif game == 'n':
            while c_scores < 17:
                c_scores = c_pullout()
            print(f"Computers cards:{computer_cards} Computer score:{c_scores}")
            if game_score > c_scores or c_scores > 21:
                print("You Win!")
                game_over = True
            else:
                print("You Lose!")
                game_over = True
    else:
        game_over = False
