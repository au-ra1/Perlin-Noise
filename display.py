import matplotlib.pyplot as plt

from perlin import *

#1D Normal noise plot
def normal_noise():
    list_x = []
    rand_list_y = []
    number = 0
    for i in range(100):     
        rand_list_y.append(round((np.random.uniform(0, 1)), 2))
        list_x.append(number)
        number +=1
    return list_x, rand_list_y

def noise_1D():
    list_x, rand_list_y = normal_noise()
    fig, ax = plt.subplots() 
    ax.set_xlim(0, 100)
    ax.tick_params(which='major', length=0, color='b')
    ax.set_xticklabels("")
    ax.set_yticklabels("")
    ax.plot(list_x, rand_list_y, color="black", linewidth=".5")  
    plt.show()     


#1D Perlin noise plot
def perlin_noise_1D():
    list_x, rand_list_y = normal_noise()
    fig, ax = plt.subplots() 
    ax.set_xlim(0, 100)
    ax.tick_params(which='major', length=0, color='b')
    ax.set_xticklabels("")
    ax.set_yticklabels("")
    ax.plot(list_x, rand_list_y, color="black", linewidth=".5")  
    plt.show()     


#2D Perlin noise plot
def perlin_noise_2D(size):
    np_array = np.empty((size, size))
    for i in range(size):
        for j in range(size):
            x = i / (size * 0.1)
            y = j / (size * 0.1)
            value = perlin_noise(x, y, seed=0)
            np_array[i, j] = (value + 1) / 2 


    plt.imshow(np_array, cmap="gray")
    plt.axis("off")
    plt.show()

perlin_noise_2D(255)
