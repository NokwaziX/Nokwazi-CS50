'''
implement a program that expects exactly two command-line arguments:

** in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
** in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should instead exit via sys.exit:

** if the user does not specify exactly two command-line arguments,
** if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
** if the input’s name does not have the same extension as the output’s name, or
** if the specified input does not exist.

Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.

'''
import sys
from PIL import Image, ImageOps
from os.path import splitext

def main():
    check_command_line_arg()

    #Open image of muppet before they get shirt
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist!')

    shirtfile = Image.open('shirt.png')     #Open shirt image
    size = shirtfile.size                   #Get size of shirt
    muppet = ImageOps.fit(imagefile, size)  #Resize muppet img so shirt fits
    muppet.paste(shirtfile,shirtfile)       #Paste shirt on muppet
    muppet.save(sys.argv[2])                #Create ouptput image



#*********************************************************************************

def check_command_line_arg():

    #check if the user inputted 2 arg after program name in cmnd line
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments!')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments!')

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])


    #We check if file is an image
    if check_extension(file1[1]) == False or check_extension(file2[1]) == False:
        sys.exit('Inavalid input!')
    #We check if both files have same extension
    if file1[1].lower() != file2[1].lower():
        sys.exit('Input and Output have different extensions!')


def check_extension(file):
    if file in ['.jpg', '.jpeg', '.png']:
        return True
    return False

'''
    #check if user inputted a image file
    if '.jpg' not in sys.argv[1] or '.jpg' not in sys.argv[2]:
        sys.exit('Invalid output!')
    elif
'''


if __name__ == '__main__':
    main()