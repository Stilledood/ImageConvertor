import PIL
from PIL import Image
from PIL import ImageEnhance ,ImageFilter


def black_and_white(image_path):
    '''Method to convert image to Black and White'''

    image=Image.open(image_path)
    image = image.convert('1')
    return image




def sharpen(image_path):

    '''Method for increase image sharppness'''

    image=Image.open(image_path)
    sharpen_image=image.filter(ImageFilter.SHARPEN)
    return sharpen_image



def increase_contrast(image):
    '''Method to increast image contrast'''

    enhancer=ImageEnhance.Contrast(image)
    factor=1.5
    high_contrast_image=enhancer.enhance(factor)
    return high_contrast_image



def decrease_contrast(image):
    '''Method to decrease image contrast'''

    enhancer=ImageEnhance.Contrast(image)
    factor=0.85
    low_contrast_image=enhancer.enhance(factor)
    return low_contrast_image


def increase_brightness(image):
    '''Method to increase image brightness'''

    enhancer=ImageEnhance.Brightness(image)
    factor=1.2
    increase_brightness_image=enhancer.enhance(factor)
    return increase_brightness_image



def decreasse_brightness(image):
    '''Method to decrease image brightness'''

    enhancer=ImageEnhance.Brightness(image)
    factor=0.8
    decreased_brightness_image=enhancer.enhance(factor)
    return decreased_brightness_image








