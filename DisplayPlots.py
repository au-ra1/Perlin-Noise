import matplotlib.pyplot as plt

from NoiseGenerators import *

#1D Normal noise plot
list_x, rand_list_y = normal_noise()
def normal_noise_plot():
    fig, ax = plt.subplots() 
    ax.set_xlim(0, 100)
    ax.tick_params(which='major', length=0, color='b')
    ax.set_xticklabels("")
    ax.set_yticklabels("")
    ax.plot(list_x, rand_list_y, color="black", linewidth=".5")  
    plt.show()     
#normal_noise_plot()

#1D Perlin noise plot
def perlin_noise_plot():
    fig, ax = plt.subplots() 
    ax.set_xlim(0, 100)
    ax.tick_params(which='major', length=0, color='b')
    ax.set_xticklabels("")
    ax.set_yticklabels("")
    ax.plot(list_x, rand_list_y, color="black", linewidth=".5")  
    plt.show()     


#2D Perlin noise plot
def perlin_noise_2D():
    width = 512
    height = 512
    





    plt.imshow(noise_grid, cmap='gray')
    plt.colorbar()
    plt.show()

perlin_noise_2D()