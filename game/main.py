# Utility func to clear screen on all platforms
from utils import clear_terminal
from tournament import Tournament
from bull_pen import make_bulls
import sys

# Clear terminal in preparation for game
clear_terminal()

print(
    '''          .=     ,        =.
  _  _   /'/    )\,/,/(_   \ 
   `//-.|  (  ,\\)\//\)\/_  ) |
   //___\   `\\\/\\/\/\\///'  /
,-"~`-._ `"--'_   `"""`  _ \`'"~-,_
\       `-.  '_`.      .'_` \ ,-"~`/
 `.__.-'`/   (-\        /-) |-.__,'
   ||   |     \O)  /^\ (O/  |
   `\\  |         /   `\    /
     \\  \       /      `\ /
      `\\ `-.  /' .---.--.
        `\\/`~(, '()      ('
         /(O) \\   _,.-.,_)
        //  \\ `\'`      /
       / |  ||   `""""~"`
     /'  |__||
           `o'''
)

print('Welcome to Toroledo Bull Fighting!')
player_name = input('Please enter your name: ')

while True:

    selection = input(
        """
Would you like to run a tournament? If yes 
press Y, if no press N.
--> """
    )

    if selection in ('N', 'n', 'No', 'no'):
        clear_terminal()
        print(f'Thank you for playing!\nUntil next time...')
        break

    if selection in ('Y', 'y', 'Yes', 'yes'):
        #Make bulls and set tournament class
        bulls = make_bulls()
        tournament = Tournament(bulls)
        clear_terminal()
        print(tournament.make_bracket())
        print(tournament.elite_eight())
        print(tournament.final_four())
        print(tournament.championship())

    else:
      print('That is not a valid command.')