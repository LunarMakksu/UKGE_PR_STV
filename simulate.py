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

class EnglandParties(IntEnum): # 3 seats per constituency
    Conservative = 1
    Labour = 2
    Liberal_Democrats = 3
    Reform_UK = 4
    Green = 5
    Independant = 6

class ScotlandParties(IntEnum):
    Conservative = 1
    Labour = 2
    Liberal_Democrats = 3
    Reform_UK = 4
    Green = 5
    Independant = 6
    SNP = 7

class WalesParties(IntEnum):
    Conservative = 1
    Labour = 2
    Liberal_Democrats = 3
    Reform_UK = 4
    Green = 5
    Independant = 6
    Plaid_Cymru = 7

class NIrelandParties(IntEnum): # theres more
    Democratic_Unionist_Party = 1
    Traditional_Unionist_Voice = 2
    Sinn_Fein = 3
    Alliance_Party = 4
    Ulster_Unionist_Party = 5

popular_votes = {party.name: 0 for party in EnglandParties}

def _generateWeights(partyQuantity: int):
    weightSum = 0
    while weightSum != 1.0:
        weights = [random.random() for _ in range(partyQuantity)]
        normalised_weights = [round(w / sum(weights), 2) for w in weights]
        if sum(normalised_weights) != 1.0:
            diff = round(sum(normalised_weights) - 1.0, 2)
            print("diff ", diff)
            normalised_weights[random.randint(0, len(weights) - 1)] + diff
        weightSum = sum(normalised_weights) # condition check
    return normalised_weights

def _createConstituencyVotesDict() -> dict:
    return dict({party.name: 0 for party in EnglandParties})

def _pickParty(excl) -> int:
    choice = None
    condition = False
    while not condition:
        choice = random.choice([int(party) for party in EnglandParties])
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


england_weights = _generateWeights(len(EnglandParties))
scotland_weights = _generateWeights(len(ScotlandParties))
wales_weights = _generateWeights(len(WalesParties))
northernIreland_weights = _generateWeights(len(NIrelandParties))

for constituency, constituencyIdx in enumerate(constituencies): # long
    print(constituency)
    partyVotes = _createConstituencyVotesDict()
    allVotes = []
    for voter in range(VOTES_PER_CONSTITUENCY):
        votes = _generateVote()
        allVotes.append(votes)
        for vote in votes:
            partyVotes[EnglandParties(vote[0]).name] += 1
    # weight votes
    
            
