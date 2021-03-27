#ADVENTURE GAME

#Imports 
import time
import random
import pynput 

#Variables
Lvl = ["1"] 
currentLvl = 1 
stuff = []
m1 = 'Tackle' 
m1hp = 25
m2 = 'Tackle'
m2hp = 25
m3 = 'Tackle'
m3hp = 25 
m4 = 'Tackle'
m4hp = 25

#Bools 
bol = True

#Starter
print("--------------------------POKEADVENTURE 2000-------------------------------")
time.sleep(1)
print("LOADING... ") 
time.sleep(0.5)
print("Killing Durb... ") 
time.sleep(0.5)
print("SERVING FRESH DURBAN CURRY... ") 
time.sleep(1)
print("NOTE- Please use small letters when asked for input (except for your name) ")
time.sleep(2) 
print("----------------------------Welcome to the POKEADVENTURE!-----------------------------")
name=input("What is your name?-   ")
print("Hello! Hold on, let me just get the POKESTORE ready...")
time.sleep(3)
print(f"OK, {name} ! LETS BEGIN!!!")
time.sleep(1)
pokemonList = """
---------------------------------POKEMON-----------------------------------------

Squirtle
Charmander
Bulbasaur

(More pokemon will come in a new update.)

-----------------------------------CHOOSE!------------------------------------------
"""
print(f"{pokemonList}")
time.sleep(0.25) 
pokemon=input("Name the pokemon you choose!-   ")
pokemon.lower() 
if pokemon == 'squirtle':
    print("You chose SQUIRTLE! Congrats!")
    currentPokemon = 'Squirtle'
    pokemon = ['Squirtle']
    currentLvl = 1
elif pokemon == 'charmander':
    print("You chose CHARMANDER! Congrats!")
    currentPokemon = 'Charmander'
    pokemon = ['Charmander']
    currentLvl = 1
elif pokemon == 'bulbasaur':
    print("You chose BULBASAUR! Congrats!")
    currentPokemon = 'Bulbasaur'
    pokemon = ['Bulbasaur'] 
    currentLvl = 1
else:
    print("Please restart. DURB has hacked the system... ")
    time.sleep(1) 
    print("PLEASE... ") 
    time.sleep(86400) 
time.sleep(1)
print("Getting out of the POKESHOP...")
time.sleep(3)
#print("OK! Press shift+E, to start!") 
Coins = 100 

#Main part 
while bol == True: #def main(): 
    Coins = Coins 
    currentLvl = currentLvl 
    tips = ["Your level affects the level of your pokemon", "Get some items at the shop", "Purchase move gems, to teach your pokemon new moves"]
    tip = random.choice(tips) 
    print(f"Tip- {tip}. ")
    time.sleep(0.5) 
    cmd=input(f"Where to next, Adventurer {name} ?(Type help for all commands)-   ")
    if cmd == 'help':
        cmdList = f"""
---------------------------------------COMMANDS:-------------------------------------
Hello, {name}! 

bag = to see your items
duel = to duel an NPC   
settings = for settings 
shop = to see the pokeshop, where you can get pokeballs, potions, berries, and much more!
stats = to see your stats.
Moves = to see your moves! 

Made by FlameGame001. Not associated with discord. 
----------------------Please give feedback in our GameHub Discord--------------------
 """
        print(f"{cmdList}")
    elif cmd == 'bag':
        print("------------------------------------------Items-------------------------------------")
        if stuff == []:
            print("Items = none.")
        elif stuff != []:
            print(f"1 {stuff[1]}")
            print(f"2 {stuff[2]}")
            print(f"3 {stuff[3]}")
            print(f"4 {stuff[4]}")
            print(f"5 {stuff[5]}")
            print(f"6 {stuff[6]}")
            print(f"7 {stuff[7]}")
            print(f"8 {stuff[8]}")
            print(f"9 {stuff[9]}")
            print(f"10 {stuff[10]}")
            print(f"11 {stuff[11]}")
            print(f"12 {stuff[12]}")
            print(f"13 {stuff[13]}")
            print(f"14 {stuff[14]}")
            print(f"15 {stuff[15]}")
            print(f"16 {stuff[16]}")
            print(f"17 {stuff[17]}")
            print(f"18 {stuff[18]}")
            print(f"19 {stuff[19]}")
            print(f"20 {stuff[20]}")
        use=input("Want to use anything?(NUMBER please)-   ") 
        print("------------------------------------------------------------------------------------")
    elif cmd == 'duel':
        npcNames = ["James", "Archie", "Sally", "Sam", "Anne", "Ash", "MrNoob2029", "DaProYo", "Xenrez", "Batman", "Tiffy3000", "Purple_Pastelz", "MrBeast", "Korean1003", "ThisGamerInfo", "Hi104334", "MrMoney500"]   
        npcPokemon = ["Squirtle", "Charmander", "Bulbasaur", "Charmelon", "Wartortle", "Ivysaur", "Pikachu", "Shinx", "Kygore", "Groundon", "Mew", "Mewtwo"]
        npcMoves = ["Tackle", "Leer", "Ash Punch", "Weed Whacker", "Fireball", "Squirt", "Earthquake", "Overdrive", "Cloud Swish", "Power Punch", "Blizzard", "Kicker"] 
        chosen = random.choice(npcNames)
        chosenPokemon = random.choice(npcPokemon) 
        print(f"{chosen} wants to BATTLE you!")
        time.sleep(1)
        hp = 100+(currentLvl*10) 
        ohp = random.randint(100, 500) 
        print(f"{currentPokemon} VS {chosenPokemon} !")
        while hp != 0 and ohp != 0:
            print (f"{currentPokemon}- {hp} hp... ")
            print (f"{chosenPokemon}- {ohp} hp... ")
            move=input("Move number?(1, 2, 3 or 4)-   ")
            if move == 1:
                print(f"{currentPokemon}, use {m1}! ")
                ohp = ohp-m1hp 
            elif move == 2:
                print(f"{currentPokemon}, use {m2}! ")
                ohp = ohp-m2hp 
            elif move == 3:
                print(f"{currentPokemon}, use {m3}! ")
                ohp = ohp-m3hp 
            elif move == 4:
                print(f"{currentPokemon}, use {m4}! ")
                ohp = ohp-m4hp 
            time.sleep(1)
            chosenMove = random.choice(npcMoves)
            chosenHP = random.randint(10, 100)
            print(f"Opponent- {chosenPokemon}, use {chosenMove} !") 
            hp = hp-chosenHP
        if hp <= 0:
            print("Too bad! You lost... ")
            newLvl = currentLvl+1
            time.sleep(0.5) 
            print(f"You are on LVL{newLvl} !")
            currentLvl = newLvl
            newLvl = 0
        elif ohp <= 0:
            print("Congrats! You WON!!! ")
            update = random.randint(2, 10)
            newLvl = currentLvl+update
            time.sleep(0.5) 
            print(f"You are on LVL{newLvl} !")
            currentLvl = newLvl
            newLvl = 0
    elif cmd == 'stats':
        hp = 100+(currentLvl*10)
        statuses = f'''
------------------------------------STATS---------------------------------------

Name- {name}
PokeCoins- {Coins}$ 
Current Pokemon- {currentPokemon}
Current Level OF POKEMON- {currentLvl} 
Current HP OF POKEMON- {hp}

(ORDER- match your order with pokemon. EG- pokemon2 is bulbasaur, and lvl2 is 25)

Pokemon (Ordered)-
{pokemon} 

Pokemon Levels (In order of pokemon) 
{currentLvl}

To calculate HP, see level multiplied by 10, plus 100...

------------------------------ {Coins} Coins -----------------------------------
'''
        print(f"{statuses}")

    elif cmd == 'shop':
        shopStuff = f'''
------------------------------------SHOP----------------------------------------

Welcome back, {name}! 

Items: 

STONES 
BATTLE BOOSTS
GENERAL 
CANDY
MISC 

Coins- {Coins}

--------------------------------------------------------------------------------
'''
        print(f"{shopStuff}")
        section=input("Which section would you like to buy from?-   ")
        if section == 'stones':
            stoneSec = f'''
---------------------------------------STONES-----------------------------------

POWER STONE- Increases your pokemon's level to the max level, 100!
COST- 5000$

BABY STONE- Resests your pokemon
COST- 1000$

LEARN STONE- Learn a new move!
COST- 100$

----------------------------------COINS- {Coins}--------------------------------
'''
            print(f"{stoneSec}")
            buy=input("Put the name of the stone (ALL LOWERCASE) to buy one.")
            if buy == 'baby stone':
                if coins > 1000: 
                    stuff.append('1x Baby Stone')
                    coins = coins-1000 
                    print("Success! Check it out in your bag! ") 
                else: 
                    print("INSUFFICENT FUNDS") 
            elif buy == 'power stone':
                if coins > 5000: 
                    stuff.append('1x Power Stone')
                    coins = coins-5000
                    print("Success! Check it out in your bag! ") 
                else: 
                    print("INSUFFICENT FUNDS") 
            elif buy == 'learn stone':
                if coins > 100: 
                    stuff.append('1x Learn Stone')
                    coins = coins-100 
                    print("Success! Check it out in your bag! ") 
                else: 
                    print("INSUFFICENT FUNDS") 
            else: 
                print("Did ya type it in right???") 
        elif section == 'battle boosts': 
            BatSec = f""" 
-------------------------Battle Boosts---------------------------------

ENERGY STONE- Makes your pokemon attacks double the power! 
COST- 5000 

SHEILD STONE- Makes your pokemon HP double! 
COST- 7500 

MORE COMING SOON! 

------------------------ {Coins} coins --------------------------------
""" 
            print(f"{BatSec}") 
            buy=input("Want to buy anything?(LOWERCASE ONLY)-   ") 
            if buy == 'shield stone': 
                stuff.append('Shield Stone') 
                Coins = Coins - 7500 
                print("SUCCESS! Check it out on your bag!") 
            elif buy == 'energy stone': 
                stuff.append('Energy Stone') 
                Coins = Coins - 5000 
                print("SUCCESS! Check it out on your bag!") 
            else: 
                print("Did ya type it in right? ") 
        elif section == 'general': 
            gen = f''' 
----------------------------- GENERAL ---------------------------

Candy- Increase your pokemon's level by 1! 
COST- 100 

Rare Candy- Increase your pokemon's level by 10! 
COST- 1000 

Random Eggy- Gives you a random pokemon! 
COST- 2000

Rare Eggy- Gives you an EX, with level 50! 
COST- 5000 

------------------------- {Coins} Coins --------------------------- 
''' 
            print(f"{gen}") 
            






            
            
