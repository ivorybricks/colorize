import random
from PIL import Image


# RGB values for recoloring.
#
# Obamicon filter colors
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Sea Rose filter colors
darkLavender = (178, 129, 121)
seagreen = (103, 178, 146)
mediumPink = (255, 206, 198)
pearlPink = (255, 228, 223)

# Lime filter colors
darkGreen = (69, 178, 50)
purply = (178, 119, 161)
lighterGreen = (120, 255, 97)
lightGreen = (142, 255, 122)

# Dingy filter colors
darkOrange = (178, 118, 23)
neonishBlue = (6, 101, 178)
lighterOrange = (255, 178, 59)
lightOrange = (255, 188, 85)


# Import image.
my_image = Image.open("llama.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.

# A function called "applyFilter" which will take in four pixel values from a specific color palette and apply them to the image
def applyFilter(value1, value2, value3, value4):

    for pixel in image_list :
        pixelRGB = pixel[0] + pixel[1] + pixel[2]
        if pixelRGB < 182:
            recolored.append(value1)

        elif pixelRGB >182 and pixelRGB < 364:
            recolored.append(value2)

        elif pixelRGB > 364 and pixelRGB < 546:
            recolored.append(value3)

        else:
            recolored.append(value4)

# my_image.show()


# This will ask the user to choose the filter they want
print("Would you like the \'Obamicon\', \'Sea Rose\', \'Lime Green\' or the \'Dingy\' filter?")
filterChoice = input()

# This conditional checks which filter the user wants. Depending on the filter, it will call the "applyFilter" function
# and put in the rgb colors which apply to the filter as parameters.

if filterChoice == 'Obamicon':
    applyFilter(darkBlue, red, lightBlue, yellow)

elif filterChoice == 'Sea Rose':
    applyFilter(darkLavender, seagreen, mediumPink, pearlPink)

elif filterChoice == 'Dingy':
    applyFilter(darkOrange, neonishBlue, lighterOrange, lightOrange)

elif filterChoice == 'Lime Green':
    applyFilter(darkGreen, purply, lighterGreen, lightGreen)






# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
