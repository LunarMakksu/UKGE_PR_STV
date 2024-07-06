# pretending they're all in england for now
import random
from enum import IntEnum
import pandas as pd

def generateConstituencies(filename: str):
    df = pd.read_csv(filename)
    constituencies = df["PCON24NM"]
    return constituencies

FILENAME = "resources/constituencies.csv"
constituencies = generateConstituencies("resources/constituencies.csv")

NUMBER_CONSTITUENCIES = len(constituencies)
VOTES_PER_CONSTITUENCY = 70000

class Parties(IntEnum): # 3 seats per constituency
    Conservative = 1
    Labour = 2
    Liberal_Democrats = 3
    Reform_UK = 4
    Green = 5
    Independant = 6
weights = [0.22, 0.39, 0.14, 0.19, 0.05, 0.04]

popular_votes = {party.name: 0 for party in Parties}

def _createConstituencyVotesDict() -> dict:
    return dict({party.name: 0 for party in Parties})

def _pickParty(excl) -> int:
    choice = None
    condition = False
    while not condition:
        choice = random.choice([int(party) for party in Parties])
        if choice not in excl:
            condition = True
    return choice

def _generateVote():
    choices = [] # in order of preference
    for i in range(3):
        choices.append([_pickParty(choices), i+1]) # [party, preference]
    if len(choices) != 3:
        raise Exception("Invalid vote return. Should be 3")
    return choices

for constituency, constituencyIdx in enumerate(constituencies): # long
    print(constituency)
    partyVotes = _createConstituencyVotesDict()
    allVotes = []
    for voter in range(VOTES_PER_CONSTITUENCY):
        votes = _generateVote()
        allVotes.append(votes)
        for vote in votes:
            partyVotes[Parties(vote[0]).name] += 1
    print(partyVotes)
