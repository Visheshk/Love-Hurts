####################################################
    ############### Mobile - MESSAGES ####################
####################################################

# Yes I got lazy with the messages, I made 5 then copied pasted that 3 time for 20 total

init python:
    class messageitem:
        def __init__(self, message, fromMC, selfie):
            self.message = message
            self.fromMC = fromMC
            self.selfie = selfie

    girl1_message = [] #This is the list holder it is REQUIRED one for each girl

    #format  -->  girls-number-here_message.append(messageitem("all the text you want", (True or False), a number)) #a number 0 = no image, or the image number 1,2,3 image1 - 1million++ are setup in the all-phone-images.rpy file

    #which girl by number             a message      , from the MC(T or F), image number 0=no attached image
    #girl1_message.append(messageitem("The Message here", True, 0))

    #first message you can apppend the name_message in game as you go along or add them all here. If in game then add $ before (first message can be from the MC as well.)
    girl1_message.append(messageitem("This is the first message that we sent to girl1", True, 0))
    #second message
    girl1_message.append(messageitem("Hi [player_name], How do I look?\nxxx\nClick image for full screen.", False, 1)) #she sent an image !!
    girl1_message.append(messageitem("Better than my X. Here's a picture of my X GF.", True, 2))
    girl1_message.append(messageitem("Hi [player_name], She's pretty, why did you two break up?", False, 0))
    girl1_message.append(messageitem("You're not some raging psychopathy are you? J/K your sister told me all about you.", False, 0))
    girl1_message.append(messageitem("This is the first message that we sent to girl1", True, 0))
    girl1_message.append(messageitem("Hi [player_name], How do I look?\nxxx\nClick image for full screen.", False, 1))
    girl1_message.append(messageitem("Better than my X. Here's a picture of my X GF.", True, 2))
    girl1_message.append(messageitem("Hi [player_name], She's pretty, why did you two break up?", False, 0))
    girl1_message.append(messageitem("You're not some raging psychopathy are you? J/K your sister told me all about you.", False, 0))
    girl1_message.append(messageitem("This is the first message that we sent to girl1", True, 0))
    girl1_message.append(messageitem("Hi [player_name], How do I look?\nxxx\nClick image for full screen.", False, 1))
    girl1_message.append(messageitem("Better than my X. Here's a picture of my X GF.", True, 2))
    girl1_message.append(messageitem("Hi [player_name], She's pretty, why did you two break up?", False, 0))
    girl1_message.append(messageitem("You're not some raging psychopathy are you? J/K your sister told me all about you.", False, 0))
    girl1_message.append(messageitem("This is the first message that we sent to girl1", True, 0))
    girl1_message.append(messageitem("Hi [player_name], How do I look?\nxxx\nClick image for full screen.", False, 1))
    girl1_message.append(messageitem("Better than my X. Here's a picture of my X GF.", True, 2))
    girl1_message.append(messageitem("Hi [player_name], She's pretty, why did you two break up?", False, 0))
    girl1_message.append(messageitem("You're not some raging psychopathy are you? J/K your sister told me all about you.", False, 0))
    girl1_message.append(messageitem("This is the first message that we sent to girl1", True, 0))
    girl1_message.append(messageitem("Hi [player_name], How do I look?\nxxx\nClick image for full screen.",  False, 1))
    girl1_message.append(messageitem("Better than my X. Here's a picture of my X GF.", True, 2))
    girl1_message.append(messageitem("Hi [player_name], She's pretty, why did you two break up?",  False, 0))
    girl1_message.append(messageitem("You're not some raging psychopathy are you? J/K your sister told me all about you.", False, 0))
    


    girl2_message = []
    #first
    girl2_message.append(messageitem("Hey [player_name], it's been 3 days how come you haven't called me yet?",
    False, 0))
    #second message
    girl2_message.append(messageitem("Would you believe I have been to busy, but I was going to call you tomorrow.",
    True, 0))



    girl3_message = []

    girl4_message = [] #I hope you have it figured out by now!!
