# tic-tac-toe-game-using-python-
this is a simple python file which has a logic to mimic the tic tac toe using list concept 

----------------------------------------
lets see how the python logic is written
----------------------------------------

at first i have printed the name of the game 

> then we have declared 3 list a,b and c, with 3 empty values in each list,and print the lists which is a mimic of tictactoe board

> as the board is 3x3
          -----------------------------
          | row/col |  1  |  2  |  3  |
          -----------------------------
          |    1    |     |     |     | (list a)
          -----------------------------
          |    2    |     |     |     | (list b)
          -----------------------------
          |    3    |     |     |     | (list c)
          -----------------------------
> above is representation of board the empty boxes where we can enter values as x and o
> in output you will only get the below one
          ['','','']
          ['','','']
          ['','','']
> here every row is a separate list row0-->lista, row1->listb, row2--.listc
> then i have declared a while loop (as while loop are used when we do not know the exact itirations that we need to perform for a program)

> then i have declared 3 variables player(which accepts user input string), row(accepts row num) and col accepts col num
> we have main condition to check the character user enters it should be only x or o, so we will check the condition before we insert the value into the board, if the character is not == x or o then we will display the error message but we will not break the loop so that game can be continued
> then we have a if condition to check the entered value from the user for row and column should not exceed number 2, as the index of list starts from 0 and we have a 3x3 board we can only give 0,1,2 for rows and 0,1,2 for columns. if this condition fails we will display retry with some error message.
> as you are observing we are not breaking the loop anywhere here so if once the game starts you need to complete it or terminate the program to start a new game.
> after every condition we have 2 other condition to check that if x or o wins display the winning player and terminate the loop to end the game. For this we have 8 conditions to check for each character x and o, winning combination are horizontal line matching(3 possible combination), vertical line matching(3 possible combination) and diagonal line matching(2 possible combination) these combination to be checked for both x and o for each itiration to know the winner and end the game
