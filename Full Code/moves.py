import cube

def R():
    cube.red = cube.red[::-1]          # Reverses list
    cube.red = cube.red.transpose()     # Makes all column elements rows and vice versa
    ## The next code makes the ones that are going to move equal to turn_
    turng = [cube.green[0][2],cube.green[1][2],cube.green[2][2]]   
    turnw = [cube.white[0][2],cube.white[1][2],cube.white[2][2]]
    turnb = [cube.blue[2][0],cube.blue[1][0],cube.blue[0][0]]
    turny = [cube.yellow[0][2],cube.yellow[1][2],cube.yellow[2][2]]

    # This shows the movement of the faces moving round 1 square in the direction of movement
    turnw,turnb,turny,turng = turng,turnw,turnb,turny   

    cube.green[0][2],cube.green[1][2],cube.green[2][2] = turng[0],turng[1],turng[2]
    cube.white[0][2],cube.white[1][2],cube.white[2][2] = turnw[0],turnw[1],turnw[2]
    cube.blue[2][0],cube.blue[1][0],cube.blue[0][0] = turnb[0],turnb[1],turnb[2]
    cube.yellow[0][2],cube.yellow[1][2],cube.yellow[2][2] = turny[0],turny[1],turny[2]

def L():
    cube.orange = cube.orange[::-1]
    cube.orange = cube.orange.transpose()

    turng = [cube.green[0][0],cube.green[1][0],cube.green[2][0]]
    turnw = [cube.white[0][0],cube.white[1][0],cube.white[2][0]]
    turnb = [cube.blue[2][2],cube.blue[1][2],cube.blue[0][2]]
    turny = [cube.yellow[0][0],cube.yellow[1][0],cube.yellow[2][0]]

    turnw,turnb,turny,turng = turnb,turny,turng,turnw

    cube.green[0][0],cube.green[1][0],cube.green[2][0] = turng[0],turng[1],turng[2]
    cube.white[0][0],cube.white[1][0],cube.white[2][0] = turnw[0],turnw[1],turnw[2]
    cube.blue[2][2],cube.blue[1][2],cube.blue[0][2] = turnb[0],turnb[1],turnb[2]
    cube.yellow[0][0],cube.yellow[1][0],cube.yellow[2][0] = turny[0],turny[1],turny[2]

def U():
    cube.white = cube.white[::-1]
    cube.white = cube.white.transpose()

    turng = [cube.green[0][0],cube.green[0][1],cube.green[0][2]]
    turno = [cube.orange[0][0],cube.orange[0][1],cube.orange[0][2]]
    turnb = [cube.blue[0][0],cube.blue[0][1],cube.blue[0][2]]
    turnr = [cube.red[0][0],cube.red[0][1],cube.red[0][2]]

    turng,turno,turnb,turnr = turnr,turng,turno,turnb

    cube.green[0][0],cube.green[0][1],cube.green[0][2] = turng[0],turng[1],turng[2]
    cube.orange[0][0],cube.orange[0][1],cube.orange[0][2] = turno[0],turno[1],turno[2]
    cube.blue[0][0],cube.blue[0][1],cube.blue[0][2] = turnb[0],turnb[1],turnb[2]
    cube.red[0][0],cube.red[0][1],cube.red[0][2] = turnr[0],turnr[1],turnr[2]

def D():
    cube.yellow = cube.yellow[::-1]
    cube.yellow = cube.yellow.transpose()

    turng = [cube.green[2][0],cube.green[2][1],cube.green[2][2]]
    turno = [cube.orange[2][0],cube.orange[2][1],cube.orange[2][2]]
    turnb = [cube.blue[2][0],cube.blue[2][1],cube.blue[2][2]]
    turnr = [cube.red[2][0],cube.red[2][1],cube.red[2][2]]

    turng,turno,turnb,turnr = turno,turnb,turnr,turng

    cube.green[2][0],cube.green[2][1],cube.green[2][2] = turng[0],turng[1],turng[2]
    cube.orange[2][0],cube.orange[2][1],cube.orange[2][2] = turno[0],turno[1],turno[2]
    cube.blue[2][0],cube.blue[2][1],cube.blue[2][2] = turnb[0],turnb[1],turnb[2]
    cube.red[2][0],cube.red[2][1],cube.red[2][2] = turnr[0],turnr[1],turnr[2]

def F():
    cube.green = cube.green[::-1]
    cube.green = cube.green.transpose()

    turnw = [cube.white[2][0],cube.white[2][1],cube.white[2][2]]
    turno = [cube.orange[2][2],cube.orange[1][2],cube.orange[0][2]]
    turny = [cube.yellow[0][0],cube.yellow[0][1],cube.yellow[0][2]]
    turnr = [cube.red[0][0],cube.red[1][0],cube.red[2][0]]

    turnw,turno,turny,turnr = turno,turny,turnr,turnw

    cube.white[2][0],cube.white[2][1],cube.white[2][2] = turnw[0],turnw[1],turnw[2]
    cube.orange[0][2],cube.orange[1][2],cube.orange[2][2] = turno[0],turno[1],turno[2]
    cube.yellow[0][2],cube.yellow[0][1],cube.yellow[0][0] = turny[0],turny[1],turny[2]
    cube.red[0][0],cube.red[1][0],cube.red[2][0] = turnr[0],turnr[1],turnr[2]

def B():
    cube.blue = cube.blue[::-1]
    cube.blue = cube.blue.transpose()

    turnw = [cube.white[0][0],cube.white[0][1],cube.white[0][2]]
    turno = [cube.orange[0][0],cube.orange[1][0],cube.orange[2][0]]
    turny = [cube.yellow[2][2],cube.yellow[2][1],cube.yellow[2][0]]
    turnr = [cube.red[0][2],cube.red[1][2],cube.red[2][2]]

    turnw,turno,turny,turnr = turnr,turnw,turno,turny

    cube.white[0][0],cube.white[0][1],cube.white[0][2] = turnw[0],turnw[1],turnw[2]
    cube.orange[2][0],cube.orange[1][0],cube.orange[0][0] = turno[0],turno[1],turno[2]
    cube.yellow[2][0],cube.yellow[2][1],cube.yellow[2][2] = turny[0],turny[1],turny[2]
    cube.red[0][2],cube.red[1][2],cube.red[2][2] = turnr[0],turnr[1],turnr[2]

# Uses previous funcitons to use different movements
# lower case moves it in the opposite direction
# _2 moves it in twice in a direction

def r():    
    for i in range(3):
        R()

def l():
    for i in range(3):
        L()

def u():
    for i in range(3):
        U()

def d():
    for i in range(3):
        D()
    
def f():
    for i in range(3):  
        F()

def b():
    for i in range(3):
        B()

def R2():
    for i in range(2):
        R()

def L2():
    for i in range(2):
        L()

def U2():
    for i in range(2):
        U()

def D2():
    for i in range(2):
        D()
    
def F2():
    for i in range(2):
        F()

def B2():
    for i in range(2):
        B()

