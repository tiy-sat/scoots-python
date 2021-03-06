import unittest
import random
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class PlayingCard:
    def __init__(self, value, suit):
        if suit not in self.suits:
            raise AttributeError("suit not valid")
        if value not in self.values:
            raise AttributeError("value not valid")

        self.value = value
        self.suit = suit

    suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
    values = {'ace': 'ace',
              '2': 'two',
              '3': 'three',
              '4': 'four',
              '5': 'five',
              '6': 'six',
              '7': 'seven',
              '8': 'eight',
              '9': 'nine',
              '10': 'ten',
              'queen': 'queen',
              'king': 'king',
              'jack': 'jack'}

    def short_name(self):
        """Returns the Short Name of a card ex.(KH,7S)"""
        return '{0}{1}'.format(self.value[0].upper(),
                               self.suit[0].upper())


    def long_name(self):
        """Returns long Name of card ex(King of Hearts , Seven of Spades)"""
        return '{0} of {1}'.format(self.values[self.value].capitalize(),
                                   self.suit.capitalize())

    def get_value(self):
        return self.value

    def Rank(self):
        """Sets facecard value to int 10"""
        if self.value in ('jack', 'queen', 'king'):
            return 10
        elif self.value is 'ace':
            return 11
        else:
            return int(self.value)


class Deck():
    def __init__(self):
        self.cards = []
        for suit in PlayingCard.suits:
            for value in PlayingCard.values:
                self.cards.append(PlayingCard(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)
        return

    def deal_card(self):
        return self.cards.pop()


class Hand():
    def __init__(self):
        self.cards = []


    def get_card(self, oneCard):
        """Grabs card from Table"""
        return self.cards.append(oneCard)

    def value_Of_Hand(self):
        """Returns the total value for cards in hand."""

        cardTotal= 0
        for num in range(0,len(self.cards)):
            cardTotal += self.cards[num].Rank()
        for num in range(0,len(self.cards)):
            if self.cards[num].get_value() == 'ace':
                if cardTotal > 21:
                    cardTotal -= 10
        return cardTotal


    def read_Hand(self):
        """Prints hands as well as card totals."""
        for num in range(0, len(self.cards)):
            print("{0} > {1}".format(self.cards[num].long_name(), self.cards[num].short_name()))
        print('''

        Card Total: {0}

        '''.format(self.value_Of_Hand()))



class Bets():
    def __init__(self):
    self.Pot = 0


def play_again():
    again = input("Play again? (y/n) : ").lower()
    choice = None
    if again == 'y':
        cls()
        game()
    else:
        print("BYE!")
        choice = 'q'
    return choice


def display_player():

    print("------------------Your Hand--------------------")


def display_dealer():
    print("-------------The Dealer is Showing:------------")



def suspense():
    """Animated dots for suspense"""
    print('.')
    time.sleep(1)
    print('..')


def longsuspense():
    """Longer animated dots"""
    print('.')
    time.sleep(1)
    print('..')
    time.sleep(1)
    print('...')


def game():
    """main Game loop"""

    print('''
MM"""""""`YM M""MMMM""M MMMMMMMM""M MMP"""""""MM MM'""""'YMM M""MMMMM""M
MM  mmmmm  M M. `MM' .M MMMMMMMM  M M' .mmmm  MM M' .mmm. `M M  MMMM' .M
M'        .M MM.    .MM MMMMMMMM  M M         `M M  MMMMMooM M       .MM
MM  MMMMMMMM MMMb  dMMM MMMMMMMM  M M  MMMMM  MM M  MMMMMMMM M  MMMb. YM
MM  MMMMMMMM MMMM  MMMM M. `MMM' .M M  MMMMM  MM M. `MMM' .M M  MMMMb  M
MM  MMMMMMMM MMMM  MMMM MM.     .MM M  MMMMM  MM MM.     .dM M  MMMMM  M
MMMMMMMMMMMM MMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM
                - A BlackJack Game-

                   HELLO! Welcome to PYJACK!
               -                               -
                 try to get 21 without going over.
                 -       or at least beat the dealer    -
                 ''')


    choice = 'h'
    reveal = 'n'
    dealerHand = Hand()
    playerHand = Hand()
    deck = Deck()
    deck.shuffle()

    #deals two cards to each player
    for card in range(2):
        playerHand.get_card(deck.deal_card())
        dealerHand.get_card(deck.deal_card())

    while choice != 'q':
    #displays ascii art and prints cards and Total
        display_player()
        playerHand.read_Hand()

        display_dealer()
        dealerHand.read_Hand()

        if dealerHand.value_Of_Hand() == 21:
            print("Dealer got BlackJack")
            print("YOU LOSE!")
            break
        if playerHand.value_Of_Hand() == 21:
            print("Player has BlackJack")
            print("YOU WIN!!")
            break


        choice = input("do you want to [H]it, [S]tay, or [Q]uit: ").lower()
        if choice == 'h':
            suspense()
            playerHand.get_card(deck.deal_card())

            if playerHand.value_Of_Hand() > 21:
                display_player()
                playerHand.read_Hand()
                print("SORRY YOU BUSTED!")
                break

        elif choice == 's':

            if dealerHand.value_Of_Hand() <= 17:
                longsuspense()
                dealerHand.get_card(deck.deal_card())

            elif dealerHand.value_Of_Hand() > 17:
                suspense()
                print("The Dealer Stays")

            elif dealerHand.value_Of_Hand() > 21:
                display_dealer()
                dealerHand.read_Hand()
                suspense()
                print("DEALER BUSTS! YOU WIN!!")
                break

            elif playerHand.value_Of_Hand() > 21:
                display_player()
                playerHand.read_Hand()
                suspense()
                print("SORRY YOU BUSTED")
                break

            elif playerHand.value_Of_Hand() == 21:
                display_player()
                playerHand.read_Hand()
                suspense()
                print("CONGRATUALTIONS, YOU WIN!!")
                break

            elif playerHand.value_Of_Hand() > dealerHand.value_Of_Hand():
                display_player()
                suspense()
                playerHand.read_Hand()
                display_dealer()
                suspense()
                dealerHand.read_Hand()
                print('CONGRATUALTIONS, YOU WON!!')
                break

            elif playerHand.value_Of_Hand() < dealerHand.value_Of_Hand():
                display_player()
                suspense()
                playerHand.read_Hand()
                display_dealer()
                suspense()
                dealerHand.read_Hand()
                print("DEALER WINS!")
                print('YOU LOSE!')
                break

            else:
                display_player()
                suspense()
                playerHand.read_Hand()
                display_dealer()
                suspense()
                dealerHand.read_Hand()
                print("PUSH! Its a draw!")
                break

    play_again()




class TestPlayingCard(unittest.TestCase):
    def testSuits(self):
        self.assertEqual(4, len(PlayingCard.suits))
        self.assertTrue('hearts' in PlayingCard.suits)
        self.assertFalse('weasels' in PlayingCard.suits)

    def testValues(self):
        self.assertEqual(13, len(PlayingCard.values))
        self.assertTrue('9' in PlayingCard.values)
        self.assertTrue('21' not in PlayingCard.values)

    def testInit(self):
        pc1 = PlayingCard('ace', 'hearts')
        self.assertEqual('ace', pc1.value)
        self.assertEqual('hearts', pc1.suit)
        with self.assertRaises(TypeError):
            pc2 = PlayingCard()

        with self.assertRaises(AttributeError):
            pc3 = PlayingCard('duke', 'earl')

    def testShortName(self):
        pc1 = PlayingCard('9', 'clubs')
        self.assertEqual('9C', pc1.short_name())

    def testLongName(self):
        pc = PlayingCard('10', 'hearts')
        self.assertEqual('Ten of Hearts', pc.long_name())


class TestDeck(unittest.TestCase):
    def testInit(self):
        deck = Deck()
        self.assertEqual(52, len(deck.cards))

    def testShuffle(self):
        deck = Deck()
        copy_of_cards = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(copy_of_cards, deck.cards)

    def testDealCard(self):
        deck = Deck()
        copy_of_cards = deck.cards[:]
        deck.deal_card()
        self.assertNotEqual(copy_of_cards, deck.cards)


class TestHand(unittest.TestCase):
    def testInit(self):
        PlayerHand = Hand()
        self.assertFalse(PlayerHand is False)

    def testGetCard(self):
        PlayerHand = Hand()
        deck = Deck()
        PlayerHand.get_card(deck.deal_card)
        self.assertTrue(PlayerHand)





if __name__ == '__main__':
    # unittest.main()

    game()








































    #
    #


    # Or do game logic in a function


    #     print('Your hand: ']
    #     playerHand.read_Hand()
    #     dealerHand.read_Hand()
    # elif choice == 's':
    #     while dealerHand.value_Of_Hand() < 17:
    #         dealerHand.get_card(deck.deal_card())
    #     dealerHand.value_Of_Hand()
    #     play_again()
    # elif choice == "q":
    #     print("SEE YA!")
