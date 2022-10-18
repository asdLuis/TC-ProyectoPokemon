from time import sleep
import random

Pokedex = []
chosen_pokemon = 0
# Create a matrix with the pokemons and their stats
pokemon_list = [
    ["Pikachu", 200, 5, "Electric", 0],
    ["Charmander", 200, 5, "Fire", 0],
    ["Squirtle", 200, 5, "Water", 0],
    ["Bulbasaur", 200, 5, "Grass", 0],
    ["Pidgey", 200, 5, "Flying", 0],
    ["Rattata", 200, 5, "Normal", 0],
    ["Caterpie", 200, 5, "Bug", 0],
    ["Weedle", 200, 5, "Bug", 0],
    ["Pidgeotto", 200, 5, "Flying", 0],
    ["Pidgeot", 200, 5, "Flying", 0],
    ["Raticate", 200, 5, "Normal", 0],
    ["Spearow", 200, 5, "Flying", 0],
    ["Fearow", 200, 5, "Flying", 0],
    ["Ekans", 200, 5, "Poison", 0],
    ["Arbok", 200, 5, "Poison", 0],
    ["Pikachu", 200, 5, "Electric", 0],
    ["Raichu", 200, 5, "Electric", 0],
    ["Sandshrew", 200, 5, "Ground", 0],
    ["Sandslash", 200, 5, "Ground", 0],
    ["Nidoran", 200, 5, "Poison", 0],
    ["Nidorina", 200, 5, "Poison", 0],
    ["Nidoqueen", 200, 5, "Poison", 0],
    ["Nidoran", 200, 5, "Poison", 0],
    ["Nidorino", 200, 5, "Poison", 0],
    ["Nidoking", 200, 5, "Poison", 0],
    ["Clefairy", 200, 5, "Fairy", 0],
    ["Clefable", 200, 5, "Fairy", 0],
    ["Vulpix", 200, 5, "Fire", 0],
    ["Ninetales", 200, 5, "Fire", 0],
    ["Jigglypuff", 200, 5, "Fairy", 0],
    ["Wigglytuff", 200, 5, "Fairy", 0],
    ["Zubat", 200, 5, "Poison", 0],
    ["Golbat", 200, 5, "Poison", 0],
    ["Oddish", 200, 5, "Grass", 0],
    ["Gloom", 200, 5, "Grass", 0],
    ["Vileplume", 200, 5, "Grass", 0],
    ["Paras", 200, 5, "Bug", 0],
    ["Parasect", 200, 5, "Bug", 0],
    ["Venonat", 200, 5, "Bug", 0],
    ["Venomoth", 200, 5, "Bug", 0],
    ["Diglett", 200, 5, "Ground", 0],
    ["Dugtrio", 200, 5, "Ground", 0],
    ]

# Initialize the player's stats
xp = 0
fruit = 5
energy = 100

print("    ____             __                                                   __") 
sleep(0.35)                                           
print("   /\  _`\          /\ \                                                 /\ \ ") 
sleep(0.35)                                         
print("   \ \ \L\ \  ___   \ \ \/'\        __      ___ ___       ___     ___    \ \ \ ")
sleep(0.35)      
print("    \ \ ,__/ / __`\  \ \ , <      /'__`\  /' __` __`\    / __`\ /' _ `\   \ \ \ ") 
sleep(0.35)   
print("     \ \ \/ /\ \L\ \  \ \  \`\   /\  __/  /\ \/\ \/\ \  /\ \L\ \/\ \/\ \   \ \_\  ")
sleep(0.35)    
print("      \ \_\ \ \____/   \ \_\ \_\ \ \____\ \ \_\ \_\ \_\ \ \____/\ \_\ \_\   \/\_\ ")
sleep(0.35)    
print("       \/_/  \/___/     \/_/\/_/  \/____/  \/_/\/_/\/_/  \/___/  \/_/\/_/    \/_/ \n")
sleep(0.35)   
                                                                
                                                                   
# Welcome the player to the game
print("Welcome to the world of Pokemon, as a new trainer you can only choose one pokemon. But first, you must choose your name:")
name = input("Enter your name: ")

# Choose your pokemon and append to the player's pokedex list
def select_pokemon():
    print("Hello " + name + ", you must now choose your pokemon! Take a look at the list below and choose wisely as this will be your only pokemon for now.")
    print("1. Charmander")
    print("2. Squirtle")
    print("3. Bulbasaur")
    pokemon = int(input("Select your pokemon: "))
    if pokemon == 1:
        print("You have selected Charmander, great choice!") #■
        print("Charmander is a fire type pokemon, it is weak against water and strong against grass. An interesting fact about charmander is that")
        print("it can evolve into 3 different pokemon, Charmeleon, Charizard and Mega Charizard X.")
        print("Your charmander is currently: Level 1, it has 200 hp and 10 Attack.")
        Pokedex.append(["Charmander", 200, 10, "Fire"])
    elif pokemon == 2:
        print("You have selected Squirtle, interesting choice!")
        print("Squirtle is a water type pokemon, it is weak against grass and strong against fire. An interesting fact about squirtle is that")
        print('it can evolve into 3 different pokemon, Wartortle, Blastoise and Mega Blastoise.')
        print('Your squirtle is currently: Level 1, it has 200 hp and 10 Attack.')
        Pokedex.append(["Squirtle", 200, 10, "Water"])
    elif pokemon == 3:
        print("You have selected Bulbasaur, good choice!")
        print("Wtf are you ok bro? Who chooses bulbasaur lol")
        print('Your bulbasaur is currently: Level 1, it has 200 hp and 10 Attack.')
        Pokedex.append(["Bulbasaur", 200, 10, "Grass"])
    else:
        print("Invalid option, please try again")
        select_pokemon()
    explore()
# When you capture a pokemon, send a message to the player
def get_random_pokemon(): 
     # Chooses a random pokemon from the list
    random_pokemon = random.choice(pokemon_list)
    return random_pokemon

#Eat fruit
def eat_fruit():
    global fruit
    global energy
    if fruit > 0:
        print("You are eating fruit...")
        sleep(2)
        fruit -= 1
        energy += 10
    else:
        print("You have no fruit")
    explore()

# Sleep in oder to restore energy
def go_sleep():
    global energy
    print('Your are sleeping')
    sleep(15)
    energy = 15
    print('You have regained 200 energy!')

# Give the player their options
def actions():
        # Use the global variables for stats
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
            eat_fruit()
        elif option == 4:
            confirm_home()
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

# Fight a random pokemon, not complete yet
def combat():
    global energy
    global xp
    global chosen_pokemon
    global fruit
    print("You have engaged in combat with a wild pokemon!")
    pokemon = get_random_pokemon()
    print("You are fighting a", pokemon[0], 'it has', pokemon[1], 'hp and', pokemon[2], 'attack and is a', pokemon[3], 'type pokemon')
    print("Choose your pokemon:")
    chosen_pokemon = choose_pokemon()
    print("You have chosen", chosen_pokemon[0], 'it has', chosen_pokemon[1], 'hp and', chosen_pokemon[2], 'attack and is a', chosen_pokemon[3], 'type pokemon')
    while pokemon[1] >= 0 and chosen_pokemon[1] >= 0:
        option = int(input("Select an option:\n 1. Attack\n 2. Run\n"))
        if option == 1:
            if pokemon[1] > 0 and chosen_pokemon[1] > 0:
                critical_user = random.randint(1, 5)
                damage_user = critical_user * chosen_pokemon[2]
                damage_pokemon = critical_user * pokemon[2]
                print("You are attacking...")
                sleep(2)
                if critical_user > 4:
                    print("Critical hit! You dealt", critical_user, "times more damage!")
                    sleep(2)
                pokemon[1] -= damage_user
                print("You dealt", damage_user, "damage!")
                sleep(2)
                print(pokemon[0], "has", pokemon[1], "hp left")
                sleep(2)
                if pokemon[1] <= 0:
                    print("You have defeated the pokemon!")
                    sleep(2)
                    print("You have successfully captured the", pokemon[0])
                    Pokedex.append(pokemon)
                    sleep(2)
                    print("You and your pokemon have gained 10 xp")
                    xp += 10
                    chosen_pokemon[4] += 10
                    print("Your pokemon needs 100 xp to level up")
                    explore()
                critical_user = random.randint(1, 5)
                print(pokemon[0], "is attacking...")
                dodge(pokemon, damage_pokemon, critical_user)
                sleep(2)
                if chosen_pokemon[1] <= 0:
                    print("You have been defeated!")
                    explore()
        elif option == 2:
            print("You are running")
            explore()
        else:
            print("Invalid option")
            combat()
    print("You have captured a " + pokemon[0] + " and gained 100 xp!")
    Pokedex.append(pokemon)
    print("This is what your Pokedex looks like: ", Pokedex)
    xp += 100

# Dodge function when a pokemon attacks you
def dodge(pokemon, damage_pokemon, critical_user):
    global chosen_pokemon
    option = int(input("Watch out! The enemy pokemon is attacking! If you dodge incorrectly you will recieve 2x more damage, do you want to dodge?\n 1. Yes\n 2. No\n"))
    dodge_chance = random.randint(1, 10)
    if option == 1:
        if dodge_chance > 5:
            print("You have dodged the attack and negated the damage!")
        else:
            print("You have been hit and recieved x2 more damage!")
            chosen_pokemon[1] -= damage_pokemon * 2
            sleep(2)
            print("You recieved", damage_pokemon * 2, "damage!")
            print("Your", chosen_pokemon[0], "has", chosen_pokemon[1], "hp left")
    elif option == 2:
        if critical_user > 4:
                print("Critical hit! You've been dealt", critical_user, "times more damage!")
                print("You recieved", damage_pokemon, "damage!")
                chosen_pokemon[1] -= damage_pokemon
        else:
            chosen_pokemon[1] -= damage_pokemon * pokemon[2]
            print("You recieved", damage_pokemon, "damage!")
        sleep(2)
        print("Your", chosen_pokemon[0], "has", chosen_pokemon[1], "hp left") 
        
    else:
        print("Invalid option")
        dodge(pokemon, damage_pokemon, critical_user)


# Confirm if the player wants to go home
def confirm_home():
    print('You will need to go home to rest and regain energy.')
    home_option = int(input('Do you want to go home? \n1. Yes \n2. No\n'))
    if home_option == 1:
        print('You just arrived home! You can now check your Pokedex, select your pokemon, or go to sleep.')
        returnHome()
    elif home_option == 2:
        if energy > 0:
            print('You have enough energy to continue exploring!')
            explore()
        else:
            tired()

# Display the player's Pokedex and allow them to select a pokemon based on the index number and size of the Pokedex   
def choose_pokemon():
    for i in range(len(Pokedex)):
        print(i+1 , Pokedex[i])
    pokemon = int(input("Select your pokemon: "))
    return Pokedex[pokemon-1]

# Return home to check your Pokedex, select a pokemon, or go to sleep
def returnHome():
    print('1. Check Pokedex\n2. Select a Pokemon\n3. Go to sleep\n4. Go back to exploring')
    home_option = int(input('Select an option: '))
    if home_option == 1:
        print('Here is what your Pokedex looks like: ', Pokedex)
        returnHome()
    elif home_option == 2:
        choose_pokemon()
        explore()
    elif home_option == 3:
        go_sleep()
    elif home_option == 4:
        explore()
    else:
        print('Invalid option')
        returnHome()

# If the player is tired, they must go home to regain energy or eat fruit
def tired():
    print("You have no energy left, you must rest or eat a fruit to regain energy.")
    option = int(input("1. Rest\n2. Eat a fruit\nSelect an option: "))
    if option == 1:
        confirm_home()
    elif option == 2:
        eat_fruit()
        explore()
    else:
        print("Invalid option")

# Explore the game, game loop
def explore():
    global energy
    global fruit
    if energy > 0:
        print("You are exploring the wild")
        print("You have found a wild pokemon")
        actions()
    else:
        tired()

# Start the game
select_pokemon()

