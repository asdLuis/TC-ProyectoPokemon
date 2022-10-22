# Import time to use sleep function to make the game more realistic and give the user more time to read the text
from time import sleep
# Import random to use randint function to generate random numbers to get random stats throught the game to make it less linear
import random

# Initialize the player's stats
xp = 0
fruit = 5
energy = 100
Pokedex = []
# Inventory = Fruit, Hyper Potion, Full Restore, Pokeball, Super Ball
Inventory = [5, 5, 5, 5, 1]
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
sleep(2)
name = input("Enter your name: ")

# Choose your pokemon and append to the player's pokedex list
def select_pokemon():
    print("Hello " + name + ", you must now choose your pokemon! Take a look at the list below and choose wisely as this will be your only pokemon for now.")
    print("1. Charmander")
    print("2. Squirtle")
    print("3. Bulbasaur")
    pokemon = int(input("Select your pokemon: "))
    if pokemon == 1:
        print("You have selected Charmander, great choice!")
        sleep(2)
        print("Charmander is a fire type pokemon, it is weak against water and strong against grass. An interesting fact about charmander is that")
        print("it can evolve into 3 different pokemon, Charmeleon, Charizard and Mega Charizard X.")
        sleep(3)
        print("Your charmander is currently: Level 1, it has 200 hp and 5 Attack.")
        Pokedex.append(["Charmander", 200, 5, "Fire", 0])
    elif pokemon == 2:
        print("You have selected Squirtle, interesting choice!")
        sleep(2)
        print("Squirtle is a water type pokemon, it is weak against grass and strong against fire. An interesting fact about squirtle is that")
        print('it can evolve into 3 different pokemon, Wartortle, Blastoise and Mega Blastoise.')
        sleep(3)
        print('Your squirtle is currently: Level 1, it has 200 hp and 5 Attack.')
        Pokedex.append(["Squirtle", 200, 5, "Water", 0])
    elif pokemon == 3:
        print("You have selected Bulbasaur, good choice!")
        sleep(2)
        print("Wtf are you ok bro? Who chooses bulbasaur lol")
        sleep(2)
        print('Your bulbasaur is currently: Level 1, it has 200 hp and 5 Attack.')
        Pokedex.append(["Bulbasaur", 200, 5, "Grass", 0])
    else:
        print("Invalid option, please try again")
        select_pokemon()
    explore()
# When you capture a pokemon, send a message to the player
def get_random_pokemon(): 
     # Chooses a random pokemon from the list
    return random.choice(pokemon_list)
    
pokemon = get_random_pokemon()

#Eat fruit
def eat_fruit():
    global Inventory
    global energy
    if Inventory[0] > 0:
        print("You are eating fruit...")
        sleep(2)
        Inventory[0] -= 1
        energy += 10
    else:
        print("You have no fruit")
    explore()

# Sleep in oder to restore energy
def go_sleep():
    global energy
    print('Your are sleeping')
    sleep(15)
    energy += 15
    print('You have regained 15 energy!')

# Give the player their options
def actions():
        # Use the global variables for stats
        global fruit
        global energy
        global xp
        print(" 1. Fight\n 2. Run\n 3. Eat fruit\n 4. Rest\n 5. Check Energy\n 6. Check Inventory")
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
            print(f"Your Inventory is: {Inventory[0]} fruit, {Inventory[1]} hyper potions, {Inventory[2]} full restores {Inventory[3]} pokeballs and {Inventory[4]} superballs")
            use_inventory()
            explore()


def use_inventory():
    choice = int(input("What would you like to do? \n1. Eat a fruit \n2. Use a hyper potion \n3. Use a full restore, \n4. Go back\n"))
    if choice == 1:
        eat_fruit()
    elif choice == 2:
        print("Which pokemon would you like to use it on?")
        for i in range(len(Pokedex)):
            print(f"{i+1}. {Pokedex[i][0]}")
        choice = int(input("Select a pokemon: "))
        if Pokedex[choice-1][1] == 200:
            sleep(2)
            print("This pokemon is already at full health!")
            sleep(2)
            explore()
        else:
            Pokedex[choice-1][1] += 100
            Inventory[1] -= 1
            if Pokedex[choice-1][1] > 200:
                Pokedex[choice-1][1] = 200
            print(f"{Pokedex[choice-1][0]} has been healed by 100 hp!")
            sleep(2)
            explore()
    elif choice == 3:
            print("Which pokemon would you like to use it on?")
            for i in range(len(Pokedex)):
                print(f"{i+1}. {Pokedex[i][0]}")
            choice = int(input("Select a pokemon: "))
            if Pokedex[choice-1][1] >= 200:
                print("This pokemon is already at full health!")
                sleep(2)
                explore()
            else:
                Pokedex[choice-1][1] = 200
                Inventory[2] -= 1
                print(f"{Pokedex[choice-1][0]} has been healed to full health!")
                sleep(2)
                explore()
    elif choice == 4:
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
    global pokemon
    print("You have engaged in combat with a wild pokemon!")
    # Give a description of the pokemon you are fighting
    print("You are fighting a", pokemon[0], 'it has', pokemon[1], 'hp and', pokemon[2], 'attack and is a', pokemon[3], 'type pokemon')
    print("Choose your pokemon:")
    chosen_pokemon = choose_pokemon()
    print("You have chosen", chosen_pokemon[0], 'it has', chosen_pokemon[1], 'hp and', chosen_pokemon[2], 'attack and is a', chosen_pokemon[3], 'type pokemon')
    # While any of the pokemon have hp, continue the fight
    while pokemon[1] > 0 or chosen_pokemon[1] > 0:
        # If the pokemon you are fighting has no hp left, you win
        option = int(input("Select an option:\n 1. Attack\n 2. Run\n"))
        # If the player decides to fight
        if option == 1:
            if pokemon[1] > 0 and chosen_pokemon[1] > 0:
                # Get a random number which will multiply the attack of your pokemon
                critical_user = random.randint(1, 10)
                damage_user = critical_user * chosen_pokemon[2]
                print("You are attacking...")
                sleep(2)
                # If you land a critical hit, the damage will be increased by the amount given
                if critical_user >= 5:
                    print("Critical hit! You dealt", critical_user, "times more damage!")
                    sleep(2)
                # Decrease the hp of the pokemon you are fighting
                pokemon[1] -= damage_user
                print("You dealt", damage_user, "damage!")
                sleep(2)
                print(pokemon[0], "has", pokemon[1], "hp left")
                sleep(2)
                # If the pokemon you are fighting has no hp left, you win and have a chance to capture it
                if pokemon[1] <= 0:
                    print("You have defeated the pokemon!")
                    print("Now it's time to capture it!")
                    # If we have pokeballs allow the play to capture it
                    if Inventory[3] > 0 or Inventory[4] > 0:
                        use_pokeball()
                        break
                    # If we don't have pokeballs, we can't capture it
                    else:
                        print("You don't have any pokeballs!")
                        sleep(2)
                        explore()
                        get_random_pokemon()
                        break
                # If the pokemon you are fighting has hp left, it will attack you
                # Get a random number which will multiply the attack of the enemy pokemon
                print(pokemon[0], "is attacking...")
                sleep(2)
                # Give the user the option to dodge the attack
                dodge()
                # If your pokemon has no hp left, you lose
                if chosen_pokemon[1] <= 0:
                    print("You have been defeated!")
                    sleep(2)
                    print("You have lost 50 energy")
                    energy-= 50
                    # Set your pokemon's hp to 0 so that it doesn't go into the negatives
                    chosen_pokemon[1] = 0
                    # Reset the hp of the pokemon you are fighting
                    pokemon[1] = 200
                    sleep(2)
                    get_random_pokemon()
                    explore()
        # If the player decides to run
        elif option == 2:
            print("You are running")
            sleep(2)
            print("You have wasted 30 energy running away")
            energy -= 30
            # Reset the hp of the pokemon you are fighting
            pokemon[1] = 200
            get_random_pokemon()
            sleep(2)
            explore()
        else:
            print("Invalid option")
            combat()

def dodge():
    global chosen_pokemon
    global pokemon
    critical_pokemon = random.randint(1, 10)
    option = int(input("Watch out! The enemy pokemon is attacking! If you dodge incorrectly you will recieve 2x more damage, do you want to dodge?\n 1. Yes\n 2. No\n"))
    # Get a random number which will determine if you are able to dodge or not the attack
    dodge_chance = random.randint(1, 10)
    if option == 1:
        # If the random number is greater or equal than 5, you will dodge the attack
        if dodge_chance >= 4:
            print("You have dodged the attack and negated the damage!")
        # If the random number is less than 5, you will not dodge the attack and will recieve double the damage
        else:
            print("You have failed to dodge the attack and have recieved double the damage!")
            if critical_pokemon >= 5:
                print("Critical hit! You've been dealt", critical_pokemon * 2, "times more damage!")
                chosen_pokemon[1] -= (pokemon[2] * critical_pokemon) * 2
                sleep(2)
                print("You recieved", (pokemon[2] * critical_pokemon) * 2, "damage!")
                sleep(2)
                print("Your", chosen_pokemon[0], "has", chosen_pokemon[1], "hp left")
            elif critical_pokemon < 5:
                print("You recieved", pokemon[2] * pokemon[2], "damage!")
                chosen_pokemon[1] -= pokemon[2] * pokemon[2]
                sleep(2)
                print("Your", chosen_pokemon[0], "has", chosen_pokemon[1], "hp left")
    # If you choose not to dodge, you will recieve regular damage
    elif option == 2:
        if critical_pokemon >= 5:
                print("Critical hit! You've been dealt", critical_pokemon, "times more damage!")
                print("You recieved", pokemon[2] * critical_pokemon, "damage!")
                chosen_pokemon[1] -= pokemon[2] * critical_pokemon
        else:
            chosen_pokemon[1] -= pokemon[2] * pokemon[2]
            print("You recieved", pokemon[2] * pokemon[2], "damage!")
        sleep(2)
        print("Your", chosen_pokemon[0], "has", chosen_pokemon[1], "hp left")  
    else:
        print("Invalid option")
        sleep(2)
        dodge()

def use_pokeball():
    global xp
    global pokemon
    option = int(input("Select an option:\n 1. Pokeball\n 2. Superball\n 3. Let it go\nSelect an option: "))
    if option == 1:
        if Inventory[3] > 0:
            capture_chance_one = random.randint(1, 10) 
            capture_chance_two = random.randint(1, 10) 
            capture_chance_three = random.randint(1, 10) 
            # First iteraion of the capture chance is 50%
            print ("You have a 50% chance of capturing the pokemon")
            sleep(2)
            print("Attempting to capture...")
            print("✩✩✩")
            sleep(3)
            if capture_chance_one > 5:
                print("Attempting to capture...")
                print("★✩✩")
                sleep(3)
            else:
                print("You have failed to capture the pokemon")
                Inventory[3] -= 1
                pokemon[1] = 200
                sleep(2)
                explore()
            if capture_chance_two > 5:
                print("Attempting to capture...")
                print("★★✩")
                sleep(3)
            else:
                print("You have failed to capture the pokemon")
                Inventory[3] -= 1
                pokemon[1] = 200
                sleep(2)
                explore()
            if capture_chance_three > 5:
                print("Attempting to capture...")
                print("★★★")
                sleep(3)
                print("You have successfully captured the", pokemon[0])
                Pokedex.append(pokemon)
                # Set the hp of the pokemon you are fighting to half its hp after capture
                pokemon[1] = 100
                sleep(2)
                print("You and your pokemon have gained 10 xp")
                xp += 10
                chosen_pokemon[4] += 10
                Inventory[3] -= 1
                get_random_pokemon()
                sleep(2)
                explore()
            else:
                print("You have failed to capture the pokemon")
                Inventory[3] -= 1
                # Reset the hp of the pokemon you are fighting
                pokemon[1] = 200
                sleep(2)
                get_random_pokemon()
                explore()
        else:
            print("You don't have any pokeballs")
            sleep(2)
            use_pokeball()
    elif option == 2:
            capture_chance_one = random.randint(1, 10)
            capture_chance_two = random.randint(1, 10)
            capture_chance_three = random.randint(1, 10)
            # Must obtain more than 8, 3 times in a row to capture the pokemon
            if Inventory[4] > 0:
                print ("You have a 80% chance of capturing the pokemon")
                sleep(2)
                print("Attempting to capture...")
                print("✩✩✩")
                sleep(3)
                # Capture Chance 1
                if capture_chance_one < 8:
                    print("Attempting to capture...")
                    print("★✩✩")
                    sleep(3)
                else:
                    print("You have failed to capture the pokemon")
                    Inventory[4] -= 1
                    pokemon[1] = 200
                    sleep(2)
                    explore()
                # Capture Chance 2
                if capture_chance_two < 8:
                    print("Attempting to capture...")
                    print("★★✩")
                    sleep(3)
                else:
                    print("You have failed to capture the pokemon")
                    Inventory[4] -= 1
                    pokemon[1] = 200
                    sleep(2)
                    explore()
                # Capture Chance 3
                if capture_chance_three < 8:
                    print("Attempting to capture...")
                    print("★★★")
                    sleep(3)
                    print("You have successfully captured the", pokemon[0])
                    Pokedex.append(pokemon)
                    sleep(2)
                    print("You and your pokemon have gained 10 xp")
                    xp += 10
                    chosen_pokemon[4] += 10
                    Inventory[4] -= 1
                    pokemon[1] = 200
                    get_random_pokemon()
                    sleep(2)
                    explore()
                else:
                    print("You have failed to capture the pokemon")
                    Inventory[4] -= 1
                    # Reset the hp of the pokemon you are fighting
                    pokemon[1] = 200
                    get_random_pokemon()
                    sleep(2)
                    explore()
            else:
                print("You don't have any superballs")
                sleep(2)
                use_pokeball()
    elif option == 3:
        print("You have let the pokemon go")
        get_random_pokemon()
        sleep(2)
        explore()
    else:
        print("Invalid option")
        use_pokeball()

# Confirm if the player wants to go home
def confirm_home():
    home_option = int(input('Do you want to go home? \n1. Yes \n2. No\n'))
    if home_option == 1:
        print('You just arrived home! You can now check your Pokedex, select your pokemon, or go to sleep.')
        sleep(2)
        return_home()
    elif home_option == 2:
        if energy > 0:
            print('You have enough energy to continue exploring!')
            sleep(2)
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
def return_home():
    print('1. Check Pokedex\n2. Select a Pokemon\n3. Go to sleep\n4. Go back to exploring')
    sleep(2)
    home_option = int(input('Select an option: '))
    if home_option == 1:
        print('Here is what your Pokedex looks like: ', Pokedex)
        sleep(2)
        return_home()
    elif home_option == 2:
        choose_pokemon()
        sleep(2)
        explore()
    elif home_option == 3:
        go_sleep()
        sleep(2)
    elif home_option == 4:
        explore()
        sleep(2)
    else:
        print('Invalid option')
        return_home()

# If the player is tired, they must go home to regain energy or eat fruit
def tired():
    print("You have no energy left, you must rest or eat a fruit to regain energy.")
    sleep(2)
    option = int(input("1. Rest\n2. Eat a fruit\nSelect an option: "))
    sleep(2)
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
    chance = random.randint(1, 20)
    time_wait = random.randint(1, 15)
    if energy > 0:
        print("Since you have energy, do you want to explore? You have a 2/3 chance of finding a pokemon.")
        sleep(2)
        option = int(input("1. Yes\n2. No\nSelect an option: "))
        if option == 1:
            print("You are exploring the wild...")
            for i in range(time_wait):
                print("... *exploring* ...")
                sleep(1)
            print("... *alert* ...")
            if chance < 7:
                print("You have found a wild pokemon and it is ready to fight!")
                sleep(1)
                combat()
            else:
                print("You found an object! Do you want to pick it up?")
                sleep(1)
                option = int(input("1. Yes\n2. No\n Select an option: "))
                if option == 1:
                    if chance == 8:
                        print("You found a pokeball!")
                        Inventory[3] += 1
                        sleep(1)
                        print("You have", Inventory[3], "pokeballs!")
                        sleep(1)
                        energy -= 3
                    elif chance == 9:
                        print("You found a superball!")
                        Inventory[4] += 1
                        sleep(1)
                        print("You have", Inventory[4], "superballs!")
                        sleep(1)
                        energy -= 3
                    elif chance == 10:
                        print("You found a hyper potion!")
                        Inventory[1] += 1
                        sleep(1)
                        print("You have", Inventory[1], "potions!")
                        sleep(1)
                        energy -= 3
                    elif chance == 11:
                        print("You found a fruit!")
                        Inventory[0] += 1
                        sleep(1)
                        print("You have", Inventory[0], "fruit!")
                        sleep(1)
                        energy -= 3
                    elif chance == 12:
                        print("You found a full restore!")
                        Inventory[2] += 1
                        sleep(1)
                        print("You have", Inventory[2], " full restores!")
                        sleep(1)
                        energy -= 3
                    else:
                        print("Huh, it was just a rock.")
                        sleep(1)
                        energy -= 3
        if option == 2:
            print("You are now headed home")
            sleep(1)
            energy -= 3
            confirm_home() # Eyyyyy, 600 lines!
        explore()       
    else: 
        tired()

# Start the game
select_pokemon()
