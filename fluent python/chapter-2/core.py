import array

arr = array.array('i',[0,1,1,3])

list(filter(lambda x :x * 2, [1,2,3,4]))
list(map(lambda x: x * 2, [1,2,3,4]))
[x * 2 for x in [1,2,3,4]]
suits = ['Diamonds_', 'Spades_', 'Clubs_', 'Hearts_']
ranks = [str(index) for index in range(1,11)] + ['J', 'Q', 'K', 'A']
cards = [suit+rank for suit in suits for rank in ranks]



suit = ['Diamonds_', 'Spades_', 'Clubs_', 'Hearts_']
ranks = [str(index) for index in range(1,11)] + ['J', 'Q', 'K', 'A']
for card in  (suit+rank for suit in suits for rank in ranks):
    print(card)

pass