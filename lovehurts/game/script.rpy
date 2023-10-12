# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.menu_include_disabled = True
define h = Character("Paati",  who_color="#c8ffc8")
define p = Character("You")
default char = "Deer"
# The game starts here.

    
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene intro1
    
    "You are Dori, an explorer who is mentored by Paati, the Great Wizard of the Forest. "

    extend "\nYour last adventure was 3 months ago and you are restless to go back into the forest and explore."

    "Paati has invited you for chai. This means that a new adventure is coming up!"
    
    extend "\nAs always, Paati greets you with hot masala chai"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show wizfront1:
        xpos 0.5 ypos 0.3

    # These display lines of dialogue.

    h "Welcome, young one."
    extend "\nSit, relax, drink."
    extend "\nI am glad to see you are well"

    h "You seem restless - is there something on your mind?
    "
    menu:
        "How would you like to respond?"
        "I want to share my thoughts and emotions openly.":
        
            jump express

        "I should probably keep this to myself.":
        
            jump repress

label express:
    hide wizfront1
    show wiz2:
        xpos 0.6 ypos 0.4

    show langurrt2:
        xpos 0.1 ypos 0.3
    "You take a deep breath and relax your body."
    
    p "On my last adventure, I had fun and collected so many different objects...but I felt lonely."
    
    h "Ah yes...adventuring can be lonely. Many explorers get lost in the forest when they try to do everything alone." 

    p "I tried to use the tools and advice you gave me, Paati. But it wasn’t easy. "

    h "Yes...the forest is not an easy place to explore. Why don’t you take someone with you on the next adventure?"

    p "Paati..you know me so well. \n\nI met someone special recently...and I think I will ask them to join me."
    
    h "Yes"

    hide langurrt2

    jump charSelect

$ strength = 0
label repress:

    hide wizfront1
    show wiz2:
        xpos 0.6 ypos 0.4


    show langurriver1:
        xpos 0 ypos 0.2
    
    "You feel your chest tighten and you wonder how your response will be perceived. You play it cool."


    p "It was alright - you know how adventuring can be. \nI’ve made it back, though, and I got you these cool trinkets. "

    h "I am sensing some resistance, young one. Would you like to tell me more?"
    
    hide langurriver1
    
    show langurworried:
        xpos 0.1 ypos 0.2

    "Sometimes, it is hard to be vulnerable with those closest to us."

    p "I just don’t see the point. There’s no use whining like a baby. It was hard but I did it. Sometimes you just have to suck it up."

    h "There is no shame in acknowledging the hardship of your journey. I will always be proud of you. "

    hide langurworried

    show langurthinking:
        xpos 0.1 ypos 0.2

    "You let out a sigh and sink deeper into the chair. Sometimes it’s harder to pretend."

    p "If I’m being honest, I had a hard time. Mostly with loneliness. There were many times I wished I had someone with me - to share the experience with."

    h "Companionship is a wonderful thing to want, young one. Joy shared is joy doubled, as they say.On your next adventure, will you be going with someone? Have you met anyone interesting? "

    hide langurthinking

    show langurempathetic:
        xpos 0.1 ypos 0.2

    p "Thank you, elder one. I tried to use the tools and advice you gave me. Yes, I will be going with someone. I met another adventurer recently. We share a lot of interests and I enjoy spending time with them. "

    h "That’s wonderful news! What’s their name and tell me more!"

    hide langurempathetic

    jump charSelect


label charSelect:
    hide wiz2

    show langurthinking:
        xpos 0.1 ypos 0.3
    
    $ strength = False

    menu:
        "Hiran, The Romantic":
            jump deerStory
        
        "Khaang, The Confident" if strength:
            jump endStory

        "Ullu, The Observant" if strength:
            jump endStory


label deerStory:
    scene deerdream
    hide langurthinking
    
    # show langurempathetic:
    #     xpos 0.1 ypos 0.2
    
    # show deerriver:
    #     xpos 0.7 ypos 0.2
    
    p """I met Hiran at an adventurers group in the last town. Even though they are a bit shy, we hit it off immediately! 
    
    We spent a lot of time wandering the town together. They're really attentive and gentle. We found a quiet spot on a nearby hill and had our first kiss under the stars. 
    
    It was magical! I asked them if they would like to go on an adventure - and they said yes!"""

    "You feel the warmth in your cheeks. You’re blushing!"

    scene intro1
    
    show langurrt2:
        xpos 0.1 ypos 0.2
    
    show wiz2:
        xpos 0.6 ypos 0.4

    h "How sweet! Being in love is a nice feeling."

    p "I think so too! I’m excited to go on an adventure with them. Do you have anything for me?"

    h """I think I have just the adventure for you two.

        I must warn you, though, this journey will need courage and communication. 
        
        The terrain can be quite reactive."""
    
    p "I’m intrigued, Paati. What are we traveling through?"

    h "It is known as the Land of Infinite Possibility."

    "You feel the excitement bubble up within you. Another adventure and this time with your crush!"

    show langurrt2:
        xpos 0.2 ypos 0.3

    h "You will journey through a land that changes depending on who travels through it. Legend says, the true nature of your relationship with your partner will be revealed."

    p "What causes it to change?"

    h "Any choice, conversation, or conflict"

    p "That sounds difficult but I’m up for the challenge!"

    h "You and Hiran must walk through the  terrains, collecting tokens at various checkpoints until you reach the Eldest Sage. They are the keeper of some of the deepest wisdom known to us."

    p "Whoa. I’m excited and nervous and thrilled all at the same time. "
    
    hide langurrt2

    hide wiz2
    
    show wizfront1:
        xpos 0.3 ypos 0.4
    
    show localwizblob:
        xpos 0.05 ypos 0.1

    "While things are all upside down in that realm, just know that help is never too far away. Click on the objects to learn more"

    call screen buttons2

    "extra"

    "extra 2"

    return

screen buttons2():
    imagebutton:
        xalign 0.9
        yalign 0.35
        auto "bagbutton_%s.png" action [ToggleScreen("buttons2"), Jump("postbag")]

label postbag:
    hide localwizblob

    show langurrt2:
        xpos 0.1 ypos 0.3

    hide wizfront1
    show wiz2:
        xpos 0.55 ypos 0.4
    
    h "And lastly you will always have us, your friends and family waiting for you back home. Go on then."

    p "I can’t wait. Hiran is on their way to the Tower too. Let’s start packing!"

    "Paati hands you a brand new satchel. The material is sturdier and it is filled with items!"

    h "Take a good look, young one."

    jump chap1
    
    "extra"

    "extra 2"


label chap1:
    hide langurrt2
    hide wiz2
    scene abundantforest

    show chap1title:
        xpos 0.25 ypos 0.3
    
    ""

    return


label endStory:
    "story end"
    return



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




