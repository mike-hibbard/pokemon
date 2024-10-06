"""
 A command line game for catching pokemon
"""


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


print("hey")