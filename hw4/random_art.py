# -*- coding: utf-8 -*-
"""
Random_art.py

@author: amonmillner, adapted from pruvolo work
"""

# you do not have to use these particular modules, but they may help
import random
import math
import Image

# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 19:43:22 2014

@author: abigail
"""
from random import randint
from PIL import Image

min_depth = 4
max_depth = 40
def build_random_function(min_depth, max_depth):
    """This function takes in a minimum and maximum depth and generates a pseudo
    function with all the types of functions I have chosen, which include product,
    cubed function, cosine function, sine function and sin of (pi*argument)
    """
    if min_depth > 0: #sets the min_depth to 0 so that it doesn't interfere with the code
        max_depth = randint(min_depth,max_depth) #set max_depth to the actual depth of function generated
        min_depth = 0
        #print max_depth

    if max_depth == 1:
        options = [["x"],["y"]] #sets the last nested list with x or y
        choose = random.choice(options) #picks from options
        return choose
        #print choose
        
    else:
        options = ['prod','cosine','sine','sin_pi','cube'] #when depth is set to more than 0, can pick one of the options
        choose = random.choice(options) #chooses from options
        if choose == 'prod': # product is the only one with 2 arguments
            choose = ['prod',build_random_function(min_depth,max_depth-1),build_random_function(min_depth,max_depth-1)]
            #print choose
            return choose
        else: #the rest of the options have only one argument
            choose = [choose, build_random_function(min_depth,max_depth-1)]
            return choose
    
   
    return choose
        
#build_random_function(min_depth, max_depth)
#f = build_random_function(min_depth, max_depth)
#print f
#f = ['sin_pi', [['sin_pi', [['sin_pi', ['y']]]]]]
x = randint(-1,1)
y = randint(-1,1)
def evaluate_random_function(f, x, y):
    """ This function takes in the randomly generated function and makes into something mathematical,
    giving it an actual value that makes sense.
    """  
    #print 'f'
    #print f
    # the following if and elif statements explain what the mathematical equivalent of the pseudo code are
    if f[0] == 'x':
        return x
    elif f[0] == 'y':
        return y
    elif f[0] == "prod":
        return evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y)
    elif f[0] == "sine":
        return math.sin(evaluate_random_function(f[1], x, y))
    elif f[0] == "cosine":
        return math.cos(evaluate_random_function(f[1], x, y))
    elif f[0] == "sin_pi":
        return math.sin(math.pi*evaluate_random_function(f[1], x, y))
    elif f[0] == "cube":
        return evaluate_random_function(f[1], x, y)**3.0
    else: #if there is a problem, I will know
      print 'problem'  

    # your code goes here0
#print evaluate_random_function(f,x,y)
#evaluate_random_function(f,x,y)

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """
    # your code goes here
    val = (val-float(input_interval_start))*(1.0/(input_interval_end-float(input_interval_start)))*(float(output_interval_end)-float(output_interval_start))-float(output_interval_start)
    return val #can map an interval of numbers to any other interval of numbers


p1 = 500 #x pixel value for image
p2 = 500 #y pixel value for image
def mapping():
   """ What the mapping function does is generate random functions for RGB channels and 
   evaluates those functions for the pixel dimensions of the image. It also takes those mapped
   values and maps them again to an actual RGB value.
   """
   
    image = Image.new('RGB',(p1,p2)) #creates an empty RGB image

    R = build_random_function(min_depth,max_depth) #creates random function for red
    G = build_random_function(min_depth,max_depth) #creates random function for green
    B = build_random_function(min_depth,max_depth) #creates random function for blue
    #print R
    
    for x in range(p1): #runs values through all x pixel dimensions
        for y in range(p2): # runs values through all y pixel dimensions
                     
            #print evaluate_random_function(R,x,y)
            # evaluates and maps all RGB values to a range of [-1 1]
            R1 = evaluate_random_function(R,remap_interval(x,0,p1-1,-1,1),remap_interval(y,0,p2-1,-1,1)) 
            G1 = evaluate_random_function(G,remap_interval(x,0,p1-1,-1,1),remap_interval(y,0,p2-1,-1,1))
            B1 = evaluate_random_function(B,remap_interval(x,0,p1-1,-1,1),remap_interval(y,0,p2-1,-1,1))
            #print (R1,G1,B1)
            # maps the values returned from above to the actual RGB value between 0 and 256
            R2 = remap_interval(R1,-1,1,0,255)
            G2 = remap_interval(G1,-1,1,0,255)
            B2 = remap_interval(B1,-1,1,0,255)
            #print(R2,G2,B2)
            # puts RGB values into an image
            image.putpixel((x,y),(int(R2),int(G2),int(B2)))
    image.save('again3' + '.jpg') #saves my image :) - life is great!
            
mapping()

