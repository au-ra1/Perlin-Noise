import numpy as np
import matplotlib as plot


def assign_gradient(hash):
    gradient_vectors = [[0,1], [0, -1], [1, 0], [-1, 0]]
    a = hash
    b = a % 4
    return gradient_vectors[b]

def calculate_dot(gradient, xdv, ydv):
    return (gradient[0] * xdv) + (gradient[1] * ydv)

def lerp(a, b, x):
     return a + x * (b - a)

def fade(f):
    return 6 * f**5 - 15 * f**4 + 10 * f**3

def perlin_noise(x, y, seed=0):
    np.random.seed(seed)
    
    p = np.array((151,160,137,91,90,15,					
		131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
		190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
		88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
		77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
		102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
		135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
		5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
		223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
		129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
		251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
		49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
		138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180), dtype=int)
    
   


    np.random.shuffle(p)
  

    #find square around point
    xi = int(x) 
    yi = int(y) 
        
    #distance vectors for point value
    xdv = x - xi
    ydv = y - yi

    # hashing each corner of the square
    h00 = (p[p[xi] + yi]) #top left
    h01 = (p[p[xi] + yi + 1 ]) #top right
    h10 = (p[p[xi + 1] + yi + 1]) #bottom left
    h11 = (p[p[xi + 1] + yi] ) #bottom right
    #print(h00, h01, h10, h11)

    #assigning a pseudorandom gradient to each corner of the square
    g00 = assign_gradient(h00)
    g01 = assign_gradient(h01)
    g10 = assign_gradient(h10)
    g11 = assign_gradient(h11)
    #print(g00, g01, g10, g11)

    #calculating the dot product for each corner of the square
    d00 = calculate_dot(g00, xdv, ydv)
    d01 = calculate_dot(g01, xdv, ydv -1)
    d10 = calculate_dot(g10, xdv -1, ydv -1)
    d11 = calculate_dot(g11, xdv -1, ydv)
    #print(d00, d01, d10, d11)

    #fade/smoothing function closer to the integer
    fxdv = fade(xdv)
    fydv = fade(ydv)

    #linear interpolate the dot products (first we interpolate the top two and the bottom two to get the x-axes, then we interpolate once (bilinearly for the y))
    xtop = lerp(d00, d11, fxdv)
    xbottom = lerp(d01, d10, fxdv)
    ylerp = lerp( xtop,  xbottom, fydv)

    return (ylerp)  
    





    


