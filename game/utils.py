from os import name, system
import random

def d20():
    # Rolls a D20
    return random.randint(0,20)

def d4():
    # Rolls a D4
    return random.randint(0,4)

def clear_terminal():
    if name == "nt":
        # Windows
        system("cls")
    else:
        # Linux / Mac
        system("clear")