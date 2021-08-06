import random
import secrets

az_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphebet_pick = secrets.choice(az_list)
capitalize_letter = random.getrandbits(1)
if capitalize_letter == True:
    alphebet_pick = alphebet_pick.capitalize()
elif capitalize_letter == False:
    alphebet_pick = alphebet_pick
print(capitalize_letter)
print(alphebet_pick)
