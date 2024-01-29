from PIL import Image
import numpy as np

sharpen = np.array([
     [0, -1, 0], 
     [-1, 5, -1], 
     [0, -1, 0]])

image_array = np.array(Image.open("tutter.jpeg"))

def greyscale():

     for i in range(len(image_array)):
          for j in range(len(image_array[i])):
               blue = image_array[i, j, 0]
               green = image_array[i, j, 1]
               red = image_array[i, j, 2]
               gray = (red * 0.2126 + green * 0.7152 + blue * 0.0722)
               image_array [i,j] = gray

     return(image_array)
     image_array = greyscale()

new_tutter = image_array.copy()

for i in range(1, image_array.shape[0]-1):
     for j in range(1, image_array.shape[1]-1):
          subset = image_array[i-1:i+2, j-1:j+2]
          new_tutter[i, j] = np.sum(np.multiply(subset, sharpen))

new_tutter = Image.fromarray(new_tutter)
new_tutter.save('sharpen-tutter.jpeg')