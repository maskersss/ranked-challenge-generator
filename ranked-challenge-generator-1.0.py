#!/usr/bin/env python
# coding: utf-8


# Define the difficulty of the challenges for each match
min_difficulty = 2.5
ideal_difficulty = 4


import random
from math import log

# Define the list of challenges with their corresponding difficulties and weights
challenges = [
    {"name":"Play without a calculator.", "difficulty":2.5, "weight":1807.2},
    {"name":"Have beds of 5 different colors in your inventory at some point during the run. ", "difficulty":0.9, "weight":2405.5},
    {"name":"Obtain an egg at some point during the run.", "difficulty":1.3, "weight":43.9},
    {"name":"Play without crafting stone tools.", "difficulty":0.12, "weight":71.2},
    {"name":"Play without getting `Diamonds` advancement.", "difficulty":0.08, "weight":200.4},
    {"name":"Brew a potion of strength.", "difficulty":1.5, "weight":1921.8},
    {"name":"Get a potion of speed during the run.", "difficulty":1.4, "weight":1808.7},
    {"name":"Don't get `Acquire Hardware` advancement before entering the nether.", "difficulty":0.25, "weight":452.3},
    {"name":"Get `Fishy Business` advancement during the run.", "difficulty":0.13, "weight":761.5},
    {"name":"Get `Tactical Fishing` advancement during the run.", "difficulty":0.15, "weight":406.9},
    {"name":"Get `A Seedy Place` advancement during the run.", "difficulty":0.08, "weight":659.4},
    {"name":"Get `You Need A Mint` advancement during the run.", "difficulty":0.1, "weight":722.5},
    {"name":"Get `Remote Getaway` advancement during the run.", "difficulty":0.6, "weight":846.6},
    {"name":"Get `Getting an Upgrade` advancement while being in the end.", "difficulty":0.11, "weight":78.6},
    {"name":"Get `A Seedy Place` advancement while being in the nether.", "difficulty":0.12, "weight":412},
    {"name":"Get `A Seedy Place` advancement while being in the end.", "difficulty":0.13, "weight":311.5},
    {"name":"Get `Best Friends Forever` advancement during the run.", "difficulty":0.42, "weight":132.9},
    {"name":"Get `This Boat Has Legs` advancement during the run.", "difficulty":0.9, "weight":102.5},
    {"name":"Get `Bullseye` advancement during the run.", "difficulty":1.5, "weight":435.6},
    {"name":"Get `Getting an Upgrade` advancement during the run without getting `Stone Age` before this.", "difficulty":0.22, "weight":118.4},
    {"name":"Get `Sniper Duel` advancement during the run.", "difficulty":1.7, "weight":105},
    {"name":"Don't get `Into Fire` advancement during the run.", "difficulty":0.74, "weight":1076.9},
    {"name":"Get `The Next Generation` advancement during the run.", "difficulty":0.1, "weight":812.8},
    {"name":"Get `Getting an Upgrade` advancement while being in the bastion.", "difficulty":0.09, "weight":151.9},
    {"name":"Get `Local Brewing` advancement during the run.", "difficulty":0.2, "weight":330.3}
]


# Shuffle the list of challenges
random.shuffle(challenges)

q = 1

# Generate a random set of non-repeating challenges for each match
while q > random.uniform(0,1):
    match_challenges = []
    match_difficulty = 0

    # Randomly select non-repeating challenges until the total difficulty is reached
    while match_difficulty < min_difficulty:
        # Get a list of challenges that haven't been selected before
        available_challenges = [c for c in challenges if c["name"] not in match_challenges]
        
        # Select a random challenge based on the challenge weights
        weights = [c["weight"] for c in available_challenges]
        idx = random.choices(range(len(available_challenges)), weights=weights)[0]
        challenge = available_challenges[idx]
        
        # Add the challenge to the match
        match_challenges.append(challenge["name"])
        match_difficulty += challenge["difficulty"]
    
    q = 12*((log(ideal_difficulty/match_difficulty,2))**2)


# Print the challenges for the match
for match_challenge in match_challenges:
    print(match_challenge)

