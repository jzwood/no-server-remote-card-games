# Play (some) card games over the phone

## How
- all players must possess local copies of identically shuffled decks
- each game all players locally deal from matching decks such that only they can see only their cards
- the mechanics of the game are orchestrated over the phone

## But How How?
- each player clones this repo and opens up a python3 repl
- over the phone players agree on secret key, e.g. 'rK8v#23Qo'

**Player 1**
```
from locally_synced_deck import n_shuffled_decks

decks = n_shuffled_decks(50, 'rK8v#23Qo')
d1 = decks[0]
num_players = 3
position = 0
d1.deal_holdem(num_players, position)

Player 0:       1 ♥, 1 ♣
==========
7 ♥
Q ♦
J ♣
5 ♥
J ♥
Show all hands:
> Player 0:     1 ♥, 1 ♣
  Player 1:     A ♣, 4 ♥
  Player 2:     10 ♣, A ♥

```
**Player 2**
```
from locally_synced_deck import n_shuffled_decks

decks = n_shuffled_decks(50, 'rK8v#23Qo')
d1 = decks[0]
num_players = 3
position = 1
d1.deal_holdem(num_players, position)

Player 1:       A ♣, 4 ♥
==========
7 ♥
Q ♦
J ♣
5 ♥
J ♥
Show all hands:
  Player 0:     1 ♥, 1 ♣
> Player 1:     A ♣, 4 ♥
  Player 2:     10 ♣, A ♥
```
**Player 3**
```
from locally_synced_deck import n_shuffled_decks

decks = n_shuffled_decks(50, 'rK8v#23Qo')
d1 = decks[0]
num_players = 3
position = 2
d1.deal_holdem(num_players, position)

Player 2:       10 ♣, A ♥
==========
7 ♥
Q ♦
J ♣
5 ♥
J ♥
Show all hands:
  Player 0:     1 ♥, 1 ♣
  Player 1:     A ♣, 4 ♥
> Player 2:     10 ♣, A ♥
```

## Cheating proof?
Obviously not
