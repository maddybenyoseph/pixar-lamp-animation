import processing.opengl 

global check1
check1 = 0.01
global rotation
rotation = 0
global gravity
gravity = 0.98
global speed
speed = 0
global bounce
bounce = -1
global startX
startX = 2000
global startY
startY = 1000
global time
time = 0

global eyeX
global eyeY
global eyeZ
eyeX = 0
eyeY = 0
eyeZ = 0
d = 100

add_library("sound")
 
# Function to determine the rotation speed of the Pixar lamp
def rotationSpeed():
    global check1
    rotationSpeed = ((PI / 2 * (check1 * 0.1)) / 5.0)
    check1 += 0.1
    return rotationSpeed


# The rotating lamp portion of the Pixar lamp
def lampLight():
    # rotation things
    speed = rotationSpeed()

    # ball
    pushMatrix()
    noStroke()
    lights()
    rotateZ(-0.7)
    scale(1.25, 0.6, 1.0)
    translate(150, 150, 0)
    rotateZ(speed)
    sphere(70)
    popMatrix()

    # ball
    pushMatrix()
    noStroke()
    lights()
    rotateZ(-0.7)
    scale(1.30, 0.65, 1.0)
    translate(145, 160, 0)
    rotateZ(speed)
    sphere(70)
    popMatrix()

     # ball
    pushMatrix()
    noStroke()
    lights()
    rotateZ(-0.7)
    scale(1.35, 0.7, 1.0)
    translate(140, 170, 0)
    rotateZ(speed)
    sphere(70)
    popMatrix()

     # ball
    pushMatrix()
    noStroke()
    lights()
    rotateZ(-0.7)
    scale(1.45, 0.75, 1.0)
    translate(130, 180, 0)
    rotateZ(speed)
    sphere(70)
    popMatrix()

    # BIG ball
    pushMatrix()
    noStroke()
    lights()
    rotateZ(-0.7)
    scale(1.0, 1.0, 1.0)
    translate(195, 250, 0)
    rotateZ(speed)
    sphere(150)
    popMatrix()

    # cover ball
    pushMatrix()
    noStroke()
    noLights()
    rotateZ(-0.7)
    fill(255, 255, 255)
    scale(1.0, 0.75, 1.0)
    translate(195, 380, 0)
    rotateZ(speed)
    sphere(160)
    popMatrix()

    pushMatrix()
    fill(183, 178, 178)
    noStroke()
    translate(-100, 100, -40)
    # rotateX(-4.0)
    scale(2.5, 0.3, 0.3)
    box(150)
    popMatrix()

# The rotating stand portion of the Pixar lamp
def stand():
    speed = rotationSpeed()
    speed = 1

    # big bottom stand
    pushMatrix()
    fill(183, 178, 178)
    lights()
    noStroke()
    scale(1.0, 0.15, 1.0)
    translate(width / 2, height / 2 + 3000, 0)
    rotateY(speed)
    sphere(150)
    popMatrix()

    # mini stand
    pushMatrix()
    fill(183, 178, 178)
    lights()
    scale(0.75, 0.3, 1.0)
    noStroke()
    translate(width / 2 + 100, height / 2 + 1300, 0)
    rotateY(speed)
    sphere(50)
    popMatrix()

    # large rectangle
    pushMatrix()
    fill(183, 178, 178)
    lights()
    scale(0.3, 8.0, 0.3)
    noStroke()
    translate(width / 2 + 1100, 35, 0)
    rotateY(speed)
    box(50)
    popMatrix()

# The Luxo Ball of the Pixar Lamp
def luxoBall():
    speed = rotationSpeed() 
    
    #blue ball
    pushMatrix()
    stroke(0)
    lights()
    fill(0, 0, 255)
    rotateZ(speed)
    translate(600, 400, -200)
    sphere(150)
    popMatrix()
    
    #red ball
    pushMatrix()
    stroke(0)
    lights()
    fill(255, 0, 0)
    rotateZ(speed/5.0)
    translate(300, 380, -200)
    translate(0, 0, -300)
    sphere(150)
    popMatrix()
    
    #yellow ball
    pushMatrix()
    stroke(0)
    lights()
    fill(255, 255, 0)
    #translate(100, 400, -200)
    rotateX(speed)
    translate(0, 0, -300)
    sphere(150)
    popMatrix()
    
#The Luxo Ball of the Pixar Lamp
def luxoBallEnding():
    pushMatrix()
    noStroke()
    fill(0, 0, 255)
    translate(550, 430, -150)
    sphere(80)
    popMatrix()
    
    pushMatrix()
    noStroke()
    fill(255, 255, 0)
    translate(530, 425, -100)
    sphere(60)
    popMatrix()
    
    
def star(x, y, r1, r2, n):
    fill(255, 0, 0)
    angle = TWO_PI / n
    halfAngle = angle / 2.0
    beginShape()
    a = 0
    while (a < TWO_PI):
        sx = x + cos(a) * r2
        sy = y + sin(a) * r2
        vertex(sx, sy)
        sx = x + cos(a + halfAngle) * r1
        sy = y + sin(a + halfAngle) * r1
        vertex(sx, sy)
        a += angle
    endShape(CLOSE)


# A method for further mechanisms of the Pixar Lamp
def firstContraption():
    pushMatrix()
    translate(width / 2, height / 2 - 200, 100)
    rotateX(-0.8)
    scale(0.5, 0.5, 0.5)
    background(151, 190, 252)
    popMatrix()

def firstContraptionBlack():
    pushMatrix()
    translate(width / 2, height / 2 - 200, 100)
    rotateX(-0.8)
    scale(0.5, 0.5, 0.5)
    background(0)
    popMatrix()

def pixarLamp():
    speed = rotationSpeed()
    speed = -10

    #camera(mouseX, height/4, (height/4) / tan(PI/6), width/4, height/4, 0, 0, 1, 0);
    pushMatrix()
    #translate(-175, 150, 300)
    rotateZ(-0.08)
    translate(0, 0, 0)
    rotateY(speed)
    firstContraption()
    popMatrix()

    stand()

    pushMatrix()
    scale(0.75, 0.75, 0.75)
    translate(400, 10, -300)
    rotateY(speed)
    translate(-200, 10, -100)
    lampLight()
    popMatrix()
    
    
def blackPixarLamp():
    speed = rotationSpeed()
    speed = -10

    #camera(mouseX, height/4, (height/4) / tan(PI/6), width/4, height/4, 0, 0, 1, 0);
    pushMatrix()
    #translate(-175, 150, 300)
    rotateZ(-0.08)
    translate(0, 0, 0)
    rotateY(speed)
    firstContraptionBlack()
    popMatrix()

    stand()

    pushMatrix()
    scale(0.75, 0.75, 0.75)
    translate(400, 10, -300)
    rotateY(speed)
    translate(-200, 10, -100)
    lampLight()
    popMatrix()
    
    

def P():
    pushMatrix()
    fill(30)
    noStroke()
    translate(60, 350, -100)
    scale(0.2, 1.8, 0.2)
    box(70)
    popMatrix()

    pushMatrix()
    fill(30)
    noStroke()
    translate(90, 310, -100)
    rotateZ(-45)
    scale(0.2, 1.2, 0.2)
    box(70)
    popMatrix()

    pushMatrix()
    fill(30)
    noStroke()
    translate(90, 350, -100)
    rotateZ(45)
    scale(0.2, 0.9, 0.2)
    box(70)
    popMatrix()

def I():
    pushMatrix()
    fill(30)
    noStroke()
    translate(230, 350, -100)
    scale(0.2, 1.8, 0.2)
    box(70)
    popMatrix()

def X():
    pushMatrix()
    fill(30)
    noStroke()
    translate(420, 350, -100)
    rotateZ(-70)
    scale(0.2, 1.8, 0.2)
    box(100)
    popMatrix()

    pushMatrix()
    fill(30)
    noStroke()
    translate(420, 350, -100)
    rotateZ(70)
    scale(0.2, 1.8, 0.2)
    box(100)
    popMatrix()

def A():
    pushMatrix()
    fill(30)
    noStroke()
    translate(640, 350, -100)
    rotateZ(-60)
    scale(0.2, 1.8, 0.2)
    box(70)
    popMatrix()

    pushMatrix()
    fill(30)
    noStroke()
    translate(605, 350, -100)
    rotateZ(60)
    scale(0.2, 1.8, 0.2)
    box(70)
    popMatrix()

    pushMatrix()
    fill(30)
    noStroke()
    translate(628, 360, -100)
    scale(0.6, 0.2, 0.2)
    box(70)
    popMatrix()

def R():
    pushMatrix()
    fill(30)
    noStroke()
    translate(760, 350, -100)
    scale(0.2, 1.8, 0.2)
    box(70)
    popMatrix()

    pushMatrix()
    fill(30)
    noStroke()
    translate(790, 310, -100)
    rotateZ(-45)
    scale(0.2, 1.2, 0.2)
    box(70)
    popMatrix()

    pushMatrix()
    fill(30)
    noStroke()
    translate(790, 350, -100)
    rotateZ(45)
    scale(0.2, 0.9, 0.2)
    box(70)
    popMatrix()

    pushMatrix()
    fill(30)
    noStroke()
    translate(790, 380, -100)
    rotateZ(-45)
    scale(0.2, 1.2, 0.2)
    box(70)
    popMatrix()

    
    #camera(20.0, 10.0, d, 300.0, 300.0, 0.0, 0.0, 1.0, 0.0)

#The star part of the Luxo ball
def starEnding():
    translate(620, 510)
    fill(255, 0, 0)
    beginShape()
    vertex(0, -50)
    vertex(14, -20)
    vertex(47, -15)
    vertex(23, 7)
    vertex(29, 40)
    vertex(0, 25)
    vertex(-29, 40)
    vertex(-23, 7)
    vertex(-47, -15)
    vertex(-14, -20)
    endShape(CLOSE)
    
def setup():
    size(1200, 600, OPENGL)
    background(151, 190, 252)
    global sf
    sf = SoundFile(this,"PixarTitle.wav")
    sf.play()
    overallTime = millis()


def draw():
    overallTime = millis()
    global time
    beginCamera()
    time2 = 0
    if (time == 211):
        translate(0, 0, -1)
        if (time2 == 100):
            translate(0, 0, 0)
    else:
        translate(1, 0, 0.1)
    endCamera()
    
    
    pushMatrix()
    scale(0.3, 0.3, 0.3)
    global startX
    global startY
    global time
    translate(startX, startY, 0)
    if (startX >= -100):
        startX -= 10
        if (startY > 900):
            startY -= 5
        elif (startY == 900):
            while (startY < 1000):
                startY += 10
        time += 1
    else:
        startX = -101.0
        

    bool1 = 1300
    if (startX == -101.0):
        speed = rotationSpeed()
        speed2 = (-speed / 3.0)
        rotateY(-0.8)
        if (speed2 <= -1.1):
            translate(bool1, -500, -700)
            rotateY(-3.0)
            bool1 += 1
            
    if (bool1 == 1301):
        x = 350
        translate(0, x, 0)
    
            
    pixarLamp()
    popMatrix()
    
    #luxo balls
    pushMatrix()
    if (bool1 == 1301):
        luxoBall()
    popMatrix()
    

    P()
    I()
    X()
    A()
    R()
    
    if (overallTime >= 10000):
        background(0)
        rotateY(3.0)
        blackPixarLamp()
        rotateY(-3.0)
        
        fill(255, 255, 255)
        ellipse(400, 800, 2000, 300)
        
        fill(0)
        textSize(100)
        text("Animation By:", -50, 780)
        text("Madeline Ben-Yoseph", -50, 880)
        
        pushMatrix()
        luxoBallEnding()
        popMatrix()
        
        pushMatrix()
        scale(0.8)
        translate(20, 20)
        starEnding()
        popMatrix()
        
        
    
    
