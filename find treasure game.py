print(r"""

*****************************************************************************
                                          |
                                          8
                                         / \
                                      ,/'   `\.
                                    ,'`"`"`"`"``.
                                   /             \
         __                       ;               :                       __
        /'`\                  ,db,|               |,db,                  /'`\
       |____|   ,'`.     A   /    :_,_,_,_,_,_,_,_;    \   A     ,'`.   |____|
        |"'|    |__|    A|\_,|`"`"`A`"`"`"`"`"`"`A'`"`"|,_/|A    |__|    |"'|
        J  J    |  |    |`\,A|_____|_____________|_____|A,/'|    |  |    J  J
        |"'|    J`"J    |   |j/|A|\| ,_,_,_,_,_, |/|A|\l|   |    J"'J    |"'|
        |  |    |  |    | _ |  __  | ;   ___   ; |  __  | _ |    |  |    |  |
        F  J    |  |    |/ || /  \ | : ,' _ `. : | /  \ || \|    |  |    F  J
       J"'"'J   F  J    ||_|| |__| | ; |_/_\_| ; | |__| ||_||    F  J   J"'"'J
       |    |  J`"`"J   | _ |  __  | : |`"`"`| : |  __  | _ |   J"'"'J  |    |
       |    |  |    |   |/ || /  \ | ; | / \ | ; | /  \ || \|   |    |  |    |
       F    |__|____|___||_||_|__|_|_:_|_|_|_|_:_|_|__|_||_||___|____|__|    J
      J"'"'"'"'"'"'"'"'"'"'"'"'"'"T"'"'"'"'"'"'"'"T"'"'"'"'"'"'"'"'"'"'"'"'"'"J
      |,^,,^,,^,,^,,^,,^,,^,,^,,^,|,^,^,^,^,^,^,^,|,^,,^,,^,,^,,^,,^,,^,,^,,^,|
     _||_||_||_||_||_||_||_||_||_|||_|_|_|_|_|_|_|||_||_||_||_||_||_||_||_||_||_
    |                             |/ V V V V V V \|                             |
    |_____________________________||_|_|_|_|_|_|_||_____________________________|
                                                                            fsc
**********************************************************************************
""")
print("Welcome to find the way to Tajmahal")
first = input(
    'You\'re at a crossroad ,where do you wanna go: \n Type "left" or "right"\n'
)
if first == "right":
    print("You fell into a hole. Game Over.")
elif first == "left":
    second = input(
        "You've come to a lake. There is an island in the middle of the lake.\nType (wait) to wait for a boat. Type (swim) to swim across.\n"
    )
    if second == "swim":
        print("You got attacked by a shark. Game over")
    elif second == "wait":
        third = input(
            "You arrive at the island unharmed. Now there are 3 doors.\nOne (red), one (yellow) and one (blue). Which colour do you choose?\n"
        )
        if third == "red":
            print("It's a room full of fire. Game Over.")
        elif third == "blue":
            print("You enter a room of beasts. Game Over.")
        elif third == "yellow":
            print("Congrats! you have arrived at the Tajmahal! You Win!")
