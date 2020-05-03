#!/usr/bin/env python3

import random
from six.moves import input


class deck:
    def __init__(self, id):
        self.id = id
        red = lambda text: '\033[91m{}\033[0m'.format(text)
        deck = ['A'] + list(range(1, 11)) + ['J', 'Q', 'K']
        red_suits = ['♥', '♦']
        black_suits = ['♣', '♠']
        suits = [red(s) for s in red_suits] + black_suits
        self.cards = ['{} {}'.format(value, suit) for suit in suits for value in deck]

    def deal_holdem(self, num_players, p1_position=0):
        """ p1_position refers to the index of the current player """
        eod = num_players * 2
        deal = list(zip(self.cards[:num_players], self.cards[num_players: eod]))
        hands = [list(map(str, hand)) for hand in deal]
        hand = hands[p1_position]
        flop = self.cards[eod + 1: eod + 4]
        turn = self.cards[eod + 4]
        river = self.cards[eod + 5]
        print('Player {}:\t'.format(p1_position) + ', '.join(hand))
        input('=' * 10)
        input('\n'.join(flop))
        input(str(turn))
        print(str(river))
        input('Show all hands: ')
        for i, hand in enumerate(hands):
            print('{} Player {}:\t'.format('>' if i == p1_position else ' ', i) + ', '.join(hand))


def n_shuffled_decks(n, seed):
    random.seed(seed)
    decks = []
    for i in range(n):
        d = deck(i)
        random.shuffle(d.cards)
        decks.append(d)
    return decks


if __name__ == '__main__':
    decks = n_shuffled_decks(50, 'rK8v&23Qo')
    d1 = decks[0]
    d1.deal_holdem(4, 2)
