# System based on seats being distributed based on popular vote share. 
# Each voter selects one candidate/

import random
import time
from parties import EnglandParties, ScotlandParties, WalesParties, NIrelandParties
import pandas as pd
from typing import Literal

VOTES_PER_CONSTITUENCY = 70000 # assumption
TURNOUT_LOWER_BOUND = 0.5
TURNOUT_UPPER_BOUND = 0.88

def _generateConstituencies(filename: str, nation: Literal["England", "Scotland", "Wales", "Northern_Ireland"]):
    df = pd.read_csv(filename)
    constituencies = []
    delineating_letter = nation[0].upper()
    for _, row in df.iterrows():
        if row[0].startswith(delineating_letter):
            constituencies.append(row[1])

    return constituencies
    
all_parties = []
all_parties.extend([party.name for party in EnglandParties])
all_parties.extend([party.name for party in ScotlandParties if party.name not in all_parties])
all_parties.extend([party.name for party in WalesParties if party.name not in all_parties])
all_parties.extend([party.name for party in NIrelandParties if party.name not in all_parties])

FILENAME = "resources/constituencies.csv"
england_constituencies = _generateConstituencies("resources/constituencies.csv", "England")
scotland_constituencies = _generateConstituencies("resources/constituencies.csv", "Scotland")
wales_constituencies = _generateConstituencies("resources/constituencies.csv", "Wales")
nIreland_constituencies = _generateConstituencies("resources/constituencies.csv", "Northern_Ireland")

NUMBER_CONSTITUENCIES = len(england_constituencies) + len(scotland_constituencies) + len(wales_constituencies) + len(nIreland_constituencies)

def _generateWeights(partyQuantity: int):
    weightSum = 0
    while weightSum != 1.0:
        weights = [random.random() for _ in range(partyQuantity)]
        normalised_weights = [round(w / sum(weights), 2) for w in weights]
        if sum(normalised_weights) != 1.0:
            diff = round(sum(normalised_weights) - 1.0, 2)
            normalised_weights[random.randint(0, len(weights) - 1)] + diff
        weightSum = sum(normalised_weights) # condition check
    return normalised_weights

def _generateVote(parties: str, weighting: float) -> str:
    vote = random.choices(parties, weights=weighting, k=1)[0]
    return vote

def _generateSeats(votes: int, total_votes: int) -> int:
    ratio = round(votes/total_votes, 3) # maybe do 2 sig figs
    return int(ratio * NUMBER_CONSTITUENCIES), ratio

parties = lambda Parties: [party.name for party in Parties]

england_parties = parties(EnglandParties)
scotland_parties = parties(ScotlandParties)
wales_parties = parties(WalesParties)
nIreland_parties = parties(NIrelandParties)

popular_vote = {party:0 for party in all_parties}
seat_share = {party:0 for party in all_parties}

print("Starting simulation...")
start_time = time.time()
# England
for constituency in england_constituencies:
    turnout = round(random.uniform(TURNOUT_LOWER_BOUND, TURNOUT_UPPER_BOUND), 2)
    england_constituency_weights = _generateWeights(len(EnglandParties))
    for voter in range(int(VOTES_PER_CONSTITUENCY * turnout)):
        popular_vote[_generateVote(england_parties, england_constituency_weights)] += 1
print("England Counted")

# Scotland
for constituency in scotland_constituencies:
    turnout = round(random.uniform(TURNOUT_LOWER_BOUND, TURNOUT_UPPER_BOUND), 2)
    scotland_constituency_weights = _generateWeights(len(ScotlandParties))
    for voter in range(int(VOTES_PER_CONSTITUENCY * turnout)):
        popular_vote[_generateVote(scotland_parties, scotland_constituency_weights)] += 1
print("Scotland Counted")

# Wales
for constituency in wales_constituencies:
    turnout = round(random.uniform(TURNOUT_LOWER_BOUND, TURNOUT_UPPER_BOUND), 2)
    wales_constituency_weights = _generateWeights(len(WalesParties))
    for voter in range(int(VOTES_PER_CONSTITUENCY * turnout)):
        popular_vote[_generateVote(wales_parties, wales_constituency_weights)] += 1      
print("Wales Counted")

# Northern Ireland
for constituency in nIreland_constituencies:
    turnout = round(random.uniform(TURNOUT_LOWER_BOUND, TURNOUT_UPPER_BOUND), 2)
    nIreland_constituency_weights = _generateWeights(len(NIrelandParties))
    for voter in range(int(VOTES_PER_CONSTITUENCY * turnout)):
        popular_vote[_generateVote(nIreland_parties, nIreland_constituency_weights)] += 1
print("Northern Ireland Counted\n")

# Distribute votes
total_votes = 0
for party, vote_count in popular_vote.items():
    total_votes += vote_count

elected_seats = 0
party_ratio_seats = []
for party in all_parties:
    seats, ratio = _generateSeats(popular_vote[party], total_votes)
    elected_seats += seats
    seat_share[party] += seats
    party_ratio_seats.append([party, ratio, seats])

if elected_seats > NUMBER_CONSTITUENCIES:
    print(f"Problem with seat share calculation, elected seats {elected_seats} > {NUMBER_CONSTITUENCIES}")
    exit(-1)
elif elected_seats < NUMBER_CONSTITUENCIES: 
    parties_to_adjust = []
    while len(parties_to_adjust) != NUMBER_CONSTITUENCIES - elected_seats:
        for party_share in party_ratio_seats:
            seats_float = party_share[1] * NUMBER_CONSTITUENCIES
            if seats_float - int(seats_float) >= 0.5:
                parties_to_adjust.append(party_share[0])
    for party in parties_to_adjust:
        seat_share[party] += 1
        elected_seats += 1


end_time = time.time()
print(f"Seats elected: {elected_seats}\n")
for party, seats in seat_share.items():
    print(f"{party.replace('_', ' ')} gets {seats} seats")
print(f"Turnout is {round(total_votes/(NUMBER_CONSTITUENCIES*VOTES_PER_CONSTITUENCY) * 100, 2)}%")
print(f"Simulation time was: {round(end_time-start_time, 2)} seconds.\nGoodbye!")
