from enum import IntEnum

class Parties(IntEnum): # 3 seats per constituency
    Conservative = 1
    Labour = 2
    Liberal_Democrats = 3
    Reform_UK = 4
    Green = 5
    Independant = 6

popular_votes = {party.name: 0 for party in Parties}

popular_votes[Parties(5).name] += 1
print(popular_votes)