#!/usr/bin/python3

pets = ["dog", "cat", "goldfish", "dog", "cat"]

print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)