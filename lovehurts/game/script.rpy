# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.menu_include_disabled = True
define h = Character("Paati",  who_color="#f4c2c2")
define p = Character("You", color="#69c9b3")
define dh = Character("Hiran", color="#228b22")
define w1 = Character("Wizard Kauwa", color="#57228b")
define kw = Character("Khaang", color="#b5c9c2")
define es = Character("Eternal Sage", color="#ffbf00")
default char = "Deer"
default esteem = 0
default empathy = 0
default confidence = 0
default stress = 0
default energy = 0
default endScene = "v1"
default username = "default"

default forestBerries = False
default forestHoney = False
default forestMushroom = False

default pubWine = False
default pubBeer = False
# The game starts here.

init python:
    import json
    def to_json(obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__)

    def save_playtime(d):
        d["playtime"] = renpy.get_game_runtime()
    def jsoncallback(d):
        d["playername"] = username
        d["playtime"] = renpy.get_game_runtime()
        d["dilaogueHistory"] = to_json(_history_list)

    config.save_json_callbacks.append(jsoncallback)




label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene wiztowerdark
    if username == "default":
        $ username = renpy.input("What is the username you entered in the initial survey to play this game?")
    show langur happy
    "Hello Dori! Yes, that’s you - a bright and experienced explorer. It’s a big day for you today. You are going to meet with your mentor, the Great Wizard Paati. "

    "Your last adventure was a few months ago and while you have enjoyed resting and relaxing, you are eager to get back to exploring. "
    
    scene intro1
    with Dissolve(0.6)

    "Paati has invited you to their Tower. This means that a new adventure is coming up!"
    
    show wiz playerface:
        xpos 0.5 ypos 0.3

    "Even though it’s been a while, Paati greets you with a big hug and a cup of hot masala chai."

    h "Welcome, young one."
    extend "\nSit, relax, drink."
    extend "\nI am glad to see you are well"

    h "You seem restless - is there something on your mind?"

    menu:
        "How would you like to respond?"
        "Share what is on your mind":
        
            jump express

        "Hide what is on your mind":
        
            jump repress

label express:
    show wiz doriface:
        xpos 0.6 ypos 0.4

    show langur rightface:
        xpos 0.1 ypos 0.4
        
    "You take a deep breath and relax your body."
    
    p "On my last adventure, I had fun and collected so many different objects...but I felt lonely."
    
    h "Ah yes... adventuring can be lonely. Many explorers get lost in the forest when they try to do everything alone." 

    p "I tried to use the tools and advice you gave me, Paati. But it wasn’t easy. "

    h "Yes... the forest is not an easy place to explore. Why don’t you take someone with you on the next adventure?"

    p "Paati.. you know me so well. \n\nI met someone special recently...and I think I will ask them to join me."
    
    h "That’s wonderful news. Tell me more about them..."

    hide langurrt2

    jump charSelect

$ strength = 0
label repress:

    show wiz doriface:
        xpos 0.6 ypos 0.4

    show langur worried:
        xpos 0 ypos 0.2
    
    "Your heart skips a beat upon hearing this question. Paati knows you too well. But you are not ready to talk about things yet."

    p "It was alright - you know how adventures can be. \nI got you some nice gifts. "

    h "I am sensing that you are hiding something. Tell me, child, what is bothering you?"
    
    # show langurworried:
    #     xpos 0.1 ypos 0.2
    show langur river

    "Sometimes, it is hard to be vulnerable with those closest to us."

    p "Uff Paati...I don’t want you to see me as a child throwing a tantrum. \nThe adventure was really hard!  Sometimes you just have to deal with stuff on your own."

    h "Ah yes...adventuring can be lonely. Many explorers get lost in the forest when they try to do everything alone. There is no shame in what you felt."

    # hide langurworried

    show langur thinking:
        xpos 0.1 ypos 0.2

    "You realize how stiff and nervous you are. Yes it is difficult to be honest, but sometimes it’s so much harder to pretend."
    p "Paati, you know me so well..I tried to use the tools and advice you gave me, but there were many times I wished I had someone with me to share the adventure with."
    h "Yes...the forest is not an easy place to explore. Why don’t you take someone with you on the next adventure?"

    show langur empathetic:
        xpos 0.1 ypos 0.2
    p "I met someone special recently...and I think I will ask them to join me. "
    h "That’s wonderful news. Tell me more about them.."

    jump charSelect


label charSelect:
    hide wiz

    show langur thinking:
        xpos 0.1 ypos 0.3
    
    $ strength = False

    menu:
        "Other storylines will be available soon! Currently you can only explore this journey with Hiran!"
        "Hiran, The Romantic":
            jump deerStory
        
        "Khaang, The Confident" if strength:
            "nothing"
            # jump endStory

        "Ullu, The Observant" if strength:
            "This storyline will be available soon in an upcoming version!"
            # jump endStory


label deerStory:
    hide langurthinking
    scene black
    with Dissolve(0.5)
    scene deerdream
    with Dissolve(0.5)

    p "So... I met Hiran at the Local Pub. They are a bit shy, but I enjoyed spending time with them.{w} \nWhat I loved was they are gentle and thoughtful. A few days ago we had our first kiss under the stars. It was magical!"
    p "I asked them if they would like to go on an adventure with me - and they said yes!"

    "You feel the warmth in your cheeks as you tell Paati about Hiran. You’re blushing!"

    scene intro1
    with Dissolve(0.6)

    show langurrt2:
        xpos 0.1 ypos 0.2
    
    show wiz2:
        xpos 0.6 ypos 0.4

    h "How sweet. Having a crush is a nice feeling, isn’t it?"
    p "Yes! I am so excited to go on an adventure with them..."
    h "I have been waiting for this moment to tell you about a very special adventure. I think you are ready now..."
    p "I’m intrigued, Paati. What are we traveling through?"
    h "You will be traveling through the Land of Shifting Sands. This land is beautiful, but ever-changing. {w}\nYou and Hiran will have to use courage and communication to overcome this tricky terrain."

    "You feel the excitement bubble up within you. \nAnother adventure and this time with your crush!"

    # show langurrt2:
    #     xpos 0.2 ypos 0.2

    h "This land changes depending on who travels through it. Legend says, the true nature of your relationship with your partner will be revealed!"
    p "Oh my... What causes it to change?"

    h "Your choices, conversations, or conflicts... all of them have an effect on your surroundings."

    p "That sounds difficult, but I feel I am ready. I am sure Hiran is too."

    h "As you and Hiran explore, you must work together to collect badges, until you reach the Eldest Sage. The Sage is the keeper of some of the deepest wisdom known to us."

    p "The Eternal Sage! I always thought they were only in stories. Can’t wait to meet them."
    
    hide langurrt2

    hide wiz2
    
    show wiz playerface:
        xpos 0.3 ypos 0.4
    
    # "While things are all upside down in that realm, just know that help is never too far away. "
    
    show bagwizscreen behind wiz
    
    "Remember, young one - when things get difficult, help is never too far away. Use the materials in your bag when you get stuck."

    hide bagwizscreen
    jump postbag
    # window hide
    # call screen buttons2

    # "extra"

    # "extra 2"

    # return

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

    # hide wizfront1
    show wiz doriface:
        xpos 0.55 ypos 0.4
    
    h "And lastly you will always have us, your friends and family waiting for you back home. Go on then."

    p "I am so excited! Hiran should be reaching soon. Let’s start packing!"
    
    "Paati hands you a brand new bag. The material is strong and it is filled with items!"

    show bagicon:
        xpos 0.1 ypos 0.1

    h "Here you go, Dori. Take a look!"

    show bagpack
    window hide
    pause

    jump prechap1

label prechap1:

    scene black
    with Dissolve(0.4)
    scene journeystart
    show langur empathetic:
        xpos 0.25 ypos 0.2

    show deer happy:
        xpos 0.5 ypos 0.2

    "You are standing at the edge of the Shifting Sands. The trees, cloaked in moss, seem to be calling you. You pause to enjoy this moment of tension and excitement. {w}Suddenly you realise that a warm hand is holding yours. To your side is Hiran. They are smiling."
    
    p "Ready?"

    dh "Lead the way!"

    menu:
        "Start Journey":
            jump chap1

label chap1:
    scene black
    with Dissolve(0.4)
    scene abundantforest
    with Dissolve(0.6)
    show lushforesttitle:
        xpos 0.35 ypos 0.4

    pause

    hide lushforesttitle
    with Dissolve (0.3)

    show langur empathetic:
        xpos 0.2 ypos 0.2

    show deer happy:
        xpos 0.5 ypos 0.2

    window auto
    
    "You and Hiran have been walking together for some time. {w}\nYou wonder what they are thinking, and how they are feeling. 

        {w}\nPaati’s warning about the Shifting Sands plays in your mind."

    p "Hiran, are you doing alright? How are you liking the journey so far?"

    dh "I’m okay... I’m a little worried. What if something bad happens to us? "

    p "I am confident that we will manage it together. Have you never been on an adventure like this?"

    dh "This is actually only my second time outside our town. Am I doing okay?"

    p "Oh I didn’t realize you are a beginner. But I’m excited to see how you manage this adventure. Why don’t you pick a direction for us to go?"

    dh "Oh no! Please lead the way. I’m a terrible explorer. Besides, I’d love to see you in action."

    "Hiran encouraging you to take the lead has put a spring in your step. You feel a surge of confidence."
    $ esteem += 10

    p "Let’s start by looking for some food together!"
    
    scene abundantforest2
    
    show langur empathetic:
        xpos 0.2 ypos 0.2
    show deer happy:
        xpos 0.7 ypos 0.2    
    
    """Hiran leaps slightly ahead of you. They are quick and graceful as they run through the bushes. You watch and admire them. {w} You find a rope and keep it safely. The forest is full of berries, honey and mushrooms.""" 
    "Click on food items to collect them."

    call screen berries
    call screen berries
    call screen berries
    
    ### TODO ADD multi BERRY CLICKABLE SCREEN
    "You both return with many berries and wildflowers."""
    
    p "Wow! Look at all this! You’re really good at this, huh?"
    
    dh "Oh haha, just something I learned from my mom. I like running around and finding cool hiding spots too!"

    show badge collab:
        xpos 0 ypos 0.1
    with Dissolve(0.2)
    
    "You reach a campsite, where most folks on their own journeys are sitting around fires, cooking, eating and laughing. They welcome the two of you with a small cheer and suggest you find a quiet spot to camp."
    hide badge 
    p "We’ve reached! Do you want to pick a spot?"

    dh "I’m good with anything!"

    p "Uhm okay...do you have a preference?"

    dh "No, not really. Just some place warm and I’ll curl up into a ball and sleep."

    p "Okay fine, I’ll choose this spot."
    hide badge
    with Dissolve(0.3)

    hide langur
    with Dissolve(0.7)

    "You set up the tent while Hiran arranges dinner. They make a delicious meal of mushroom stew, honeyed buns and wildflower tea. The scent of their cooking travels through the campsite to the others."
    
    # scene forestanimals
    
    show deer happy:
        xpos 0.5
    
    "They begin to gather around you."
    show crowdialog
    "They begin to gather around you."
    pause
    show monkeydialog
    # "They begin to gather around you."
    pause

    ### TODO ADD IMAGEMAP for ANIMALS

    "You notice how happy Hiran’s cooking makes the others, and feel lucky to have someone like this on the journey with you. "

    scene deerdream

    "It’s getting late! The others pack up and go into their tents. It’s just you and Hiran, alone under the stars, holding hands. "

    show smallberries:
        xpos 0.5 ypos 0.6

    dh "I - um - picked this for us. It stood out from the other berries - reminded me of us."
    
    p "Oh my god, Hiran! Don’t eat that! That’s a really poisonous berry. "
    dh "Oh no. I’m such an idiot. I should have known."
    hide smallberries
    p "Arre, don’t worry about it! Any new explorer could have made that mistake."
    dh "I don’t know much... as you can tell. It must be frustrating to have me as a partner. "
    p "Relax, I know only because I made the mistake of eating it once - hahaha."
    dh "It’s just - it’s just that it’s been a while since I’ve felt this safe with anyone. Nobody’s ever looked out for me like you do. "

    "You don't really know what to say"
    $ stress += 10

    menu:
        "Uhm....that’s awful. Let’s get some sleep.":
            # "empathy hit!!"
            $ empathy -= 10
            jump nightend
            
        
        "You’re a good explorer. I’m glad to have you by my side.":
            # "empathy ++ "
            $ empathy += 10
            jump nightend


screen berries():
    frame:
        xpos 400 ypos 600
        # has vbox
        text "Click on food items to collect them! (There are 3!)"
    if forestBerries == False:
        imagebutton:
            xalign 0.18
            yalign 0.02        
            auto "forestberries_%s.png" action [Hide("berries"), SetVariable("forestBerries", True), Return()]
    
    if forestHoney == False:
        imagebutton:
            xalign 0.65
            yalign 0.2
            auto "foresthoney_%s.png" action [Hide("berries"), SetVariable("forestHoney", True), Return()]
    
    if forestMushroom == False:
        imagebutton:
            xalign 0.99
            yalign 0.6      
            auto "forestmushroom_%s.png" action [Hide("berries"), SetVariable("forestMushroom", True), Return()]
    

label nightend:
    "You both head into the tent for the night."

    scene black
    with Dissolve(1)

    scene abundantforest
    with Dissolve(0.5)
    
    show langur river:
        xpos 0.1 ypos 0.2
    
    show deer happy 4:
        xpos 0.5 ypos 0.1

    "The next morning you wake up and the tent is empty. You grab your things in a hurry and see Hiran, sitting next to the fire and holding a piece of wood and a knife."

    dh "You’re up! Slept well? I’ve been thinking about last night. "

    p "What do you mean?"

    dh "You were just so kind to me. I made this for you. As a token."

    show pendant1:
        xpos 0.4 ypos 0.5
    with Dissolve(0.2) 

    "Hiran places a beautifully carved wooden pendant on a string into your hands. You feel the muscles in your shoulders tighten. You don’t know what to say."

    show langur shocked

    hide deer

    "You’re not sure how to react. You don’t want to hurt Hiran’s feelings but the gift is making you feel confused. You remember the compass in your bag - this might be a good time to ask for some help!"


    menu:
        "Get help":
            jump wizardConsult
        
        "Manage it yourself":
            jump pendantResponse


default wizard1Consulted = False

label wizardConsult:
    $ wizard1Consulted = True
    scene black
    with Dissolve (0.4)
    scene wizardcave
    with Dissolve (0.4)
    show localwiz:
        xpos 0 ypos 0.2

    show langur thinking:
        xpos 0.7 ypos 0.2

    "The compass flashes on, suddenly you’re in a mystical cave with the local wizard. Their robes remind you of Paati. "

    w1 "Hello there! I’m the Local Wizard, Kauwa."

    p "Hello, Wizard Kauwa. Paati said I could visit you in case I needed help?"

    w1 "Oh, you must be the brave young explorer Paati was telling me about. Tell me, what’s the matter?"

    "You explain to Wizard Kauwa that you are feeling confused by Hiran’s gift - that it seems like things are moving too fast."

    p "How do I talk to Hiran without hurting their feelings?"

    w1 "Hmm, that is confusing. Before I answer, let’s look inward. How do you feel?"

    "You take a moment to listen to your thoughts and feelings. The screen on the compass begins to glow."

    show glowingcompass:
        xpos 0.87 ypos 0.05
    with Dissolve(0.5)

    w1 "That’s it! We can now look closer at your emotional states."

    show stats forest wiz:
        xpos 0.3 ypos 0.1

    show localwiz:
        easein 0.4 xpos 0.1 ypos 0.2

    w1 "What do you see?"
         
    p "It seems like I’m too stressed out to think straight."

    w1 "That’s right! Would it help if I explained a little bit more about the situation?"
    hide glowingcompass

    menu:
        "Yes, please":
            jump forestWizExplain
        "No, thank you. I’m ready to head out.":
            w1 "Very well, young explorer. All the best for your journey. Feel free to call any time you’re in the area."
            p "Thank you for your help! I will."
            "It feels good to get a wise perspective on things. You feel more capable of talking things out with Hiran."
            jump pendantResponse
    
label forestWizExplain:
    w1 "When someone showers you with attention and compliments at the beginning of a relationship, it is ok to feel confused."

    p "Oh I am so glad to hear that."

    w1 "Sometimes it is genuine, and sometimes it is a way to make you like them more. "

    p "But why do I feel this pressure to prove that I like Hiran? I wouldn’t be on this adventure with them if I didn’t like them!"

    w1 "In a healthy relationship, both people give each other time to fall in love without pressure and without guilt. {w}It is your right to go slow, and say no to things you're not ready for."

    p "Okay! I understand. I think I’m ready to talk to Hiran now."

    w1 "Excellent! Talking to your partner is a great way to resolve such conflicts. \n All the best for your journey. Feel free to call any time you’re in the area."
    "It feels good to get a wise perspective on things. You feel more capable of talking things out with Hiran."
    jump pendantResponse   
    
label pendantResponse:
    scene black
    with Dissolve (0.4)
    scene abundantforest
    with Dissolve (0.4)
    show langur thinking:
        xpos 0.05 ypos 0.3
    show deer tears1:
        xpos 0.7 ypos 0.2
    show pendant1:
        xpos 0.45 ypos 0.5
    menu:
        "Reject the Pendant":
            jump rejectPendant
        "Accept the Pendant":
            jump acceptPendant

label rejectPendant:
    show langur angry:
        xpos 0.15 ypos 0.2
    
    show deer angry:
        xpos 0.6 ypos 0.2
    
    p "I... uh... don't know what to say"
    $ stress += 10

    dh "Put it on, silly!"

    p "This just doesn't feel right"

    dh "Dori, what? I’m just trying to give you a gift."

    p "I don't want your dumb pendant"
    $ empathy -= 10

    """Hiran is silent but you can tell that they are hurt and angry. {w}
    \nSuddenly the land under you starts to shift. {w}\nThis is what Paati had told you about. """

    jump turbulentRiver

label acceptPendant:
    "You clasp the pendant in your hand. Hiran smiles widely. You know what you are going to say."
    menu:
        "This is such a beautiful pendant, but I think we are moving too fast":
            jump logicalPendant

        "This is such a beautiful pendant, but I am feeling so confused by it" if wizard1Consulted:
            jump empatheticPendant

label empatheticPendant:
    show langur empathetic
    show deer happy
    dh "Oh, what is there to be confused about? It’s just a pendant. I wanted to show you how much I care about you!"

    p "I feel so special. But next time can you just tell me, instead of giving me something?"

    dh "Uhm, okay. Do you not like gifts or something?"

    p "It’s not that... it’s complicated. "

    """
    You want to open up about your feelings. But you fear that Hiran will stop liking you if you tell them the truth. {w}
    \nSuddenly the land under you starts to shift. This is what Paati had told you about. 
    """

    jump valleyTruth

label valleyTruth:
    scene black
    with Dissolve(0.4)
    pause(0.3)

    window hide
    scene valleysc
    with Dissolve(0.6)
    show valleytitle:
        xpos 0.25 ypos 0.5
    pause

    window auto
    show langur thinking:
        xpos 0 ypos 0.25
    show deer normal:
        xpos 0.7 ypos 0.2
    
    hide valleytitle
    menu:
        "Start conversation":
            jump valleyConvoStart
        "Wait for Hiran to start the conversation":
            jump valleyHiranWait

label valleyConvoStart:
    show langur worried
    show deer normal:
        xpos 0.55
    "You feel the urge to explain why you’re feeling the way you’re feeling and you hope Hiran will be understanding."

    p "So I guess I should tell you why I freaked out so much about the pendant."
    dh "Yes...I don’t understand why this has become such a big deal!"
    
    p "My ex...they hurt me really badly. At the start of the relationship they were so sweet, and later they used that sweetness against me."
    p "Now I feel scared when someone is so sweet to me. I feel like I can’t trust them or something. "
    
    jump valleyCont

label valleyHiranWait:
    show deer river:
        xpos 0.5
    "Hiran comes closer to you, and holds your hand gently."
    dh "So, tell me about it. What’s complicated?"
    p "I feel like such a baby. But the truth is, my ex...they hurt me really badly. {w}At the start of the relationship they were so sweet, and later they used that sweetness against me. "
    p "Now I feel scared when someone is so sweet to me. I feel like I can’t trust them or something."
    
    jump valleyCont

label valleyCont:
    "Hiran looks at you with understanding in their eyes. You smile nervously. "
    dh "Okay, I get that. It sucks that your ex did that!"
    p "Yeah, it was confusing because the beginning was so good.  All the gifts, all the attention - I felt so loved. "
    p "Then they started making me feel guilty when I didn’t do what they wanted. They used the gifts to remind me that they were a better partner than I was."
    dh "Oh, that is so sneaky! I won’t ever do that to you. I want you to trust me and tell me what you’re feeling."
    p "I know, I am trying. I didn’t mean to hurt your feelings. I am so glad you are by my side.{w}\n"
    show badge courage:
        xpos 0.1 ypos 0.1
    with Dissolve(0.1)

    $ empathy += 10
    # TODO TOKEN AWARD

    # hide deer
    show langur thinking
    "You and Hiran seem to be quite different, but, by having a tough conversation, you are showing them and yourself that you are willing to let someone else see your feelings."
    "You feel lighter and closer to Hiran. Both of you discuss where you want to go next. What will come next for the two of you?"

    
    menu: 
        "Go ahead with excitement":
            jump localPub
        "Go ahead with caution":
            jump mangrove

label localPub:
    
    scene black
    with Dissolve(0.4)
    pause(0.3)
    
    window hide
    scene localpub

    with Dissolve(0.6)
    show pubtitle:
        xpos 0.35 ypos 0.4
    pause

    window auto
    "The valley opens up and in the distance, you see a shack. You hear music, voices and the sound of plates and glasses - seems like a good place to stop and rest. "

    hide pubtitle
    
    show langur empathetic:
        xpos 0 ypos 0.25
    show deer normal:
        xpos 0.67 ypos 0.2
    with Dissolve(0.5)
    
    "Upon entering, you see the place is crowded and full of noisy chatter. Seems to be a popular place."

    p "Wow, this is nice! And look at all these people! It’s good to see so many new faces. "

    dh "I get a little nervous in crowded places. Will you stay close to me?"

    p "Of course, I promise."
    
    "You can sense that Hiran is not going to enjoy the evening, but you are excited to socialize with the other explorers."

    show langur empathetic 4 behind deer:
        xpos 0.45 ypos 0.2
    show wolf npc1:
        xpos 0.05 ypos 0.2
    show deer normal:
        xpos 0.72
    kw "Hey, newcomers! You both look like you have some stories to tell. Why don’t you join our table?"
    
    show badge social:
        xpos 0 ypos 0.1

    $ confidence += 10
    
    show langur empathetic 5:
        xpos 0.2
    show wolf npc1 behind langur:
        xpos 0.45
    show deer normal:
        xpos 0.78

    "The other travellers seem very impressed by you and your stories. You are enjoying the attention and try to keep Hiran involved in the conversation."

    "You tell the others about how Hiran impressed the campsite with their cooking and quickness. You hold Hiran’s hand and squeeze it gently. They squeeze yours and seem to relax a bit."

    hide badge
    
    show localpub2 behind langur
    # "Click on the objects to drink"
    call screen drinks
    call screen drinks
    # TODO Add clickable drinks

    $ confidence += 10

    hide wolf

    show deer normal:
        xpos 0.47
    
    "After a few hours, people start leaving. Soon, you and Hiran are alone in the pub. You are feeling relaxed and happy. "

    dh "You are so good with people - they like listening to you tell your wonderful stories!"

    p "Ha ha, I just like meeting new people! I’m so glad you stayed. You did such a great job too and I’m proud of you! "

    dh "Thanks! I’m proud of me too. I was nervous at first but then it was fun. It was easier because you were by my side."

    p "You know I've got your back!"

    "You see a familiar shawl in the bar and you recognize it!"
    
    p "Oh look, the Local Wizard Kauwa is here! Let me go say hi."

    hide deer 

    show langur thinking:
        xpos 0.65 ypos 0.22
    
    show localwiz:
        xpos 0.2 ypos 0.22
    
    w1 "Young Dori! You look well! How’s the adventuring going? "

    p "Things are going well with Hiran. I feel that we are both trying to make it work with each other."

    w1 "Well, I am very happy to hear that! "

    p "Wizard...I know this may seem a little weird but would you be able to help me look inward again?"

    w1 "Gladly!"

    "You take a moment to listen to your thoughts and feelings. The screen on the compass begins to glow. "
    show glowingcompass:
        xpos 0.87 ypos 0.05
    with Dissolve(0.5)
    pause

    show stats pub1:
        xpos 0.3 ypos 0.1
    # TODO stats screen

    w1 """Look at that, Dori! Great work! A strong relationship is about give and take. 
    {w}But remember, it not about keeping score of who does how much! {w}
    Give with an open heart, and ask for what you want. A good partner will do the same for you."""

    p "Thank you, Kauwa"
    hide glowingcompass
    hide stats

    hide localwiz

    show langur empathetic 5:
        xpos 0.2 ypos 0.18
    
    show deer normal:
        xpos 0.6 ypos 0.22

    "Having had a nice moment with the Wizard Kauwa, you return to Hiran."
    p "I just spoke to the Local Wizard and told them how well we are doing together."
    dh "Oh yes..I think we’re on the right path. I feel very close to you."
    p "Me too!"
    dh "So, then...would you be open to making it more official with the pendant?"

    show langur thinking:
        xpos 0.1 ypos 0.22

    "You don’t want to spoil the good mood, but you are not comfortable with what Hiran is doing. "

    menu:
        "You've had enough!":
            jump pubFight
        "Try to get your point across":
            jump pubTalk

screen drinks():
    text "Click on the objects to drink":
        xpos 0.5 ypos 0.3
        at transform:
            alpha 1
    if pubBeer == False:
        imagebutton:
            xpos 218
            ypos 330
            auto "pubbeer_%s.png" action [Hide("berries"), SetVariable("pubBeer", True), Return()]
    
    if pubWine == False:
        imagebutton:
            xpos 965
            ypos 326
            auto "pubwine_%s.png" action [Hide("berries"), SetVariable("pubWine", True), Return()]

label pubFight:
    show langur angry
    "There is a loud rumble - thick roots and trees sprout from the pub. The land is changing again!"

    p "Hiran I told you I don’t want any gifts right now. Why can’t you respect that and just let this go? It’s such weird behaviour!"
    dh "You’re being so mean."

    $ endScene = "m2"
    jump mangrove4
    
label pubTalk:
    show langur empathetic 5:
        xpos 0.2
    show deer river:
        xpos 0.55
    p "Hiran, I told you, I don’t want to do anything big right now but I’ll keep the pendant close and wear it when I’m ready.  Does that sound good?"
    dh "That sounds good!"

    "You and Hiran exchange a tender kiss. You feel the ground become uneven beneath you - the land is changing again!"

    $ endScene = "rh1"
    jump rollingHills

label mangrove:
    scene black
    with Dissolve(0.4)
    pause(0.3)
    
    window hide
    scene mangrovesc1

    with Dissolve(0.6)
    show mangrovetitle:
        xpos 0.3 ypos 0.4
    pause

    window auto
    "The valley opens up into a swamp. The mud is thick and sticky, it is hard to get through. Hiran is struggling more than you are."

    hide mangrovetitle
    
    show langur worried:
        xpos 0.57 ypos 0.16
    show deer river left:
        xpos 0.1 ypos 0.16
    with Dissolve(0.5)

    dh "Slow down! I keep getting stuck!"

    p "It’s hard for me to walk too! I don’t know what to do to make it easier."

    dh "There ‘s rope in your bag. Use that!"

    show deer normal left
    
    show langur thinking

    "You tie Hiran to yourself using the rope, and you both begin to walk slowly through the mud. It is much easier. But you suddenly realize something."

    # TODO Secure supporter badge

    p "Hiran, how do you know that I had rope? Did you look in my bag?"

    dh "Well, I couldn’t find my watch and I thought it might have gotten put into your bag. You know it’s normal for people traveling together to look inside each other’s things, right?"

    "You do not agree with Hiran. It is pretty weird that they opened your bag like that. You might need some help with this one!"

    show langur shocked

    menu:
        "Get help":
            jump pubWizard

        "Manage by yourself":
            jump marshPass


label pubWizard:
    scene black
    with Dissolve (0.4)
    scene wizardcave
    with Dissolve (0.4)
    show localwiz:
        xpos 0 ypos 0.2

    show langur thinking:
        xpos 0.7 ypos 0.2

    w1 "Welcome, Dori! I can see you look distressed - let’s take a look inward!"

    show stats mangrove1:
        xpos 0.3 ypos 0.1
        
    #TODO Stats Screen

    p "Kauwaji, is it wrong that I feel angry at Hiran for going through my bag without asking me."

    p "I don’t have anything to hide from them. We are getting so close to each other. {w}\nBut does that mean that they can just go through my private things?"
    dh "In one word - no!"
    dh "In any relationship, there are some things that are shared, and some things that are private."
    dh "Trusting your partner includes respecting their privacy and individuality. "
    dh "Going through your partner’s things, especially without their permission or knowledge violates that trust."

    p "I had a feeling that was the case."
    
    scene mangrovesc1
    with Dissolve (0.4)
    show deer normal left:
        xpos 0.15 ypos 0.2
    
    show langur thinking:
        xpos 0.7 ypos 0.22
    
    jump marshPass

label marshPass:
    "Your heart sinks. You don’t know if things can be fixed with Hiran - this was a violation of your trust and privacy. "

    menu:
        "Tell them how you feel.":
            jump marshTell

        "Let it pass.":
            jump marshPass2
        
        "Break up with Hiran.":
            jump marshBreakup

label marshTell:
    show deer:
        xpos 0.2
    show langur:
        xpos 0.4
    
    p "Hiran, it wasn’t okay that you went through my stuff without asking. "

    p "I know we’re partners and everything but my privacy is important to me - and I wouldn’t go through your things."

    dh "I’m sorry, I didn’t know this is how you felt. In my previous relationships, I shared everything my partners. "
    dh "I can’t say it was the healthiest thing, but it made us feel closer. "
    dh "I want you to know you can trust me and that I respect your space. It won’t happen again."

    p "Okay, thanks for being honest. Next time, just ask me."
    $ endScene = "rh2"
    jump rollingHills

label rollingHills:
    scene black
    with Dissolve(0.4)
    pause(0.3)
    
    window hide
    scene rollinghillsalone

    with Dissolve(0.6)
    show rollingtitle:
        xpos 0.05 ypos 0.3
    pause

    window auto
    
    hide rollingtitle
    
    show langur empathetic 5:
        xpos 0.2 ypos 0.22
    show deer happy 2:
        xpos 0.45 ypos 0.1
    
    with Dissolve(0.5)

    "Hand in hand, you and Hiran run outside. You have reached the final destination - the legendary Rolling Hills!"
        
    
    dh "This place is lovely, Dori!"
    p "I know! The sky, the sun, having you here with me. So much to be grateful for. "
    

    "You are enjoying the hills together when..." 
    show white bg
    with Dissolve(0.1)
    show deer happy 3:
        xpos 0 ypos 0.1
    show langur worried behind deer:
        xpos 0.1 ypos 0.2
    show eternalsage:
        xpos 0.6
    hide white
    with Dissolve(0.8)

    "Suddenly there is a flash of light; the brightness almost blinds you! You see a mysterious figure standing before you. The Eternal Sage!"

    "The Eternal Sage looks inside your eyes and senses everything. "
    
    if endScene == "rh1":
        show stats rh1:
            xpos 0.3 ypos 0.1
    if endScene == "rh2":
        show stats rh2:
            xpos 0.3 ypos 0.1
    #TODO Stats screen
    hide deer 
    show langur:
        xpos 0 ypos 0.1
    es "Welcome to the final stage of your adventure, Monkey Dori! Your friends and family will be thrilled to see how far you’ve come."
    es "These lands are not easy to cross and yet you showed great courage and communicated well with your partner, Hiran."
    es "I hope you are satisfied with your ending. If you would like to use it, I grant you a single use of my Time Machine. "
    es "This powerful relic that allows you to revisit key moments in your journey and change your decision. You can see how differently things could have turned out."
    p "A Time Machine? How can I ever repay you for such a gift?"
    es "Challenge yourself, young one! Make an effort to have tough conversations, ask for help and listen to what you need. That will be your repayment."

    hide stats
    "What do you do? Do you wish to take the second chance and change the course of your story? Or do you accept and learn to live with the decisions you’ve made?"
    show langur thinking
    
    call screen postsurvey
    menu:
        "Use Time Machine":
            p "Thank you, Eternal Sage. I promise to use this gift responsibly and make things right."
            jump pendantResponse
        "End Game":
            return


label marshPass2:
    p "You know what, maybe I’m overthinking this."
    dh "Yeah, I think you are."
    $ endScene = "bd3"
    jump barrenDesert


label marshBreakup:
    p "Hira, what you did back there really wasn’t cool. You broke my trust and you invaded my privacy."
    
    p "I don't think we should be together anymore"

    dh "You’re breaking up with me? But I didn’t even do anything, "

    dh "You know what! Fine. I don’t need you any way. {w}This whole thing has been one disaster after another. {w}I’m better off without you. Have fun on your stupid little quest."
    
    $ endScene = "rha2"
    jump rollingHillsAlone

label logicalPendant:
    show langur worried
        # xpos 0.2 ypos 0.3
    show deer angry
        # xpos 0.7 ypos 0.3
    dh "That's mean. I'm just trying to show you that I like you. Why are you making it such a big deal?"
    p "I do appreciate the gift. I just want to take things slow."
    dh "Yeah, whatever. Maybe you're just like the rest of them"
    p "Hey, that's not fair! I'm only trying to tell you how I feel!"
    $ stress += 10
    $ confidence -= 10
    show deer:
        ease 1.4 xpos 1.2
        
    "Hiran shrugs and turns away. \nSuddenly the land under you starts to shift. This is what Paati had told you about. "

    jump turbulentRiver
# screen animals():
    
label turbulentRiver:
    scene black
    with Dissolve(0.4)
    pause(0.3)
    # figure out fade to b
    window hide
    scene turbulentbg
    with Dissolve(0.6)
    show turbulentrivertitle:
        xpos 0.25 ypos 0.5
    pause
    
    # ""
    hide turbulentrivertitle

    show deer river left:
        xpos 0.1 ypos 0.2
    
    show langur angry 2:
        xpos 0.6 ypos 0.2
    window auto
    "Clouds form above your head and rain begins to fall. It shifts the mud beneath you, pushing you towards a river. Tied to a pole, is a small boat. You realize there is nowhere to go except through. You and Hiran get into the boat in a hurry. "

    dh "What’s your problem, dude? Who reacts like that to a small gift."

    p "It’s complicated, okay! And also, does this seem to be a good time to have a conversation? We’re literally fighting for our lives."
    
    $ stress += 10

    show langur worried

    show deer tears left

    dh "We're in this mess because of you"
    $ confidence -= 10
    dh "Why are you so closed off?"
    dh "Just answer me! {w}Why did you even ask me out? It seems like everything has to be on your terms and you always get your way."

    p "Hiran, I am literally trying to get us out of this dangerous river. Do you think we could MAYBE have this conversation once we’re in a safer environment? "
    dh "We ARE the environment, Dori. Did you not even listen to your Paati."

    $ stress += 10

    "You are having trouble deciding which problem to focus on. Why is Hiran being so unhelpful? "
    "You decide that survival is more important than Hiran’s feelings."

    p "For God’s sake, Hiran, just help me row the boat."

    dh "I should never have agreed to be here with you."

    "Hiran grabs the second oar in anger. The two of you row the boat through the choppy waters. "

    show langur thinking:
        ypos 0.24

    "After a few hours, the river calms down and the rain stops. You are completely exhausted."

    scene turbulentbg2
    show langur thinking:
        xpos 0.6 ypos 0.24
    show deer tears left:
        xpos 0.1 ypos 0.2
    
    "You want to thank Hiran for their help with the boat, but the tension between you is too high."
    "You remember the compass in your bag - this might be a good time to ask for some help!"

    menu:
        "Get help":
            jump riverWiz
        "Manage by yourself":
            jump riverCont

label riverWiz:

    scene black
    with Dissolve (0.4)
    scene wizardcave
    with Dissolve (0.4)
    show localwiz:
        xpos 0 ypos 0.2

    show langur thinking:
        xpos 0.7 ypos 0.24
    "The compass flashes on"

    w1 "Back so soon, young one!"
    p "I need your help, Wizard! It’s still only the beginning of my new relationship and I’m exhausted."

    w1 "Okay, explorer, let’s see what we can do! Take a deep breath and focus."

    "You take a moment to listen to your thoughts and feelings. The screen on the compass begins to glow. "
    show glowingcompass:
        xpos 0.87 ypos 0.05
    with Dissolve(0.5)
    pause

    #TODO STATS Screen
    show stats forest wiz:
        xpos 0.3 ypos 0.1

    w1 "You seem upset, young one. \n You might find it helpful to use the tools you and Paati packed. Why don’t we look in the bag and see what we have? What are two tools that can help you feel better in this moment?"

    hide glowingcompass
    hide stats
    show bag river wiz:
        xpos 0.32 ypos 0.3
    pause
    # show 
    #TODO Inventory screen

    "You take a moment to have a snack and focus your energy -  the temperature of the cave feels cool, the air smells fresh, you see the sunlight through the waterfall, the chips taste salty and delicious and you listen to the sound of the forest all around you. "
    hide bag river wiz

    show badge emotion:
        xpos 0.4 ypos 0.4

    "Having rested and recollected your thoughts, you feel you have the energy to return. "
    
    scene turbulentbg2
    with Dissolve(0.6)

    show langur thinking:
        xpos 0.65 ypos 0.24

    jump riverCont

label riverCont:
    show deer normal left:
        xpos 0.15 ypos 0.2
    
    "You turn to face Hiran"

    menu:
        "Ignore the fight":
            jump riverIgnore

        "Talk about the fight":
            jump riverTalk

label riverIgnore:
    show langur worried
    p "Listen, I'd rather not get into what happened back there. Can we just leave it behind us?"
    $ empathy -= 10
    dh "Uhm, okay."
    "You tie up the boat and leave it by the shore. In the distance, you see shack. You hear music, voices and the sound of plates and glasses - seems like a good place to stop and rest. "
    p "Let’s go there. I’m sure we’ll feel better after some time."

    jump pub3

label riverTalk:
    p "Listen Hiran, if we want to make this work, then we need to talk."
    dh "That’s literally all I’ve been trying to do with you."

    "You tie up the boat and leave it by the shore. Up ahead, you see the land slopes into a deep valley. You wonder what will come next. "

    jump valleyTruth3

label valleyTruth3:
    scene black
    with Dissolve(0.4)
    pause(0.3)

    window hide
    scene valleysc
    with Dissolve(0.6)
    show valleytitle:
        xpos 0.25 ypos 0.5
    pause

    window auto
    show langur thinking:
        xpos 0 ypos 0.25
    show deer normal:
        xpos 0.7 ypos 0.2
    
    hide valleytitle
    menu:
        "Start the conversation":
            jump valleyConvoStart3
        "Wait for Hiran to start the conversation":
            jump valleyHiranWait3

label valleyConvoStart3:
    show langur worried
    show deer river:
        xpos 0.55
    p "I feel I have been making all the decisions and you’re so passive. But, somehow I feel I have no control on what is happening."
    dh "I don’t know what you’re talking about. I am just trying to learn and help. I am new to adventure, remember? "
    dh "In fact, I feel like you’re just waiting to push me away."
    p "That is not true! How can you say this? This is coming out of nowhere!"
    dh "I am not passive, I am trying to learn from you because we have to stick together. Sorry but it’s just the truth. "
    dh "Also! I would like if you were more appreciative of my gifts."

    jump valleyCont3

label valleyHiranWait3:
    show deer river:
        xpos 0.55
    dh "I feel like you’ve been avoiding talking about how you feel...why?"
    p "I’m trying, Hiran This is new for me. "
    dh "I hope you know it took lot of courage for me to go on this adventure. The truth is I constantly worry about if you still like me or not. {w}It’s because of my past where I was hurt by my partner. I can’t help it."
    p "I care about you a lot but sometimes, I feel overwhelmed by the constant need for me to keep proving it. {w}\nIt's been a lot to handle, especially since we just started this journey."
    dh "l didn’t realize you were feeling pressured and stressed. I will work on it. But can you think about accepting the gift?"
    jump valleyCont3

label valleyCont3:
    # show langur rightface
    # "Hiran looks at you with understanding in their eyes. You smile nervously. "
    # dh "Okay, I get that. It sucks that your ex did that!"
    p "Oh yeah, the pendant. Look, I have bad history with partners showering me with gifts only to throw them in my face later. {w}It made me feel really guilty. So now gifts just make me feels weird."
    p "Then they started making me feel guilty when I didn’t do what they wanted. They used the gifts to remind me that they were a better partner than I was."
    dh "Oh, that is so sneaky! I won’t ever do that to you. I want you to trust me and tell me what you’re feeling."
    p "I know, I am trying. I didn’t mean to hurt your feelings. I am so glad you are by my side.{w}\nI'll work on saying things out loud. We'll face this together."
    show badge courage:
        xpos 0.1 ypos 0.1
    with Dissolve(0.1)

    $ empathy += 10
    # TODO TOKEN AWARD

    # hide deer
    show langur shocked
    "You and Hiran seem to be quite different, but, by having a tough conversation, you are showing them and yourself that you are willing to let someone else see your feelings."
    "You feel lighter and closer to Hiran. Both of you discuss where you want to go next. What will come next for the two of you?"

    dh "I’m really glad you told me, Dori. I wouldn’t have known. "
    p "It does feel good to tell someone. "
    p "I think we’re almost through the tunnel- there’s a light up ahead!"
    dh "I see it - let’s go!"

    menu: 
        "Go ahead with excitement":
            jump localPub
        "Go ahead with caution":
            jump pub3

label pub3:
    scene black
    with Dissolve(0.4)
    pause(0.3)
    # figure out fade to b
    window hide
    scene localpub
    with Dissolve(0.6)
    show pubtitle:
        xpos 0.35 ypos 0.5
    pause
    
    # ""
    hide pubtitle
    
    window auto
    "You enter a crowded pub. It seems to be a popular place and is full of noisy chatter."

    
    show langur empathetic:
        xpos 0 ypos 0.25
    show deer normal:
        xpos 0.67 ypos 0.2
    with Dissolve(0.5)
    
    p "Wow, this is nice! And look at all these people! It’s good to see so many new faces. "

    dh "Why does it sound like you want to talk to anyone except me?"

    p "Look, I just want to enjoy myself and forget about how stressful this adventure has been so far. I suggest you do the same. You might enjoy letting loose!"
    
    dh "(Sadly) Okay...please stay close to me, though. I don’t want to get lost in the crowd. "

    "You can sense that Hiran is nervous and shy, but seeing other people has improved your mood. "

    show langur empathetic 4 behind deer:
        xpos 0.45 ypos 0.2
    show wolf npc1:
        xpos 0.05 ypos 0.2
    show deer normal:
        xpos 0.72
    kw "Hey, newcomers! You both look like you have some stories to tell. Why don’t you join our table?"

    show badge social:
        xpos 0.4 ypos 0
    
    $ confidence += 10
    
    show langur empathetic 5:
        xpos 0.2
    show wolf npc2 behind langur:
        xpos 0.45
    show deer normal:
        xpos 0.78

    "The other travellers seem very impressed by you and your stories. {w}You don’t know if it is the alcohol or the attention, but your tension melts away and you forget all about the fight. {w}You also forget about Hiran."

    hide badge
    show deer angry

    # "Click on the objects to drink "
    call screen drinks
    call screen drinks
    # TODO Add clickable drinks

    $ confidence += 10

    hide wolf
    with Dissolve(0.3)
    
    show langur shocked:
        xpos 0.2

    "Suddenly you realize that Hiran has left the room. You see them standing in the corner, looking angry."

    show deer angry:
        xpos 0.47
    
    dh "You forgot about me, didn’t you?"
    p "I - uh - was just coming to check on you!"
    dh "I’m not an idiot, Dori. I can see you love being the center of attention."
    p "*hiccup*"
    dh "And by the way I saw you were flirting with that hot wolf!"
    p "..."
    dh "Are you being like this to hurt me? What did I do to deserve this?"
    $ stress += 10
    dh "Are we ever going to talk about the pendant or not?"
    $ energy -= 10

    "Your head feels fuzzy and Hiran’s words leave you numb. You run out of the pub and spot a Local Wizard. Help is right here if you want it."
    show langur:
        xpos 0.0
    show deer:
        xpos 0.7
    menu:
        "Get help":
            jump pubWiz
        "Manage it yourself":
            jump pubCont

label pubWiz:
    hide deer
    show langur thinking:
        xpos 0.6 ypos 0.24
    show localwiz:
        xpos 0.1 ypos 0.24
    
    "You run up to the Wizard. They greet you warmly but realize quickly that something is wrong."
    w1 "Young Dori! You don’t well at all! Anything I can help with?"
    p "Yes! I think I really hurt my partner and they said some things that hurt me too. What do I do!"
    w1 "Well, let’s take a look, shall we?"
    "You take a moment to listen to your thoughts and feelings. The screen on the compass begins to glow. "
    show glowingcompass:
        xpos 0.87 ypos 0.05
    with Dissolve(0.5)

    show stats pub early:
        xpos 0.3 ypos 0.1
    #TODO Stats screen
    w1 "I sense that there has been a break down in the trust and communication between you and Hiran."
    p "I feel like I’m doing everything wrong with Hiran. They’re being so clingy. I feel so stuck with them."
    w1 "This can happen when two people find themselves in a stressful situation."
    w1 "Hiran did something that hurt you, and then you did something to hurt them. And now they tried to hurt you again. Watch out for this cycle!"
    w1 "Remember, hurting someone who hurt you will not take away your pain!"
    hide glowingcompass
    hide stats
    "You realize the truth of those words."
    w1 "Your next few steps are very important for your future with Hiran, so you need to be careful. "
    w1 "Even though you have the tools in your bag, you seem too fatigued to use them. \nI suggest you rest and recover."
    hide localwiz
    show langur:
        xpos 0.0

    show deer angry:
        xpos 0.7 ypos 0.2
    jump pubCont

label pubCont:
    "You walk back into the pub and find Hiran sitting alone, with an angry expression on their face. The thought of talking to them scares you. Before you can say anything, they get up."
    menu:
        "Go back to the room":
            jump homeReturn

        "Stay in the pub":
            dh "I am going to sleep. This has been a crazy day"
            jump homeLate

label homeReturn:
    scene black
    with Dissolve(0.4)
    pause(0.3)
    scene pubhomebg
    with Dissolve(0.6)
    $ energy += 10
    "You follow Hiran to the room, but they are in no mood to talk. It takes you many hours to fall asleep because you keep going over the last few days. 
    The next morning, you need to make an important decision."
        
    show langur thinking:
        xpos 0 ypos 0.25
    show deer angry:
        xpos 0.67 ypos 0.2
    with Dissolve(0.5)
    
    menu:
        "Share what's on your mind":
            jump homeShare
        "Pretend like nothing happened":
            jump homeIgnore


label homeShare:
    show langur worried
    p "Listen, Hiran. If we want to make this work, then we really need to talk."
    "You hear a rumble and look outside the window. The land is changing again. You and Hiran run outside."

    jump valley4
    
label valley4:
    scene black
    with Dissolve(0.4)
    pause(0.3)

    window hide
    scene valleysc
    with Dissolve(0.6)
    show valleytitle:
        xpos 0.25 ypos 0.5
    pause

    hide valleytitle

    window auto
    show langur worried:
        xpos 0 ypos 0.25
    show deer normal:
        xpos 0.7 ypos 0.2
    "You feel a cool breeze as you open the door. Up ahead, you see the land slopes into a deep valley. You suggest a walk and prepare yourself for a tough conversation."

    p "I feel so tired of proving how much you mean to me. This relationship feels like a never ending test. "
    p "I feel like nothing I do is enough for you."
    dh "You know I have my own worries and insecurities. If you can’t accept me, then I don’t think this is going anywhere."
    p "I don’t want our relationship to feel like a problem we have to fix. "
    dh "Wow. I’m sorry you feel that way."

    "You’re starting to feel very frustrated, like you’re about to snap."

    show deer river left:
        xpos -0.1
    show langur behind deer:
        xpos 0.1
    show eternalsage:
        xpos 0.6
    
    "Suddenly, there is a flash of light; the brightness almost blinds you! You see a mysterious figure standing before you. The Eternal Sage!"
    
    es "Young adventurers, you seen to be struggling."

    hide deer
    show langur:
        xpos 0
    "You feel the Sight of The Eternal Sage on you. You know that they sense everything."
    show stats valley end:
        xpos 0.3 ypos 0.1
    #TODO Stats Screen

    es "Young Dori, how heavy your heart is!
    {w}\nRemember that going on an adventure with a partner can be a wonderful thing, and it should never feel like a burden. The journey  is not about proving anything; it's about understanding, trust, and connection."
    es "I see that you feel that you lost control of things with Hiran. I can help with that as I believe things can change."
    es "So, I grant you a single use of my Time Machine, a powerful relic that allows you to revisit those moments and act differently, changing the course of events."
    hide stats
    "What do you do? Do you wish to take the second chance and change the course of your story? Or do you accept and learn to live with the decisions you’ve made?"

    call screen postsurvey
    menu:
        "Use Time Machine":
            p "This is wonderful wise one. Thank you! I want to know if things could have gone differently."
            jump pendantResponse
            # return
        "End Game":
            return



label homeIgnore:
    show deer normal left
    "You have already invested so much time into this relationship but the tension between the two of you seems too much to address right now. Hopefully, things will get better with a change of scene."

    p "Hope you slept well. Let’s just keep moving."
    dh "Fine. Whatever"

    # "GOING TO MARSHY LAND"
    $ endScene = "m1"
    jump mangrove4

label mangrove4:
    scene black
    with Dissolve(0.4)
    pause(0.3)
    
    window hide
    scene mangrovesc1

    with Dissolve(0.6)
    show mangrovetitle:
        xpos 0.3 ypos 0.4
    pause

    window auto
    
    hide mangrovetitle
    
    show langur angry:
        xpos 0.6 ypos 0.22
    show deer river left:
        xpos 0 ypos 0.22
    with Dissolve(0.5)

    "You walk right into a marsh that has appeared. The pathway is muddy and it is very difficult to walk. Hiran is struggling a lot and needs your help."

    dh "Will you slow down! I keep getting stuck!"
    p "Try harder then!"
    $ empathy -= 10
    dh "Don’t you have rope in your bag? Just use that."
    p "How do you know what’s in my bag? Did you look in it without asking me?"
    dh "I was going to put the pendant in as a surprise! You know it’s normal for people travelling together to look inside each other’s things?"
    $ stress += 10
    p "What? I told you I didn’t want that!"
    dh "I was hoping you’d changed your mind after all this time. Will you please just use the rope - I’m sinking in the mud!"
    p "You’re the worst partner I’ve ever had and I - "

    "Suddenly, there is a flash of light; the brightness almost blinds you! You see a mysterious figure standing before you. The Eternal Sage!"
    show white bg
    with Dissolve(0.1)

    show deer normal left:
        xpos -0.2   
    show langur worried behind deer:
        xpos 0.2
    show eternalsage behind white:
        xpos 0.65
    
    hide white bg
    with Dissolve(1.5)


    es "Young adventurers! What’s all the commotion?"
    hide deer
    "You feel the Sight of The Eternal Sage on you. You know that they sense everything."

    if endScene == "m1":
        show stats mangrove 1:
            xpos 0.3 ypos 0.1
    #TODO Stats screen for m1 vs m2

    es "Young Monkey Dori, you seem frustrated and disappointed. These Marshy Lands are indeed difficult to cross.
    \n{w}But, don’t worry, I see your pain - you are hurt and regret the hurt you’ve caused Hiran. You don’t know how to mend it." 
    es "I can help with that as I believe in second chances. {w}\nI grant you a single use of my Time Machine, a powerful relic that allows you to revisit those moments and make amends."
    p "A Time Machine? How can I ever repay you for such a gift?"
    es "You must use this gift wisely, Dori. You can choose to undo the hurt you've caused, learn from your mistakes, cross these lands with Hiran. That will be your repayment."

    hide stats
    "What do you do? Do you wish to take the second chance and change the course of your story? Or do you accept and learn to live with the decisions you’ve made?"

    call screen postsurvey
    menu:
        "Use Time Machine":
            p "Thank you, Eternal Sage. I promise to use this gift responsibly and make things right."
            jump pendantResponse
        "End Game":
            return

label homeLate:
    scene black
    with Dissolve(0.4)
    pause(0.3)
    scene pubhomebg
    with Dissolve(0.6)
    $ energy -= 10
    show langur worried:
        xpos 0 ypos 0.25
    show deer angry:
        xpos 0.67 ypos 0.2
    with Dissolve(0.5)
    "You are woken up by the sun rays hitting your eyes. You don’t remember last night, just that you stayed back in the pub and had a few more drinks. 
    \n{w}Where are you? And how did you get here?"

    dh "I see you are awake. Hope you had a fun night. One of your new friends dropped you off here just as the sun was rising."
    dh "Where the hell were you? Next time I’m not letting you out of my sight."
    menu:
        "You feel angry":
            jump homeAngry
        "You feel guilty":
            jump homeGuilty

label homeAngry:
    show langur angry
    "You feel like you're being treated unfairly"
    menu:
        "Listen, Hiran. If we want to make this work, then we need to talk." if energy > 1000:
            "I'm too tired to talk"
        "I can’t deal with your tantrums anymore.It’s over.":
            $ endScene = "rha1"
            jump rollingHillsAlone

label rollingHillsAlone:
    scene black
    with Dissolve(0.4)
    pause(0.3)
    
    window hide
    scene rollinghillsalone

    with Dissolve(0.6)
    show rollingalonetitle:
        xpos 0.05 ypos 0.3
    pause

    window auto
    
    hide rollingalonetitle
    
    show langur shocked:
        xpos 0.2 ypos 0.22
    
    with Dissolve(0.5)

    "Hiran leaves and you find your path leads you into a beautiful field. The sky is blue and the sun shines brightly. "
    
    "As you walk through the grasses, you think about how excited you had been to start this adventure with Hiran. {w}Since then, you have learned how challenging communication can be - learning about another person and their needs."
    
    "You think about the choices you made - some you are proud of, some you aren’t. Perhaps you have more questions now than you did at the start of your journey. {w}For example, is there such a thing as true love or a perfect partnership? "
    
    "You miss Hiran - having someone to talk to and share the adventure with - but you are relieved that you don’t have to reassure them constantly. "
    
    "You begin to wonder when your journey will end. "
    show white bg
    with Dissolve(0.1)
    show langur worried:
        xpos 0.1 ypos 0.26
    show eternalsage:
        xpos 0.6

    hide white
    with Dissolve(0.9)
    
    "Suddenly a bright light glows and a mysterious figure appears. It is the Eternal Sage!"

    es "Young Dori, welcome to the Rolling Hills! Reflecting on your journey alone?"
    p "Wise One! Paati told me I’d meet you eventually. It is good to see you. "
    p "Yes, actually. I’m thinking about how I ended up here. "

    "You feel the Sight of The Eternal Sage on you. You know that they sense everything."

    
    if endScene == "rha1":
        show stats rha1: 
            xpos 0.3 ypos 0.1
        with Dissolve(0.3)
    if endScene == "rha2":
        show stats rha2:
            xpos 0.3 ypos 0.1
        with Dissolve(0.3)
    #TODO Stats screen

    es "Young Monkey Dori, you have many questions! This is good. {w}
    \nWhile not every question has an answer, I am proud to see you taking the time to reflect and think about the choices you have made."
    es "If you would like to use it, I grant you a single use of my Time Machine, a powerful relic that allows you to revisit key moments in your journey and change your decision. You can see how differently things could have turned out."
    p "A Time Machine? How can I ever repay you for such a gift?"
    es "You must use this gift wisely, Dori. Make an effort to have tough conversations, ask for help and listen to what you need. That will be your repayment."

    hide stats
    "What do you do? Do you wish to take the second chance and change the course of your story? Or do you accept and learn to live with the decisions you’ve made?"
    show langur thinking

    call screen postsurvey
    menu:
        "Use Time Machine":
            p "Thank you, Eternal Sage. I promise to use this gift responsibly and make things right."
            jump pendantResponse
        "End Game":
            return
    



label homeGuilty:
    show langur thinking
    p "You made what you wanted clear to me and I forgot. I know that must’ve hurt you and for that I’m so sorry. It won’t happen again."
    dh "It better not"
    "You hear a rumble and look outside the window. The land is changing again. You and Hiran run outside."
    $ endScene = "bd1"
    jump barrenDesert

label barrenDesert:

    scene black
    with Dissolve(0.4)
    pause(0.3)
    
    window hide
    scene barrendesert

    with Dissolve(0.6)
    show barrentitle4:
        xpos 0.3 ypos 0.4
    pause

    window auto
    
    hide barrentitle4
    
    show langur shocked:
        xpos 0.1 ypos 0.22
    show deer normal left:
        xpos 0.6 ypos 0.22
    with Dissolve(0.5)

    "As you walk, the path turns to sand. You find yourself in a hot, dusty desert. There’s no one around you for miles. "
    dh "This is nice, huh? Just you and me - nobody else to bother us?"
    "Hiran’s words feel strangely lonely. Despite being physically in same place there doesn’t like you two have  much to do or talk about. You are unsure about how to bring it up especially since the last few environments have been so taxing. "
    p "I mean, it would be nice if there was something or someone else around. Don’t you feel lonely?"
    dh "How could I feel lonely when I have you all to myself?"
    "There’s that sinking feeling again."

    show deer normal left:
        xpos 0
    show langur worried behind deer:
        xpos 0.1
    show eternalsage:
        xpos 0.6

    "You continue walking for a very long time. {w}You’re tired, sore and parched. You feel like giving up. {w}Suddenly, there is a flash of light; the brightness almost blinds you! You see a mysterious figure standing before you. The Eternal Sage!"

    es "Young adventurers! These sands are indeed lonely to travel. "
    "You don’t know what to say or how to ask for help."
    hide deer
    "But you feel the Sight of The Eternal Sage on you. You know that they sense everything."
    show langur:
        xpos 0
    
    if endScene == "bd1":
        show stats bd1:
            xpos 0.3 ypos 0.1
    
    if endScene == "bd3":
        show stats bd3:
            xpos 0.3 ypos 0.1

    #TODO STATS Screen
    es "Young Monkey Dori, it seems you are struggling quite a bit."

    es "Being the focus of your partner's attention may seem romantic at first, but it can become too much over time. {w}It is important to maintain balance and individuality in a relationship."

    es "If you would like the opportunity to push for those boundaries, I have just the thing. {w}\n I grant you a single use of my Time Machine, a powerful relic that allows you to revisit those moments and make amends."

    p "A Time Machine? How can I ever repay you for such a gift?"

    es "You must use this gift wisely, Dori. Make an effort to have tough conversations, ask for help and listen to what you need. That will be your repayment."
    
    hide stats

    "What do you do? Do you wish to take the second chance and change the course of your story? Or do you accept and learn to live with the decisions you’ve made?"

    show langur thinking:
        xpos 0 ypos 0.24

    call screen postsurvey
    menu:
        "Use Time Machine":
            p "Thank you, Eternal Sage. I promise to use this gift responsibly and make things right."
            jump pendantResponse
        "End Game":
            return

screen postsurvey():
    frame:
        xpos 0.3
        ypos 0.2
        has vbox
        textbutton "You reached a game end! We would \nlove to hear your thoughts on the game!\n Click to open our post survey":
            xalign 0.3
            action [OpenURL("https://tinyurl.com/postdori"), Return()]

        textbutton "\n Just play again":
            # xalign 0.3
            action [Return()]
        
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




