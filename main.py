import random
from time import sleep

Pokedex = []
xp = 0
fruit = 5
energy = 100

def selectPokemon():
    print("Welcome to the world of Pokemon, as a new trainer you can only choose one pokemon. But first, you must choose your name:")
    name = input("Enter your name: ")
    print("Hello " + name + ", you must now choose your pokemon! Take a look at the list below and choose wisely as this will be your only pokemon for now.")
    print("1. Charmander")
    print("2. Squirtle")
    print("3. Bulbasaur")
    pokemon = int(input("Select your pokemon: "))
    if pokemon == 1:
        print("You have selected Charmander, great choice!") #■
        print("Charmander is a fire type pokemon, it is weak against water and strong against grass. An interesting fact about charmander is that")
        print("it can evolve into 3 different pokemon, Charmeleon, Charizard and Mega Charizard X.")
        print("Your charmander is currently: Level 1, it has 20 hp and 10 Attack.")
        Pokedex.append("Charmander")
    elif pokemon == 2:
        print("You have selected Squirtle, interesting choice!")
        print("Squirtle is a water type pokemon, it is weak against grass and strong against fire. An interesting fact about squirtle is that")
        print('it can evolve into 3 different pokemon, Wartortle, Blastoise and Mega Blastoise.')
        print('Your squirtle is currently: Level 1, it has 20 hp and 10 Attack.')
        Pokedex.append("Squirtle")
    elif pokemon == 3:
        print("You have selected Bulbasaur, good choice!")
        print("Bulbasaur is a grass type pokemon, it is weak against fire and strong against water. An interesting fact about bulbasaur is that")
        print("it can evolve into 3 different pokemon, Ivysaur, Venusaur and Mega Venusaur.")
        print('Your bulbasaur is currently: Level 1, it has 20 hp and 10 Attack.')
        Pokedex.append("Bulbasaur")
    else:
        print("Invalid option, please try again")

def getCapturedPokemon():
    global xp
    pokemonCaptured = getRandomPokemon()
    print("You have captured a " + pokemonCaptured + " and gained 100 xp!")
    Pokedex.append(pokemonCaptured)
    print("This is what your Pokedex looks like: ", Pokedex)
    xp += 100

def getRandomPokemon():
    randomPokemon = random.randint(1, 9)
    if randomPokemon == 1:
        pokemonCaptured = "Eevee"
    elif randomPokemon == 2:
        pokemonCaptured = "Pikachu"
    elif randomPokemon == 3:
        pokemonCaptured = "Onix"
    elif randomPokemon == 4:
        pokemonCaptured = "Meowth"
    elif randomPokemon == 5:
        pokemonCaptured = "Pysduck"
    elif randomPokemon == 6:
        pokemonCaptured = "Cubeone"
    elif randomPokemon == 7:
        pokemonCaptured = "Togepi"
    elif randomPokemon == 8:
        pokemonCaptured = "Turtwig"
    elif randomPokemon == 9:
        pokemonCaptured = "Pigeon"
    return pokemonCaptured

def eatFruit():
    global fruit
    global energy
    if fruit > 0:
        print("You are eating fruit...")
        sleep(2)
        fruit -= 1
        energy += 10
    else:
        print("You have no fruit")

def goSleep():
    global energy
    print('Your are sleeping')
    sleep(15)
    energy = 20
    print('You have regained 20 energy!')

def actions():
        global fruit
        global energy
        global xp
        print(" 1. Fight\n 2. Run\n 3. Eat fruit\n 4. Rest\n 5. Check Energy\n 6. Check Fruit\n 7. Check XP")
        option = int(input("Select an option: "))
        if option == 1:
            combat() 
        elif option == 2:
            print("You are running")
            explore()
        elif option == 3:
            eatFruit()
        elif option == 4:
            print("You are resting...")
            sleep(15)
            energy += 10
            explore()
        elif option == 5:
            print("Your energy is: ", energy)
            explore()
        elif option == 6:
            print("You have", fruit, "fruit")
            explore()
        elif option == 7:
            print("Your XP is: ", xp)
            explore()
        else:
            print("Invalid option")
            explore()   

def combat():
    global energy
    print("You have engaged in combat with a wild pokemon!")
    winningOdds = random.randint(1, 2)
    if winningOdds == 1:
        getCapturedPokemon()
        explore()
    elif winningOdds == 2:
        print("You have lost the battle, run away!")
        energy -= 10
        explore()

def choosePokemon():
    print('Here is what your pokedex currently looks like: ', Pokedex)
    pokedexLength = len(Pokedex)
    if pokedexLength > 1:
        print('Which pokemon would you like to use?')
        for i in range(0, pokedexLength):
            print(i, Pokedex[i])
        pokemonChoice = int(input('Select your pokemon: '))
        for i in range (0, pokedexLength):
            if pokemonChoice == i:
                print('You have selected', Pokedex[i])
                print('You are now fighting a wild pokemon with', Pokedex[i])
                i += 1

def explore():
    global energy
    global fruit
    if energy > 0:
        print("You are exploring the wild")
        print("You have found a wild pokemon")
        choosePokemon()
        actions()
    else:
        print("You have no energy left, you must rest or eat a fruit to regain energy. You will be able to explore again in 15 seconds if you sleep.")
        option = int(input("1. Rest\n2. Eat a fruit\nSelect an option: "))
        if option == 1:
            goSleep()
            explore()
        elif option == 2:
            eatFruit()
            explore()
        else:
            print("Invalid option")
selectPokemon()
explore()
