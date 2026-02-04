import numpy as np

# 1D normal noise
def normal_noise():
    list_x = []
    rand_list_y = []
    number = 0
    for i in range(100):     
        rand_list_y.append(round((np.random.uniform(0, 1)), 2))
        list_x.append(number)
        number +=1
    return list_x, rand_list_y

#perlin noise at coordinates x, y
def perlin(x, y):
    x0 = x
    y0 = y
    x1 = x + 1
    y1 = y + 1



class Perlin2D:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    
