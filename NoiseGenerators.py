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



    #hash table
p = [151,160,137,91,90,15,
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
        138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]
p += p
    



 #compute the gradient vector from the hashed corner coordinates
def grad(hash):
      dir_index = hash % 4
      match (dir_index):
        case 0: return np.array([-1, 0])
        case 1: return np.array([1, 0])
        case 2: return np.array([0, 1])
        case 3: return np.array([0, -1])
           
#compute dot grad from the gradient and the distance vector
def dot_grad(gv, dv):  
     v_add = ((gv[0] * dv[0]) + (gv[1] * dv[1]))
     return v_add
     

#linear interpolation function
def lerp(a, b, c):
      return (a + c * (b - a))

# fader function to smooth the output by adjusting coordinates towards integrals
def fade(x):
      return x * x * x * (x * (x * 6 - 15) + 10)

#perlin noise
def perlin(x, y):

        #compute 4 corners around point
        x0 = int(x)
        y0 = int(y)
        x1 = x0 + 1
        y1 = y0 + 1

        #for each corner: compute interpolation points (the distance vector) 
        xdv0 = x - x0
        ydv0 = y - y0
        xdv1 = x - x1
        ydv1 = y - y1
        dv1 = np.array([xdv0,  ydv0])
        dv2 = np.array([xdv0, ydv1])
        dv3 = np.array([xdv1, ydv0])
        dv4 = np.array([xdv1, ydv1])

        #for each corner: assigns them a hash value
        xi = x0 & 255
        yi = y0 & 255  
        h00 = p[p[xi + 0] + yi + 0]
        h01 = p[p[xi + 0] + yi + 1]
        h10 = p[p[xi + 1] + yi + 0]
        h11 = p[p[xi + 1] + yi + 1]

        #compute faded values and appy to the location
        xf0f = fade(xdv0)
        yf0f = fade(ydv0)

        #compute the dot gradient of the gradient vector and the distance vector
        dg1 = dot_grad(grad(h00), dv1)
        dg2 = dot_grad(grad(h01), dv2)
        dg3 = dot_grad(grad(h10), dv3)
        dg4 = dot_grad(grad(h11), dv4)

        #linearly interpolate the dot gradients
            #x axis
        xi1 = lerp(dg2, dg4, 1)
        xi2 = lerp(dg1, dg3, 1)

        #bilinearly interpolate the final interpolation value
        yi1 = lerp(xi1, xi2, 1)
        return ((yi1 +1) /2)

arr = []
for i in range(10):
     for j in range(10):
        a = np.random.uniform(0, 1)
        b = round(perlin(i +a, j + a), 3)
        arr.append(b)
vvv = "vvv"
        #gradient vectors
        #gv1 = (1, 1)
        #gv2 = (-1, 1)
        #gv3 = (1, -1)
        #gv4 = (-1, -1)
        #further vectors
        #gv5 = (np.sqrt(2), 0)
        #gv6 = (0, np.sqrt(2))
        #gv7 = (np.sqrt(-2), 0)
        #gv8 = (0, np.sqrt(-2))



  













        
