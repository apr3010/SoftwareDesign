# -*- coding: utf-8 -*-
"""
Random_art.py

@author: amonmillner, adapted from pruvolo work
"""

# you do not have to use these particular modules, but they may help
import random
import math
import Image

min_depth = 2
max_depth = 3
list_gen = []

# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 19:43:22 2014

@author: abigail
"""
from random import randint
from PIL import Image

min_depth = 4
max_depth = 25

def build_random_function(min_depth, max_depth):
    if min_depth > 0:
        max_depth = randint(min_depth,max_depth)
        min_depth = 0
        #print max_depth

    if max_depth == 1:
        options = [["x"],["y"]]
        choose = random.choice(options)
        return choose
        #print choose
        
    else:
        options = ['prod','cosine','sine','sin_pi','cube']
        choose = random.choice(options)
        if choose == 'prod':
            choose = ['prod',build_random_function(min_depth,max_depth-1),build_random_function(min_depth,max_depth-1)]
            #print choose
            return choose
        else:
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
    """ your doc string goes here
    """  
    #print 'f'
    #print f
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
        return evaluate_random_function(f[1], x, y)**3
    else:
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
    return val



def mapping():
    image = Image.new('RGB',(350,350))

    R = build_random_function(15,max_depth)
    G = build_random_function(min_depth,10)
    B = build_random_function(min_depth,30)
    #print R
    
    for x in range(350):
        for y in range(350):
                     
            #print evaluate_random_function(R,x,y)
            R1 = evaluate_random_function(R,remap_interval(x,0,349,-1,1),remap_interval(y,0,349,-1,1))
            G1 = evaluate_random_function(G,remap_interval(x,0,349,-1,1),remap_interval(y,0,349,-1,1))
            B1 = evaluate_random_function(B,remap_interval(x,0,349,-1,1),remap_interval(y,0,349,-1,1))
            #print (R1,G1,B1)
            R2 = remap_interval(R1,-1,1,0,255)
            G2 = remap_interval(G1,-1,1,0,255)
            B2 = remap_interval(B1,-1,1,0,255)
            #print(R2,G2,B2)
            
            image.putpixel((x,y),(int(R2),int(G2),int(B2)))
    image.save('again1' + '.jpg')
            
mapping()

