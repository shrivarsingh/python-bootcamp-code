import random
import art

def deal_card(deck):
    return random.choice(deck)


def score(hand):
    return sum(hand)

def display_player_turn(player_hand, dealer_hand):
    print(f"\n♠ ♣ ♥ ♦ Your cards are {player_hand}, current score = {score(player_hand)}")
    print(f"♠ ♣ ♥ ♦ Dealer's first card is: {dealer_hand[0]}")

def display_dealer_turn(player_hand, dealer_hand):
    print(f"\n♠ ♣ ♥ ♦ Your cards are {player_hand}, current score = {score(player_hand)}")
    print(f"♠ ♣ ♥ ♦ Dealer's cards are: {dealer_hand}, current score = {score(dealer_hand)}")

def check_winner(player_score, dealer_score):
    if player_score > dealer_score:
        print(f"\nPlayer: {player_score} | Dealer: {dealer_score}\nYou beat the dealer! You win! 😃")
        wins["Player"] += 1
    elif player_score < dealer_score:
        print(f"\nPlayer: {player_score} | Dealer: {dealer_score}\nThe house always wins. You lose! 😭")
        wins["Dealer"] += 1
    else:
        print(f"\nPlayer: {player_score} | Dealer: {dealer_score}\nIt's a draw. 🙄")

def check_ace(current_hand):
    if score(current_hand) > 10:
        return 1
    else:
        return 11


def blackjack():
    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    dealer_cards = []
    for i in range(2):
        player_cards.append(deal_card(cards))
        dealer_cards.append(deal_card(cards))
    continue_black_jack = True
    if player_cards[1] == 11:
        player_cards[1] = 1
    if dealer_cards[1] == 11:
        dealer_cards[1] = 1
    while continue_black_jack: # Player's Turn
        display_player_turn(player_cards, dealer_cards)
        hit = input("Type \"y\" to get another card, type \"n\" to to pass: ")
        if hit == "y":
            card_from_deck = deal_card(cards)
            if card_from_deck == 11:
                card_from_deck = check_ace(player_cards)
            print(f"\tPlayer drew {card_from_deck} from deck.")
            player_cards.append(card_from_deck)
            if score(player_cards) > 21:
                print(f"\n♠ ♣ ♥ ♦ Your cards are {player_cards}, current score = {score(player_cards)}")
                print("\tYou went over 21! You lose. 😨")
                wins["Dealer"] += 1
                return
        elif hit == "n":
            continue_black_jack = False
        else:
            print("\tYou counting cards!\n\tRestarting Game.\n")
            return
    while score(dealer_cards) < 16 or score(dealer_cards) < score(player_cards): # Dealer Turn
        display_dealer_turn(player_cards, dealer_cards)
        card_from_deck = deal_card(cards)
        if card_from_deck == 11:
            card_from_deck = check_ace(dealer_cards)
        print(f"\tDealer drew {card_from_deck} from deck.")
        dealer_cards.append(card_from_deck)
        if score(dealer_cards) > 21:
            print(f"\n♠ ♣ ♥ ♦ Dealer's cards are: {dealer_cards}, current score = {score(dealer_cards)}")
            print("\tDealer went over 21! You win. 😎")
            wins["Player"] += 1
            return
    display_dealer_turn(player_cards, dealer_cards)
    check_winner(score(player_cards), score(dealer_cards))

def play():
    play_game = "y"
    while play_game == "y":
        print("\n| ", end = "")
        for win in wins:
            print(f"{win} number of games won: {wins[win]}", end = " | ")
        play_game = input("\nDo you want to play a game of Blackjack? Type \"y\" or \"n\": ")
        if play_game == "y":
            blackjack()
        else:
            print("\nGoodBye.")

wins = {"Player": 0, "Dealer": 0}
play()
