from PIL import Image
from filters import *
from Resize import *


image=Image.open('4.5 pikachu.jpg.jpg')

#black_and_white(image)
#sharpen(image)
#increase_contrast(image)
#decrease_contrast(image)
#increase_brightness(image)
#decreasse_brightness(image)
#medium_resize(image)

#small_resize(image)
custom_resize_by_height(image,150)






