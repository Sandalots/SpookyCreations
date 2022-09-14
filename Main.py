import os
import random
from PIL import Image

path = './images'  # in case the folder is in the same directory as the script
files = os.listdir(path)  # listdir gives you a list with all filenames in the provided path.
randomFile = random.choice(files)

if randomFile == "Main.py":
    randomFile = random.choice(files) # random.choice then selects a random file from your list

print(randomFile) #  prints the random filename

image = Image.open(path + '/' + randomFile)  # displayed the image
image.show()