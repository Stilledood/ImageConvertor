from PIL import *


def medium_resize(image):
    '''Method to reduce size of a image by 50 %'''

    width,height = image.size

    new_size_image = image.resize((width//2,height//2))
    return new_size_image


def small_resize(image):
    '''Method to reduce image size by 75 %'''

    width,height = image.size

    small_size_image = image.resize((width//4,height//4))
    return small_size_image


def custom_resize_by_width(image,width_value):
    width,height = image.size
    aspect_ratio=width/height

    new_height=int(aspect_ratio*width_value)
    new_aspect_ratio_image=image.resize((width_value,new_height))
    return new_aspect_ratio_image


def custom_resize_by_height(image,height_value):
    width,height=image.size
    aspect_ratio=width/height
    new_width=int(aspect_ratio*height_value)
    new_aspect_ratio_image=image.resize((new_width,height_value))
    return new_aspect_ratio_image



def save_file(image_file,filename,path):

    image_file=image_file.save(f"{path}/{filename}")





