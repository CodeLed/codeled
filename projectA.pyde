import random
from dictionary import quiz

data = quiz.data
choose = ''#groen
ran = -1
chosenAns = ''
chosenPlayers = 0
listPlayers = []
cPlayer = 0

x = 300
y = 300
def setup():
    global x, y
    frameRate(20)
    size(x,y)
def card():
    global data
    global choose
    global ran
    fill(255,255,255)
    rect(0,0,300, 250)
    fill(255,0,0)
    rect(0,0, 300,75)
    fill(0)
    text(data[choose][ran]['vraag'], 30, 40)
    text(data[choose][ran]['antwoorden']['A'], 30, 100)
    text(data[choose][ran]['antwoorden']['B'], 30, 140)
    text(data[choose][ran]['antwoorden']['C'], 30, 180)
    text(data[choose][ran]['antwoorden']['D'], 30, 220)

def players():
    fill(192,192,192)
    rect(50, 50, 80, 40)
    fill(255,255,255)
    text("One player", 60, 75)
    
    fill(192,192,192)
    rect(170, 50, 80, 40)
    fill(255,255,255)
    text("Two players", 180, 75)
    
    fill(192,192,192)
    rect(50, 150, 80, 40)
    fill(255,255,255)
    text("Three players", 55, 175)
    
    fill(192,192,192)
    rect(170, 150, 80, 40)
    fill(255,255,255)
    text("Four players", 180, 175)

def colorChoose():
    global x, y
    fill(255,0,0)
    rect(0,0, x / 2, y / 2)
    
    fill(0,128,0)
    rect(x / 2,0, x / 2, y / 2)
    
    fill(255,255,0)
    rect(0,y / 2, x / 2, y / 2)
    
    fill(255,128,0)
    rect(x / 2,y / 2, x / 2, y / 2)
  
def reset():
    global choose, chosenAns, ran, chosenPlayers, listPlayers
    choose = chosenAns = ''
    ran = -1
  
def result(res, points):
    fill(255)
    rect(50, 50,200,200)
    fill(0)
    text("je antwoord is " + res, 80, 150)
    if points == 0:
        text("je hebt geen punten verdient", 80, 170)
    else:
        text("je hebt " + str(points) + " punten gekregen", 80, 170)

    
def mousePressed():
    global chosenAns, data, choose, chosenPlayers, listPlayers, cPlayer
    global ran
        #A, B, C, D
    if chosenPlayers == 0:
        if 50 < mouseX < 50 + 80 and 50 < mouseY < 50 + 40:
            chosenPlayers = 1
            listPlayers = [0]
            
        elif 170 < mouseX < 170 + 80 and 50 < mouseY < 50 + 40:
            chosenPlayers = 2
            listPlayers = [0, 0]
            
        elif 50 < mouseX < 50 + 80 and 150 < mouseY < 150 + 40:
            chosenPlayers = 3
            listPlayers = [0, 0, 0]
            
        elif 170 < mouseX < 170 + 80 and 150 < mouseY < 150 + 40:
            chosenPlayers = 4
            listPlayers = [0, 0, 0, 0]
            
        else:
            print("Click on the right button!")    
    else:
        if choose != '' and chosenAns != '':
            reset()  
            cPlayer +=1 
            if cPlayer >= len(listPlayers):
                cPlayer = 0
        elif choose != '':
            if 30 < mouseX < 300 and 85 <mouseY < 105:
                chosenAns = 'A'
            elif 30 < mouseX < 300 and 125 <mouseY < 145:
                chosenAns = 'B'
            elif 30 < mouseX < 300 and 165 <mouseY < 185:
                chosenAns = 'C'
            elif 30 < mouseX < 300 and 205 <mouseY < 225:
                chosenAns = 'D'
            
        else:
            global x, y, choose
            if 0 < mouseX < x / 2 and 0 <mouseY < y / 2:
                choose = 'rood'
            elif x / 2 < mouseX < x and 0 <mouseY < y / 2:
                choose = 'groen'
            elif 0 < mouseX < x / 2 and y / 2 <mouseY < y:
                choose = 'geel'
            elif x / 2 < mouseX < x and y / 2 <mouseY < y:
                choose = 'oranje'
        
def draw():
    global data, choose, ran, chosenAns, chosenPlayers, listPlayers, cPlayer
    clear()
    print(choose) 
    if chosenPlayers == 0:
        players()
    else: 
        if choose != '':
            if chosenAns != '':
                if data[choose][ran]['goed'] == chosenAns:
                    print("goed")
                    result("goed", data[choose]["punten"])
                    listPlayers[cPlayer] = data[choose]["punten"]
                else:
                    result('fout', 0)
                
                print(cPlayer)
                print(listPlayers)
            else:
                if ran == -1:
                    print(len(data[choose]) -2)
                    ran = random.randint(0, len(data[choose]) -2)
                card()
        else:
            colorChoose()
