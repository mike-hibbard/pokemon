"""
 A command line game for catching pokemon
"""

from pathlib import Path
import csv
import random
import game_art


# Read and extract Pokemon database
path = Path('data/pokemon.csv')

# Parse into a list of lines
lines = path.read_text(encoding='utf-8').splitlines()

# Give the lines list to a reader object
reader = csv.reader(lines)

# Use the next method to (initially) get headers, and assign to a variable.
# By assigning to the variable we can retain the headers...
# - calling next again will yield the first line of data, and so on...
# NOTE: next() is a function NOT a method of reader!
header_row = next(reader)

# prints ['ID','Name','Form','Type1','Type2','Total','HP','Attack','Defense','Sp. Atk','Sp. Def','Speed','Generation']
# print(header_row)

# helps us understand the headers
# for index, column_header in enumerate(header_row):
#   print(index, column_header)

# Extract data from columns by index - just as you would from a list.
# NOTE: reader tracks position in the file - the below works because we extracted
# the headers first, and the start position for row is the first data row, not
# the header row.

# Extract pokemon name, type, total
pokemon_details = []
for row in reader:
    pokemon = (row[1],row[3],row[5])
    pokemon_details.append(pokemon)

# print(pokemon_details[0])

# A function that randomly chooses a pokemon
def Find_Pokemon(pokemon_details):
    
    # Choose a random pokemon in the database
    pokemon = random.choice(pokemon_details)
    # print(pokemon)
    return pokemon

# Test
# Find_Pokemon(pokemon_details)


# Game logic
print(game_art.title)
player = input('\nPlease enter your name: ')

print(f"\n----Welcome {player} - LET'S CATCH SOME POKEMON!----")

# A list of pokemon names caught
pokemon_caught = []

while True:
    
    print("""
      \nChoose an option
          1 = Find a new pokemon
          2 = List all pokemon captured
          3 = Quit game
      """)

    command = input()

    # Quit immediately.
    if command == '3':
        print("\nThanks for playing!")
        print(game_art.charizard)
        break
    
    # Play the game.
    elif command == '1':
        pokemon_found = Find_Pokemon(pokemon_details)
        print(f"\nYou found {pokemon_found[0]}!")

       # Collect only the pokemon's name
        pokemon_caught.append(pokemon_found[0])

    # Print pokemon caught so far
    elif command == '2':
        print("'\nYou have found...")
        for pokemon in pokemon_caught:
            print(pokemon)

    else:
        print("\nIncorrect command.")


"""
 Rules and Game Logic

 1.  Pokemon catch ratings run from 0 (hardest) to 255 (easiest).
 2.  Pokeballs reduce as follows:
        - Pokeball:     -10
        - Great ball:   -20
        - Ultra ball:   -30
 3.  Pokemon actions that further reduce catch ratings:
        - Asleep:       -25
        - Poison:       -25
        - Injure:       -12
        - Confuse;      -12

 There are 1250 Pokemon in total, each with a catch rating.

 A random 1250-Die is thrown to select the Pokemon to catch.

 A random 3-Die is thrown to select the Pokeball.

 A random 6-Die is thrown to select the action
     (1/6 for Asleep and Poison).
     (2/6 for Injure and Confuse).

 Once the final catch-rate is calculated, a final dice roll is used to 
 determine a number > or < than the catch rate.  If LESS THAN, the 
 Pokemon is caught and stored in the database.

"""