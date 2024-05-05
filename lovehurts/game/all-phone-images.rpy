####################################################
    ############### Mobile - IMAGES ####################
####################################################

#Be sure to make all the three(3) entries for the images to work.
#1) Define the main image (what ever your renpy screen size is)
#2) Define the thumbnail
#3) Enter both of those in the List

#image lockedthumb = ("/images/mobile/messages_images/gthumbs/g_thumb_0.jpg")

#1) define main image for full screen image 1920 x 1080
image img0 = ("images/mobile/icons/blank.png") #0 is blank for no image DO NOT CHANGE
image img1 = ("images/mobile/messages_images/image_1.jpg")
image img2 = ("images/mobile/messages_images/image_2.jpg")
#image img3 = ("images/mobile/messages_images/image_3.jpg")
#image img4 = ("images/mobile/messages_images/image_4.jpg")

#add more here as needed increasing the numbers

#2) define small image to be shown on phone screen check the size of the thumb
#use your 1920 x 1080 image and resize it to 258 x 145 (still a 16 x 9 format)
image thumb0 = ("images/mobile/icons/blank.png") # DO NOT CHANGE
image thumb1 = ("images/mobile/messages_images/thumbs/p_thumb_1.jpg")
image thumb2 = ("images/mobile/messages_images/thumbs/p_thumb_2.jpg")
#image thumb3 = ("images/mobile/messages_images/thumbs/p_thumb_3.jpg")
#image thumb4 = ("images/mobile/messages_images/thumbs/p_thumb_4.jpg")

#add more here as needed increasing the numbers

#3) put everything in a python list (just like the messages, because I know to do these!)
init python:
    closeup_page = 0
    class phoneItem:
        def __init__(self, images, thumb):
            self.images = images
            self.thumb = thumb

    phone_images = []
    phone_images.append (phoneItem(["img0"], "thumb0"))
    phone_images.append (phoneItem(["img1"], "thumb1"))
    phone_images.append (phoneItem(["img2"], "thumb2"))
#    phone_images.append (phoneItem(["img3"], "thumb3"))
#    phone_images.append (phoneItem(["img4"], "thumb4"))

#add more here as needed increasing the numbers
