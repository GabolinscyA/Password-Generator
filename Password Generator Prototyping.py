import random
import secrets

az_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphebet_pick = secrets.choice(az_list)
capitalize_letter = random.getrandbits(1)
if capitalize_letter == True:
    alphebet_pick = alphebet_pick.capitalize()
elif capitalize_letter == False:
    alphebet_pick = alphebet_pick
print(alphebet_pick)

number_pick = random.randint(0,9)
print(number_pick)

symbol_list = ['`', '~', '!', '@', '$', '#', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '[', '}', ']', '|', '<', ',', '>', '.', '?', '/', ':', ';']
symbol_pick = secrets.choice(symbol_list)
print(symbol_pick)
