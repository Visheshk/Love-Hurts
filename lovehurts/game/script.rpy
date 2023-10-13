﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.menu_include_disabled = True
define h = Character("Paati",  who_color="#c8ffc8")
define p = Character("You")
define dh = Character("Hiran")
define w1 = Character("Wizard Cauwa")
default char = "Deer"
default esteem = 0
default empathy = 0
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

    show wiz playerface:
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
    show wiz doriface:
        xpos 0.6 ypos 0.4

    show langur rightface:
        xpos 0.1 ypos 0.4
        
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

    # hide wizfront1
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
    hide wiz

    show langur thinking:
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
    hide langurthinking
    scene black
    with Dissolve(0.5)
    scene deerdream
    ### FIX DEER DREAM ETC
    with Dissolve(0.5)
    
    # show langurempathetic:
    #     xpos 0.1 ypos 0.2
    
    # show deerriver:
    #     xpos 0.7 ypos 0.2
    
    p """I met Hiran at an adventurers group in the last town. Even though they are a bit shy, we hit it off immediately! 
    
    We spent a lot of time wandering the town together. They're really attentive and gentle. We found a quiet spot on a nearby hill and had our first kiss under the stars. 
    
    It was magical! I asked them if they would like to go on an adventure - and they said yes!"""

    "You feel the warmth in your cheeks. You’re blushing!"

    scene intro1
    with Dissolve(0.6)

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

    "You feel the excitement bubble up within you. \nAnother adventure and this time with your crush!"

    # show langurrt2:
    #     xpos 0.2 ypos 0.2

    h """You will journey through a land that changes depending on who travels through it. 
    
    Legend says, the true nature of your relationship with your partner will be revealed."""

    p "What causes it to change?"

    h "Any choice, conversation, or conflict"

    p "That sounds difficult but I’m up for the challenge!"

    h "You and Hiran must walk through the  terrains, collecting tokens at various checkpoints until you reach the Eldest Sage. They are the keeper of some of the deepest wisdom known to us."

    p "Whoa. I’m excited and nervous and thrilled all at the same time. "
    
    hide langurrt2

    hide wiz2
    
    show wizfront1:
        xpos 0.3 ypos 0.4
    
    "While things are all upside down in that realm, just know that help is never too far away. Click on the objects to learn more"

    call screen buttons2

    "extra"

    "extra 2"

    return

screen buttons2():
    imagebutton:
        xalign 0.1
        yalign 0.35
        auto "localwizblob_%s.png" action [ToggleScreen("buttons2"), Jump("wizblob")]
    
    imagebutton:
        xalign 0.9
        yalign 0.35
        auto "bagbutton_%s.png" action [ToggleScreen("buttons2"), Jump("bagScreen")]

label wizblob:
    "blah blah info about wizards"

label bagScreen:
    "bag screen here"

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
    
    scene black
    with Dissolve(0.4)
    pause(0.3)
    # figure out fade to b
    window hide
    scene abundantforest
    with Dissolve(0.6)
    show chap1title:
        xpos 0.25 ypos 0.3

    pause

    hide chap1title
    with Dissolve (0.3)

    show langur empathetic:
        xpos 0.2 ypos 0.2

    show deer happy:
        xpos 0.6 ypos 0.2

    window auto
    
    "You and Hiran have been walking together for some time. {w}\nYou wonder what they are thinking, and how they are feeling. 

        {w}\nPaati’s warning about the Shifting Sands plays in your mind."

    p "Hiran, are you doing alright? How are you liking the journey so far?"

    dh "I’m okay...I’m a little worried. What if something bad happens to us? "

    p "I am confident that we will manage it together. Have you never been on an adventure like this?"

    dh "This is actually only my second time outside our town. Am I doing okay?"

    p "Oh I didn’t realize you are a beginner. But I’m excited to see how you manage this adventure.
Why don’t you pick a direction for us to go?"

    dh "Oh no! Please lead the way. I’m a terrible explorer. Besides, I’d love to see you in action."

    "Hiran encouraging you to take the lead has put a spring in your step. You feel a surge of confidence."
    $ esteem += 10

    p "Let’s start by looking for some food together!"
    
    show deer happy:
        xpos 0.7 ypos 0.2    
    
    """Hiran leaps slightly ahead of you. They are quick and graceful as they run through the bushes. You watch and admire them. 
        You find a rope and keep it safely. The forest is full of berries, honey and mushrooms. Click on food items to collect them.

        You both return with many berries and wildflowers."""

    ### ADD multi BERRY CLICKABLE SCREEN
    
    p "Wow! Look at all this! You’re really good at this, huh?"

    dh "Oh haha, just something I learned from my mom. I like running around and finding cool hiding spots too!"

    "You reach a campsite, where most folks on their own journeys are sitting around fires, cooking, eating and laughing. They welcome the two of you with a small cheer and suggest you find a quiet spot to camp."

    p "We’ve reached! Do you want to pick a spot?"

    dh "I’m good with anything!"

    p "Uhm okay...do you have a preference?"

    dh "No, not really. Just some place warm and I’ll curl up into a ball and sleep."

    p "Okay fine, I’ll choose this spot."

    hide langur
    with Dissolve(0.7)

    "You set up the tent while Hiran arranges dinner. They make a delicious meal of mushroom stew, honeyed buns and wildflower tea. The scent of their cooking travels through the campsite to the others."
    
    scene forestanimals

    show deer happy
    "They begin to gather around you. Click on the other adventurers to see what they’re saying!"

    ### ADD IMAGEMAP for ANIMALS

    "You notice how happy Hiran’s cooking makes the others, and feel lucky to have someone like this on the journey with you. "

    scene deerdream

    "It’s getting late! The others pack up and go into their tents. It’s just you and Hiran, alone under the stars, holding hands. "

    dh "I - um - picked this for us. It stood out from the other berries - reminded me of us."

    p "Oh my god, Hiran! Don’t eat that! That’s a really poisonous berry. "
    dh "Oh no. I’m such an idiot. I should have known."
    p "Arre, don’t worry about it! Any new explorer could have made that mistake."
    dh "I don’t know much... as you can tell. It must be frustrating to have me as a partner. "
    p "Relax, I know only because I made the mistake of eating it once - hahaha."
    dh "It’s just - it’s just that it’s been a while since I’ve felt this safe with anyone. Nobody’s ever looked out for me like you do. "

    "You don't really know what to say"

    menu:
        "Uhm....that’s awful. Let’s get some sleep.":
            "empathy hit!!"
            $ empathy -= 10
            jump nightend
            
        
        "You’re a good explorer. I’m glad to have you by my side.":
            "empathy ++ "
            $ empathy += 10
            jump nightend
    
label nightend:
    "You both head into the tent for the night."

    scene black
    with Dissolve(1)

    scene abundantforest
    with Dissolve(0.5)
    
    show langur rightface:
        xpos 0.1 ypos 0.2
    
    show deer happy:
        xpos 0.7 ypos 0.2 

    "The next morning you wake up and the tent is empty. You grab your things in a hurry and see Hiran, sitting next to the fire and holding a piece of wood and a knife."

    dh "You’re up! Slept well? I’ve been thinking about last night. "

    p "What do you mean?"

    dh "You were just so kind to me. I made this for you. As a token."

    ### add token screen

    "Hiran places a beautifully carved wooden pendant on a string into your hands. You feel the muscles in your shoulders tighten. You don’t know what to say."

    show langur shocked

    hide deer

    "You’re not sure how to react. You don’t want to hurt Hiran’s feelings but the gift is making you feel confused. You remember the compass in your bag - this might be a good time to ask for some help!"

    menu:
        "Visit Local Wizard":
            jump wizardConsult
        
        "Deal with it yourself":
            jump pendantResponse


label wizardConsult:
    scene black
    with Dissolve (0.4)
    scene wizardcave
    with Dissolve (0.4)
    show localwiz:
        xpos 0 ypos 0.2

    show langur thinking:
        xpos 0.7 ypos 0.2

    "The compass flashes on, the screen shows you a new face. This wizard wears clothes that are similar to Paati’s. "

    w1 "Welcome, young explorer! I’m the Local Wizard, Kauwa."

    p "Hello, Wizard Kauwa. Paati said I could visit you in case I needed help?"

    w1 "Oh, you must be the brave young explorer Paati was telling me about. Tell me, what’s the matter?"

    "You explain to Wizard Kauwa that you are feeling confused by Hiran’s gift - that it seems like things are moving too fast."

    p "How do I talk to Hiran without hurting their feelings?"

    w1 "Hmm, that is confusing. Before I answer, let’s look inward. How do you feel?"

    "You take a moment to listen to your thoughts and feelings. The screen on the compass begins to glow."

    w1 "That’s it! We can now look closer at your emotional states."

    show localwiz:
        easein 0.4 xpos 0.1 ypos 0.2

    w1 "What do you see?"



    
label pendantResponse:
    "pendant response here"


# screen animals():
    


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




