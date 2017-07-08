# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import simplegui

global str1
str1 = []
global str2
str2 = ''

def binary_value(x):
    a = []
    b = []
    while( x/2 != 1):
        a.append(x%2)
        x /= 2
    if(x%2==0):    
        a.append(0)
    else:
        a.append(1)
    a.append(1)
    a.reverse()    
    #str1 = ''
    if(len(a) < 7):
        y = len(a)
        z = 7 - y
        for i in range(0, z):
            b.append(0)
        for j in range(0, y):
            b.append(a[j])
              
    else:
        b = a
        
    return b

def hamm(t):
    x = 0
    y = []
    
    c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    three = [0, 0, 0, 0]
    five = [0, 0, 0, 0]
    six = [0, 0, 0, 0]
    seven = [0, 0, 0, 0]
    nine = [0, 0, 0, 0]
    ten = [0, 0, 0, 0]
    eleven = [0, 0, 0, 0]
    
    x = ord(t)
    y = binary_value(x)    
    
    c[2] = y[0]
    c[4] = y[1]
    c[5] = y[2]
    c[6] = y[3]
    c[8] = y[4]
    c[9] = y[5]
    c[10] = y[6]
    
    if(c[2]==1):
        three[0] = three[1] =1
    if(c[4]==1):
        five[0] = five[2] = 1
    if(c[5]==1):
        six[1] = six[2] = 1
    if(c[6]==1):
        seven[0] = seven[1] = seven[2] = 1
    if(c[8]==1):
        nine[0] = nine[3] = 1
    if(c[9]==1):
        ten[1] = ten[3] = 1
    if(c[10]==1):
        eleven[0] = eleven[1] = eleven[3] = 1
        
    ze = three[0]+five[0]+six[0]+seven[0]+nine[0]+ten[0]+eleven[0]
    on = three[1]+five[1]+six[1]+seven[1]+nine[1]+ten[1]+eleven[1]
    tw = three[2]+five[2]+six[2]+seven[2]+nine[2]+ten[2]+eleven[2]
    th = three[3]+five[3]+six[3]+seven[3]+nine[3]+ten[3]+eleven[3]
    
    if(ze%2 == 1):
        c[0] = ze%2
    if(on%2 == 1):
        c[1] = on%2
    if(tw%2 == 1):
        c[3] = tw%2
    if(th%2 == 1):
        c[7] = th%2
        
    return c

def convert_to_string(s):
    str1 = ''
    for k in range(0, len(s)):
        str1 = str1 + str(s[k])
        
    return str1

def input(i):
    m = convert_to_string(binary_value(ord(i)))
    str3 = " Code for " + str(i) + " before hamming: " + m + " and THE HAMMING CODE FOR " + str(i) + " is: " + convert_to_string(hamm(i)) 
    return str3


    
def word_input(w):
    global str1
    global str2
    for i in range(len(w)):
        str1.extend([input(w[i])])
        str2 = "\n".join(str1)
    print (str2)
    if (len(w)>1):
        str2 = " Check in Output window"       
    
    
      
def draw(canvas):
    canvas.draw_text(str2, (50, 40), 15, 'Green')
    
f = simplegui.create_frame("HAMMING",1000,125)
f.set_draw_handler(draw)
f.add_input("Enter the letter ", word_input, 50)

f.start()
