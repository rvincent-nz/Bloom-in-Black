# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Brooke")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Brooke happy

    # These display lines of dialogue.

    b "It’s going to snow tomorrow, or at least it’s very likely."
    b "Either I’m going to be stuck in my room, cycling in heat from d’6 and trying to study,
    or I’m going to be out in the cold helping shovel snow,
    followed by being stuck in my room, only now I’m wet and tired."
    b "So, this is the driving question for tonight:"
    b "What am I going to do…"

menu:

    "Let's go to the campus cafe.":
        jump cafe

    "Let's just get high.":
        jump end_high

label cafe:

    "Placeholder."

label end_high:

    "420"
    # This ends the game.

    return
