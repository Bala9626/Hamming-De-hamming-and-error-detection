import simplegui

global s2
s2 = ''
global s3
s3 = ''

def code_input(c):
    global s3
    s1 = str(c)
    counter = 0
    
    one = [0, 0, 0, 0]
    two = [0, 0, 0, 0]
    three = [0, 0, 0, 0]
    four = [0, 0, 0, 0]
    five = [0, 0, 0, 0]
    six = [0, 0, 0, 0]
    seven = [0, 0, 0, 0]
    eight = [0, 0, 0, 0]
    nine = [0, 0, 0, 0]
    ten = [0, 0, 0, 0]
    eleven = [0, 0, 0, 0]
    
    if(int(s1[0])==1):
        one[0] = 1 
    if(int(s1[1])==1):
        two[1] = 1 
    if(int(s1[2])==1):
        three[0] = three[1] = 1
    if(int(s1[3])==1):
        four[2] = 1
    if(int(s1[4])==1):
        five[0] = five[2] = 1
    if(int(s1[5])==1):
        six[1] = six[2] = 1
    if(int(s1[6])==1):
        seven[0] = seven[1] = seven[2] = 1
    if(int(s1[7])==1):
        eight[3] = 1
    if(int(s1[8])==1):
        nine[0] = nine[3] = 1
    if(int(s1[9])==1):
        ten[1] = ten[3] = 1
    if(int(s1[10])==1):
        eleven[0] = eleven[1] = eleven[3] = 1 
        
    a1 = one[0] + two[0] + three[0] + four[0] + five[0] + six[0] + seven[0] + eight[0] + nine[0] + ten[0] + eleven[0]
    a2 = one[1] + two[1] + three[1] + four[1] + five[1] + six[1] + seven[1] + eight[1] + nine[1] + ten[1] + eleven[1]
    a4 = one[2] + two[2] + three[2] + four[2] + five[2] + six[2] + seven[2] + eight[2] + nine[2] + ten[2] + eleven[2]
    a8 = one[3] + two[3] + three[3] + four[3] + five[3] + six[3] + seven[3] + eight[3] + nine[3] + ten[3] + eleven[3]
    
    if(a1%2==1):
        counter += 1
    if(a2%2==1):
        counter += 2
    if(a4%2==1):
        counter += 4
    if(a8%2==1):
        counter += 8
        
    if(int(s1[counter-1])==1):
        s2 = s1[0: counter-1] + '0' + s1[counter:]
    elif(int(s1[counter-1])==1):
        s2 = s1[0: counter-1] + '1' + s1[counter:]
    elif(counter==0):
        s2 = s1
    
    if(s1==s2):
        s3 = "Given code is correct code without errors"
    elif(s1!=s2):
        s3 = "Correct code is: "+s2
        
def draw(canvas):
    canvas.draw_text(s3, (50, 40), 15, 'Green')
    
f = simplegui.create_frame("ERROR CORRECTION",500,125)
f.set_draw_handler(draw)
f.add_input("Enter the 11 digit binary code ", code_input, 100)

f.start()    
