# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Home Wizard")
default char = "Deer"
# The game starts here.

screen buttons():
    imagebutton:
        xalign 0.3
        yalign 0.8
        # FactorScale 
        auto "waterbuff_%s.png" action [ToggleScreen("buttons"), Jump("b1_label")]
    
    imagebutton:
        xalign 0.7
        yalign 0.2
        auto "waterbuff_%s.png" action [ToggleScreen("buttons"), Jump("b2_label")]
    
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg1
    
    "You have found yourself in the Wizard’s Tower again, having returned from another one of your adventures. Your pack is heavy with souvenirs and you have many stories you are excited to share with your mentor. "
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show waterbuff

    # These display lines of dialogue.

    h "Come, come, young one. Make yourself comfortable."

    h "Now tell me."
    menu:
        h "Now tell me."
        "Tell him it was all good and show him souvenirs.":
        
            jump intro

        "Tell him you’re ready for your next assignment.":
        
            jump intro

        "Tell him it was gratifying, but hard to do alone.":
        
            jump forest


label intro:

    scene bg2
    
    "intro here"

    "intro choice"
    menu:
        "intro choice"
        "Deer":
            $ char = "Deer"
            jump forest
        
        "Wolf":
            $ char = "Wolf"
            jump forest

label forest:
    scene forestbg
    if char == "Deer":
        "deer dialogue 1"
        
        show deer

        "deer d2"

        show deer:
            easein 0.9 xpos 0.2
        show pc:
            xpos 1.2
            easein 0.9 xpos 0.7

        "deer d3"

    if char == "Wolf":
        "wolf dialogue 1"
    
        show wolf1
    
    call screen buttons

label b1_label:
    "b1 pressed endddd"
    # This ends the game.

    return

label b2_label:
    "b2 pressed endddd"
    # This ends the game.

    return




