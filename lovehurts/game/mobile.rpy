####################################################
    ############### Mobile - PHONE ####################
####################################################


####################################################
    ############### MUSIC - SONGS ####################
####################################################

default mouse_xy = (0, 0)

default songplaying = 0
default musicpaused = 1
default phonebackground = 1
default bg1 = True
default bg2 = False
default bg3 = False
default bg4 = False
default bg5 = False
default bg6 = False
default bg7 = False
default bg8 = False
default bg9 = False

############ Girl 1 Setup ############
default girl1_name = "BadMustard1"
default girl1_phone = False
default girl1_love = 1
default girl1_lust = 2
default girl1_dominance = 3
default girl1_submissive = 4
default girl1_pregnant = "Yes"
default girl1_msg_count = 0
############ Girl 1 Stop ############

############ Girl 2 Setup ############
default girl2_name = "11 char Max"
default girl2_phone = False
default girl2_love = 4
default girl2_lust = 3
default girl2_dominance = 2
default girl2_submissive = 1
default girl2_pregnant = "No"
default girl2_msg_count = 0
############ Girl 2 Stop ############

############ Girl 3 Setup ############
default girl3_name = "BadMustard3"
default girl3_phone = False
default girl3_love = 1
default girl3_lust = 2
default girl3_dominance = 3
default girl3_submissive = 4
default girl3_pregnant = "Yes"
default girl3_msg_count = 0
############ Girl 1 Stop ############

############ Girl 4 Setup ############
default girl4_name = "BadMustard4"
default girl4_phone = False
default girl4_love = 1
default girl4_lust = 2
default girl4_dominance = 3
default girl4_submissive = 4
default girl4_pregnant = "Yes"
default girl4_msg_count = 0
############ Girl 1 Stop ############

default girl5_phone = False
default girl6_phone = False
default girl7_phone = False
default girl8_phone = False
default girl9_phone = False
default girl10_phone = False
default girl11_phone = False
default girl12_phone = False
default girl13_phone = False
default girl14_phone = False
default girl15_phone = False


init python:
    mr = MusicRoom(fadeout=0.6)
    mr.add("audio/music/Nehilo - Alone.mp3", always_unlocked=True)
    mr.add("audio/music/Alfonso Lugo - Latinas feat. Vince Miranda.mp3", always_unlocked=True)
    mr.add("audio/music/Offenbach Project - Dreamy.mp3", always_unlocked=True)
    mr.add("audio/music/Square a Saw - Meant To Be This Way.mp3", always_unlocked=True)
    mr.add("audio/music/The Same Persons- Dance with me.mp3",always_unlocked=True)

    def get_mouse():
        global mouse_xy
        mouse_xy = renpy.get_mouse_pos()

style volumebar:
    right_bar "images/Mobile/mroom/volumebar.png"
    left_bar "images/Mobile/mroom/volumebar.png"
    thumb "images/Mobile/mroom/volumeicon.png"
    thumb_offset 10

transform phonepos:
    xalign 1.0
    yalign 0.005

####################################################
    ############### Display On and Off ####################
####################################################

label phone_on: #call this label the give player the phone
    show screen phoneaway
    return

label phone_off: #call this to turn the phone off
    hide screen relationships
    hide screen wallpapers
    hide screen phone
    hide screen phoneaway
    hide screen central_stats
    hide screen central_message
    stop music
    return

screen phoneaway(): #small phone hides on the right side of the screen
    zorder 100
    imagebutton:
        xalign 1.0
        yalign 0.005
        auto "Mobile/Buttons/phone_%s.png"
        action [Hide("phoneaway"), Show("phone")] #action NullAction()

screen phone_closeup(pictar):
    zorder 1
    imagebutton idle pictar:
        action Hide("phone_closeup", dissolve)
        xalign 0.5
        yalign 1.0
        background "#fff8"

label phonePal(girl, name, love, lust, dominance, submissive, pregnant):
    show screen central_stats(girl, name, love, lust, dominance, submissive, pregnant)
    return

####################################################
    ############### PHONE 1st screen ####################
####################################################

screen phone(): #full phone display
    zorder 1
    modal True
    add "Mobile/Backgrounds/phone_bg[phonebackground].png" at phonepos

    imagebutton:
        xalign 0.92
        yalign 0.615
        auto "Mobile/Buttons/phone_middle_button_%s.png"
        action [Hide("phone"),Hide("messages"),Hide("musicplay"),Hide("relationships"),Hide("wallpapers"), Show("phoneaway")]

    imagebutton:
        xalign 0.87
        yalign 0.1
        auto "Mobile/Icons/subscribestar_icon_%s.png"
        action OpenURL("https://subscribestar.adult/cr8tive-m3dia")
        tooltip "SubscribeStar"

    imagebutton:
        xalign 0.925
        yalign 0.1
        auto "Mobile/Icons/discord_icon_%s.png"
        action OpenURL("https://discord.gg/UE9aPVrdNy")
        tooltip "Discord"

    imagebutton:
        xalign 0.98
        yalign 0.1
        auto "Mobile/Icons/patreon_icon_%s.png"
        action OpenURL("https://www.patreon.com/cr8tivem3dia")
        tooltip "Patreon"

    imagebutton:
        xalign 0.87
        yalign 0.18
        auto "Mobile/Icons/buy_coffee_%s.png"
        action OpenURL("https://www.buymeacoffee.com/BadMustard")
        tooltip "Buy Me Coffee"

    imagebutton: #GALLERY button if you have a gallery
        xalign 0.925
        yalign 0.18
        auto "Mobile/Icons/gallery_icon_%s.png"
        #action ShowMenu("gallery")
        tooltip "Gallery"

    imagebutton: #Change the wallpaper
        xalign 0.98
        yalign 0.18
        auto "mobile/icons/wallpaper_icon_%s.png"
        action [Hide("phone"), Show("wallpapers")]
        tooltip "Wallpapers"

#to add more image buttons
#    imagebutton:
#        xalign 0.87 0.925 or 0.98
#        yalign 0.26 0.34 .42(max)
#        idle "mobile/icons/something.png.jpg"
#        hover "mobile.icons/something to show movement.jpg.png"
#        action Hide("phone"), Show("another screen")

    imagebutton: #messages
        xalign 0.86
        yalign 0.55
        auto "Mobile/Icons/message_icon_%s.png"
        action [Hide("phone"),Show("messages")]
        tooltip "Messages"

    imagebutton: #money check
        xalign 0.9
        yalign 0.55
        auto "Mobile/Icons/money_icon_%s.png"
        action [Hide("phone"),Show("money")]
        tooltip "Finances"

    imagebutton: #music player
        xalign 0.94
        yalign 0.55
        auto "Mobile/Icons/music_icon_%s.png"
        action [Hide("phone"),Show("musicplay")]
        tooltip "Music"

    imagebutton: #relationships stats
        xalign 0.98
        yalign 0.55
        auto "Mobile/Icons/relationship_icon_%s.png"
        action [Hide("phone"),Show("relationships")]
        tooltip "Relationships"

    $ tooltip = GetTooltip()

    if tooltip:
        timer 0.1 repeat True action Function(get_mouse)
        $ mx = mouse_xy[0] - 30 # LR
        $ my = mouse_xy[1] + 30 # UD
        text tooltip:
            pos(mx, my)
            color "#fff"
            size 15
            outlines [(2, "#000005", 0, 0)]

####################################################
    ############### Relationships - Stats ####################
####################################################

screen relationships(): ##page 1 of 6
    zorder 1
    modal True
    add "Mobile/Backgrounds/phone_bg[phonebackground].png" at phonepos

    imagebutton:
        xalign 0.92
        yalign 0.615
        auto "Mobile/Buttons/phone_middle_button_%s.png"
        action [Hide("relationships"),Hide("wallpapers"),Show("phone")]

    viewport:
        spacing 20
        ymaximum 475
        xmaximum 293
        draggable True
        mousewheel True
        scrollbars "vertical"
        side_xalign 0.988
        side_yalign 0.165
        has hbox:
            spacing 10
            box_wrap True
            box_wrap_spacing 10
            
        if girl1_phone:
            imagebutton:
                auto "mobile/icons/girl1_icon_%s.png"
                action [Hide("relationships"), Call("phonePal", 1, girl1_name, girl1_love, girl1_lust, girl1_dominance, girl1_submissive, girl1_pregnant)]
                tooltip "[girl1_name]"

        if girl2_phone:
            imagebutton:
                auto "mobile/icons/girl2_icon_%s.png"
                action [Hide("relationships"), Call("phonePal", 2, girl2_name, girl2_love, girl2_lust, girl2_dominance, girl2_submissive, girl2_pregnant)]
                tooltip "[girl2_name]"

        if girl3_phone:
            imagebutton:
                auto "Mobile/Icons/girl3_icon_%s.png"
                action [Hide("relationships"), Call("phonePal", 3, girl3_name, girl3_love, girl3_lust, girl3_dominance, girl3_submissive, girl3_pregnant)]
                tooltip "[girl3_name]"

        if girl4_phone:
            imagebutton:
                auto "Mobile/Icons/girl4_icon_%s.png"
                action [Hide("relationships"), Call("phonePal", 4, girl4_name, girl4_love, girl4_lust, girl4_dominance, girl4_submissive, girl4_pregnant)]
                tooltip "[girl4_name]"

        if girl5_phone:
            imagebutton:
                auto "Mobile/Icons/girl5_icon_%s.png"
                action [Hide("relationships"), Call("phonePal", 5, girl5_name, girl5_love, girl5_lust, girl5_dominance, girl5_submissive, girl5_pregnant)]
                tooltip "[girl5_name]"

        if girl6_phone:
            imagebutton:
                auto "Mobile/Icons/girl6_icon_%s.png"
                action [Hide("relationships"), Call("phonePal", 6, girl6_name, girl6_love, girl6_lust, girl6_dominance, girl6_submissive, girl6_pregnant)]
                tooltip "[girl6_name]"

        if girl7_phone:
            imagebutton:
                auto "Mobile/Icons/girl7_icon_%s.png"
                action [Hide("relationships"), Call("phonePal", 7, girl7_name, girl7_love, girl7_lust, girl7_dominance, girl7_submissive, girl7_pregnant)]
                tooltip "[girl7_name]"

        if girl8_phone:
            imagebutton:
                auto "Mobile/Icons/girl8_icon_%s.png"
                action [Hide("relationships"), Call("phonePal", 8, girl8_name, girl8_love, girl8_lust, girl8_dominance, girl8_submissive, girl8_pregnant)]
                tooltip "[girl8_name]"

        if girl9_phone:
            imagebutton:
                auto "Mobile/Icons/girl9_icon_%s.png"
                action [Hide("relationships"), Call("phonePal", 9, girl9_name, girl9_love, girl9_lust, girl9_dominance, girl9_submissive, girl9_pregnant)]
                tooltip "[girl9_name]"

        if girl10_phone:
            imagebutton:
                auto "Mobile/Icons/girl10_icon_%s.png"
                action [Hide("relationships"), Call("phonePal", 10, girl10_name, girl10_love, girl10_lust, girl10_dominance, girl10_submissive, girl10_pregnant)]
                tooltip "[girl10_name]"

        #add more here as required!!

    $ tooltip = GetTooltip()

    if tooltip:
        timer 0.1 repeat True action Function(get_mouse)
        $ mx = mouse_xy[0] - 30 # LR
        $ my = mouse_xy[1] + 30 # UD
        text tooltip:
            pos(mx, my)
            color "#fff"
            size 15
            outlines [(2, "#000005", 0, 0)]

########## Relationships - Stats stop ###########

####################################################
    ############### Centralized Character Stats start ####################
####################################################

screen central_stats(girl, name, love, lust, dominance, submissive, pregnant):
    zorder 1
    modal True
    add "mobile/backgrounds/phone_bg[phonebackground].png" at phonepos 
    #$ print(girl)
    add "mobile/stats_bg/girl[girl]_bg.png" at phonepos

    imagebutton:
        xalign 0.92
        yalign 0.615
        auto "Mobile/Buttons/phone_middle_button_%s.png"
        action [Hide("central_stats"),Hide("wallpapers"), Show("relationships")]

    vbox:
        style_prefix "stats_style"
        xalign 0.98
        yalign 0.4
        textbutton "[name]'s\nStats"
        hbox:
            vbox:
                text "Love"
                text "Lust"
                text "Dominance"
                text "Submission"
                text "Pregnant"
            vbox:

                text "   [love]"
                text "   [lust]"
                text "   [dominance]"
                text "   [submissive]"
                text "   [pregnant]"

########## Centralized Character Stats stop ###########

####################################################
    ############### Finances Start####################
####################################################

screen money(): ##Finances
    zorder 1
    modal True
    add "Mobile/Backgrounds/phone_finance_bg.png" at phonepos

    imagebutton:
        xalign 0.92
        yalign 0.615
        auto "Mobile/Buttons/phone_middle_button_%s.png"
        action Hide("money"), Show("phone")

    vbox:
        xalign 0.97
        yalign 0.3
        style_prefix "money_style"
        textbutton "£[money]"
        text ""
        text ""
        hbox:
            vbox:
                text "{color=#000000}Shares{/color}"
                text ""
                text "{color=#000000}Income{/color}"
                text "{color=#000000}Expenses{/color}"
            vbox:
                text "   £[share_value]"
                text ""
                text "   £[income]"
                text "   £[costs]"

########## Finances Stop ###########

####################################################
    ############### Music Room ###############
####################################################

transform plus_size:
    zoom 1.5

screen musicplay():
    zorder 1
    modal True
    add "Mobile/Backgrounds/phone_musicroom.png" at phonepos

    imagebutton:
        xalign 0.92
        yalign 0.615
        auto "Mobile/Buttons/phone_middle_button_%s.png"
        action Hide("musicplay"), Show("phone")

    bar:
        style "volumebar"
        value Preference("music volume")
        xalign 0.955
        yalign 0.425
        xysize (202, 35)

    vbox:
        xalign 0.969
        yalign 0.12
        style_prefix "music_style"
        text "Nehilo - Alone"
        text "Alfonso Lugo - Latinas feat. Vince Miranda"
        text "Offenbach Project - Dreamy"
        text "Square a Saw - Meant To Be This Way"
        text "The Same Persons- Dance with me"

    bar:
        value AudioPositionValue(channel='music')
        xpos 1620
        ypos 400
        ysize 20
        xsize 250
        # xmaximum 250

    imagebutton:
        xalign 0.882
        yalign 0.49
        auto "Mobile/mroom/mroom_back_icon_%s.png" 
        action If(songplaying == 0, mr.Previous())

    imagebutton:
        xalign 0.906
        yalign 0.49
        auto "Mobile/mroom/mroom_play_icon_%s.png"
        action mr.Play()

    imagebutton:
        xalign 0.930
        yalign 0.49
        auto "Mobile/mroom/mroom_stop_icon_%s.png"
        action mr.Stop()

    imagebutton:
        xalign 0.953
        yalign 0.49
        auto "Mobile/mroom/mroom_forward_icon_%s.png"
        action mr.Next()

    imagebutton:
        xalign 0.952
        yalign 0.54
        auto "Mobile/mroom/mroom_loop_icon_%s.png"
        action mr.SetLoop(1)

    imagebutton:
        xalign 0.892
        yalign 0.54
        auto "Mobile/mroom/mroom_shuffle_icon_%s.png"
        action mr.RandomPlay()

########## Music Room Stop ###########

####################################################
    ############### Message System ###############
####################################################

screen messages():
    zorder 1
    modal True
    add "Mobile/Backgrounds/phone_msg_bg1.png" at phonepos

    imagebutton:
        xalign 0.92
        yalign 0.615
        auto "Mobile/Buttons/phone_middle_button_%s.png"
        action Hide("messages"), Show("phone")

    vpgrid:

        cols 1
        rows 15 #10 per screen 6 screens max 60 change when adding more if statements below
        spacing 8
        ymaximum 400
        xmaximum 290
        draggable True
        mousewheel True
        scrollbars "vertical"
        side_xalign 0.982
        side_yalign 0.27

        if girl1_phone:
            imagebutton:
                auto "Mobile/Icons/girl1_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl1_msg_count, girl=1, messageholder=girl1_message, gname=girl1_name)]
                #new action requires girls to have numbers !!
                #the number of messages, her number, the list the messages are stored in
        else:
            null

        if girl2_phone:
            imagebutton:
                auto "Mobile/Icons/girl2_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl2_msg_count, girl=2, messageholder=girl2_message, gname=girl2_name)]
        else:
            null

        if girl3_phone:
            imagebutton:
                auto "Mobile/Icons/girl3_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl3_msg_count, girl=3, messageholder=girl3_message, gname=girl3_name)]
        else:
            null

        if girl4_phone:
            imagebutton:
                auto "Mobile/Icons/girl4_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl4_msg_count, girl=4, messageholder=girl4_message, gname=girl4_name)]
        else:
            null

        if girl5_phone:
            imagebutton:
                auto "Mobile/Icons/girl5_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl5_msg_count, girl=5, messageholder=girl5_message, gname=girl5_name)]
        else:
            null

        if girl6_phone:
            imagebutton:
                auto "Mobile/Icons/girl6_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl6_msg_count, girl=6, messageholder=girl6_message, gname=girl6_name)]
        else:
            null

        if girl7_phone:
            imagebutton:
                auto "Mobile/Icons/girl7_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl7_msg_count, girl=7, messageholder=girl7_message, gname=girl7_name)]
        else:
            null

        if girl8_phone:
            imagebutton:
                auto "Mobile/Icons/girl8_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl8_msg_count, girl=8, messageholder=girl8_message, gname=girl8_name)]
        else:
            null

        if girl9_phone:
            imagebutton:
                auto "Mobile/Icons/girl9_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl9_msg_count, girl=9, messageholder=girl9_message, gname=girl9_name)]
        else:
            null

        if girl10_phone:
            imagebutton:
                auto "Mobile/Icons/girl10_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl10_msg_count, girl=10, messageholder=girl10_message, gname=girl10_name)]
        else:
            null

        if girl11_phone:
            imagebutton:
                auto "Mobile/Icons/girl11_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl11_msg_count, girl=11, messageholder=girl11_message, gname=girl11_name)]
        else:
            null

        if girl12_phone:
            imagebutton:
                auto "Mobile/Icons/girl12_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl12_msg_count, girl=12, messageholder=girl12_message, gname=girl12_name)]
        else:
            null

        if girl13_phone:
            imagebutton:
                auto "Mobile/Icons/girl13_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl13_msg_count, girl=13, messageholder=girl13_message, gname=girl13_name)]
        else:
            null

        if girl14_phone:
            imagebutton:
                auto "Mobile/Icons/girl14_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl14_msg_count, girl=14, messageholder=girl14_message, gname=girl14_name)]
        else:
            null

        if girl15_phone:
            imagebutton:
                auto "Mobile/Icons/girl15_msg_icon_%s.png"
                action [Hide("messages"), Show ("central_message", count=girl15_msg_count, girl=15, messageholder=girl15_message, gname=girl15_name)]
        else:
            null
### if you add more girls here be sure to increase the rows for the VPgrid  above

########## Message System Stop ###########

####################################################
    ########## Central Message Start ###########
####################################################

screen central_message(count, girl, messageholder, gname):
    zorder 1
    modal True
    add "Mobile/Backgrounds/phone_msg_bg2.png" at phonepos
    add "Mobile/Icons/girl[girl]_msg_icon_sign.png":
        xalign 0.979
        yalign 0.095
    text "[gname]":
        color "#000000"
        xalign 0.979
        yalign 0.095
    imagebutton:
        xalign 0.92
        yalign 0.615
        auto "Mobile/Buttons/phone_middle_button_%s.png"
        action [Hide("central_message"), Show("messages")]

    vpgrid:
        cols 1
        rows 1
        ymaximum 405
        xmaximum 285
        mousewheel True
        scrollbars "vertical"
        side_xalign 0.982
        side_yalign 0.27
        yfill False
        xfill False
        yinitial 1.0

        hbox:
            style_prefix "msg_style"
            vbox:
                spacing 5
                for i in range(0, count):
                    frame:
                        if messageholder[i].fromMC:
                            background Frame("images/mobile/backgrounds/sent_background.png", 0,0,0,0)
                        else:
                            background Frame("images/mobile/backgrounds/received_background.png", 0,0,0,0)
                        vbox:
                            xsize 250
                            if messageholder[i].fromMC:
                                add "images/mobile/backgrounds/nuggetR.png" size (16, 16) xalign 1.0 yalign 0.0
                            else:
                                add "images/mobile/backgrounds/nuggetL.png" size (16, 16) xalign 0.0 yalign 0.0
                            text messageholder[i].message

                            if messageholder[i].selfie > 0:
                            #BadMustard 0 = no image 1 - 1million = an image from the list
                                #use the thumb for the button
                                imagebutton idle phone_images[messageholder[i].selfie].thumb:
                                    action Show("phone_closeup", dissolve, phone_images[messageholder[i].selfie].images)
                                    xalign 0.5
                                    yalign 0
 
########## Central Message Stop ###########

####################################################
    ############### Phone Wallpaper System ###############
####################################################

screen wallpapers():
    zorder 1
    modal True
    add "Mobile/Backgrounds/phone_bg[phonebackground].png" at phonepos

    imagebutton:
        xalign 0.92
        yalign 0.615
        auto "Mobile/Buttons/phone_middle_button_%s.png"
        action Hide("messages"), Show("phone")

    hbox:
        xalign 0.974
        yalign 0.1
        spacing 20

        vbox:
            imagebutton:
                xalign 0.5
                yalign 0.5
                if bg1:
                    idle "mobile/backgrounds/bg_select_1.jpg"
                    action Hide ("wallpapers"), SetVariable("phonebackground", 1), Show("phone")
                else:
                    idle "mobile/backgrounds/bg_select_lock.png"
                    action NullAction()

        vbox:
            imagebutton:
                xalign 0.5
                yalign 0.5
                if bg2:
                    idle "mobile/backgrounds/bg_select_2.jpg"
                    action Hide ("wallpapers"), SetVariable("phonebackground", 2), Show("phone")
                else:
                    idle "mobile/backgrounds/bg_select_lock.png"
                    action NullAction()

        vbox:
            imagebutton:
                xalign 0.5
                yalign 0.5
                if bg3:
                    idle "mobile/backgrounds/bg_select_3.jpg"
                    action Hide ("wallpapers"), SetVariable("phonebackground", 3), Show("phone")
                else:
                    idle "mobile/backgrounds/bg_select_lock.png"
                    action NullAction()

    hbox:
        xalign 0.974
        yalign 0.3
        spacing 20

        vbox:
            imagebutton:
                xalign 0.5
                yalign 0.5
                if bg4:
                    idle "mobile/backgrounds/bg_select_1.jpg"
                    action Hide ("wallpapers"), SetVariable("phonebackground", 1), Show("phone")
                else:
                    idle "mobile/backgrounds/bg_select_lock.png"
                    action NullAction()

        vbox:
            imagebutton:
                xalign 0.5
                yalign 0.5
                if bg5:
                    idle "mobile/backgrounds/bg_select_2.jpg"
                    action Hide ("wallpapers"), SetVariable("phonebackground", 2), Show("phone")
                else:
                    idle "mobile/backgrounds/bg_select_lock.png"
                    action NullAction()

        vbox:
            imagebutton:
                xalign 0.5
                yalign 0.5
                if bg6:
                    idle "mobile/backgrounds/bg_select_3.jpg"
                    action Hide ("wallpapers"), SetVariable("phonebackground", 3), Show("phone")
                else:
                    idle "mobile/backgrounds/bg_select_lock.png"
                    action NullAction()

    hbox:
        xalign 0.974
        yalign 0.5
        spacing 20

        vbox:
            imagebutton:
                xalign 0.5
                yalign 0.5
                if bg7:
                    idle "mobile/backgrounds/bg_select_4.jpg"
                    action Hide ("wallpapers"), SetVariable("phonebackground", 4), Show("phone")
                else:
                    idle "mobile/backgrounds/bg_select_lock.png"
                    action NullAction()

        vbox:
            imagebutton:
                xalign 0.5
                yalign 0.5
                if bg8:
                    idle "mobile/backgrounds/bg_select_4.jpg"
                    action Hide ("wallpapers"), SetVariable("phonebackground", 4), Show("phone")
                else:
                    idle "mobile/backgrounds/bg_select_lock.png"
                    action NullAction()

        vbox:
            imagebutton:
                xalign 0.5
                yalign 0.5
                if bg9:
                    idle "mobile/backgrounds/bg_select_4.jpg"
                    action Hide ("wallpapers"), SetVariable("phonebackground", 4), Show("phone")
                else:
                    idle "mobile/backgrounds/bg_select_lock.png"
                    action NullAction()

########## Phone Wallpaper System stop ###########

####################################################
    ########### Assorted Styles ###########
####################################################
init 5:

    style stats_style_button_text:
        bold True
        underline True
        color "#ffffff"

    style msg_style_text:
        color "#1A3299"
        size 18

    style money_style_text:
        color "#084812"

    style money_style_button_text:
        color "#084812"

    style music_style_text:
        color "#2EEBED"
        size 12

    style phone_reply:
        size 12
        xalign 0.5
        xsize 284
        background Solid("#58E8A0") #menu button color
        hover_background Solid("#78E8A0") #menu button color change mouse over change color
        ypadding 10
        xpadding 10

    style phone_reply_text:
        xalign 0.5
        size 25 #font size
        color ("#3da1f3") #font color

########## Assorted Styles stop ###########

####################################################
    ########### Input Screens start ###########
####################################################

screen phone_reply(reply1, label1, reply2, label2, girl, gname, phoneQuestion):
    on "show" action Hide("phoneaway")
    modal True
    add "Mobile/Backgrounds/phone_msg_bg2.png" at phonepos
    add "Mobile/Icons/girl[girl]_msg_icon_sign.png":
        xalign 0.979
        yalign 0.095
    imagebutton:
        xalign 0.92
        yalign 0.615
        auto "Mobile/Buttons/phone_middle_button_%s.png"
        action [Hide("phone_reply"), Show("phoneaway")]
    text "[gname]":
        color "#000000"
        xalign 0.979
        yalign 0.095

    frame:
        xalign 0.980
        yalign 0.17
        background Frame("images/mobile/backgrounds/received_background.png", 0,0,0,0)
        vbox:
            style_prefix "msg_style"
            xsize 270
            add "images/mobile/backgrounds/nuggetL.png" size (16, 16) xalign 0.0 yalign 1.0
            text phoneQuestion

    vbox:
        xalign 0.98
        yalign 0.4
        spacing 5

        textbutton "[reply1]" action [Hide("phone_reply"), Show("phoneaway"), Jump(label1)] style "phone_reply"
        textbutton "[reply2]" action [Hide("phone_reply"), Show("phoneaway"), Jump(label2)] style "phone_reply"

screen phone_reply3(reply1, label1, reply2, label2, reply3, label3, girl, gname, phoneQuestion):
    on "show" action Hide("phoneaway")
    modal True
    add "Mobile/Backgrounds/phone_msg_bg2.png" at phonepos
    add "Mobile/Icons/girl[girl]_msg_icon_sign.png":
        xalign 0.979
        yalign 0.095
    imagebutton:
        xalign 0.92
        yalign 0.615
        auto "Mobile/Buttons/phone_middle_button_%s.png"
        action [Hide("phone_reply"), Show("phoneaway")]
    text "[gname]":
        color "#000000"
        xalign 0.979
        yalign 0.095

    frame:
        xalign 0.980
        yalign 0.17
        background Frame("images/mobile/backgrounds/received_background.png", 0,0,0,0)
        vbox:
            style_prefix "msg_style"
            xsize 270
            add "images/mobile/backgrounds/nuggetL.png" size (16, 16) xalign 0.0 yalign 1.0
            text phoneQuestion

    vbox:
        xalign 0.98
        yalign 0.4
        spacing 5

        textbutton "[reply1]" action [Hide("phone_reply3"), Show("phoneaway"), Jump(label1)] style "phone_reply"
        textbutton "[reply2]" action [Hide("phone_reply3"), Show("phoneaway"), Jump(label2)] style "phone_reply"
        textbutton "[reply3]" action [Hide("phone_reply3"), Show("phoneaway"), Jump(label3)] style "phone_reply"
