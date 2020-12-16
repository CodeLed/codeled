import random
from dictionary import quiz

data = quiz.data
choose = ''
ran = -1
chosenAns = ''
listPlayers = []
cPlayer = 0
dice = 0
state = 'start'
# start
# throw
# card
# cardResult
# end
x = 300
y = 300
def setup():
    global x, y
    frameRate(20)
    size(x, 500)

def card():
    global data, choose, ran
    fill(255,255,255)
    rect(0,0,300, 250)
    if choose == 'rood':
        fill(255,0,0)
        rect(0,0, 300,75)
    elif choose == 'geel':
        fill(255,255,0)
        rect(0,0, 300,75)
    elif choose == 'oranje':
        fill(255,128,0)
        rect(0,0, 300,75)
    elif choose == 'groen':
        fill(0,128,0)
        rect(0,0, 300,75)
    else:
        fill(255,0,0)
        rect(0,0, 300,75)
    fill(0)
    text(data[choose][ran]['vraag'], 30, 40)
    text(data[choose][ran]['antwoorden']['A'], 30, 100)
    text(data[choose][ran]['antwoorden']['B'], 30, 140)
    text(data[choose][ran]['antwoorden']['C'], 30, 180)
    text(data[choose][ran]['antwoorden']['D'], 30, 220)

def diceButton():
    fill(192,192,192)
    rect(110, 450, 80, 40)
    fill(255,255,255)
    text("Throw Dice", 120, 475)

def throwDice():
    dice = random.randint(1,6)
    return dice

def displayDice(throwDice):
    global dice
    if dice != 0:
        return text("Dice thrown and got " + str(throwDice), 100, 350)

def showCurrentPlayerTurn(current_player):
    return text("This is the turn of player " + str(current_player + 1), 100, 380)

def showWinner(current_player):
    return text("GAME ENDED. Player " + str(current_player + 1) + " WON!", 100, 380)

def scoreboard(listPlayers):
    player_number = 1
    vertical_height = 400
    for points in listPlayers:
        text("Player " + str(player_number) + ": " + str(points) + " points", 100, vertical_height)
        player_number += 1
        vertical_height += 15

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
    global chosenAns, data, choose, state, listPlayers, cPlayer, dice
    global ran
        #A, B, C, D
    if state == 'start':
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
        
         # Pure for testing!!!!!
        elif 110 < mouseX < 110+ 80 and 450 < mouseY < 450 + 40:
            dice = throwDice()
            
        if len(listPlayers) > 0:
            state = 'throw'
               
    elif state == 'cardResult':
        reset()  
        cPlayer +=1 
        if cPlayer >= len(listPlayers):
            cPlayer = 0
        state = 'throw'
            
    elif state == 'card':
        if 30 < mouseX < 300 and 85 <mouseY < 105:
            chosenAns = 'A'
        elif 30 < mouseX < 300 and 125 <mouseY < 145:
            chosenAns = 'B'
        elif 30 < mouseX < 300 and 165 <mouseY < 185:
            chosenAns = 'C'
        elif 30 < mouseX < 300 and 205 <mouseY < 225:
            chosenAns = 'D'
        if data[choose][ran]['goed'] == chosenAns:
            listPlayers[cPlayer] += data[choose]["punten"]
            
        if listPlayers[cPlayer] > 3:
            state = 'end'
        else:
            state = 'cardResult'
            
    elif state == 'throw':
        global x, y, choose
        dice = 0
        if 0 < mouseX < x / 2 and 0 <mouseY < y / 2:
            choose = 'rood'
        elif x / 2 < mouseX < x and 0 <mouseY < y / 2:
            choose = 'groen'
        elif 0 < mouseX < x / 2 and y / 2 <mouseY < y:
            choose = 'geel'
        elif x / 2 < mouseX < x and y / 2 <mouseY < y:
            choose = 'oranje'
        state = 'card'
        
    elif state == 'end':
        if 0 < mouseX < 300 and 0 < mouseY < 500:
            exit()
        
        
def draw():
    global data, choose, ran, chosenAns, chosenPlayers, listPlayers, cPlayer, dice
    clear()
    print(choose) 
    scoreboard(listPlayers)
    
    if state == 'start':
        players()
        # Placeholder area, for testing
        diceButton()
        displayDice(dice)
    elif state == 'cardResult':
        if data[choose][ran]['goed'] == chosenAns:
            print("goed")
            return result("goed", data[choose]["punten"])
            
        else:
            return result('fout', 0)
        
        print(cPlayer)
        print(listPlayers)
    elif state == 'card':
        if ran == -1:
            print(len(data[choose]) -2)
            ran = random.randint(0, len(data[choose]) -2)
        card()
    elif state == 'throw':
        colorChoose()
        showCurrentPlayerTurn(cPlayer)
    elif state == 'end':
        #test
        colorChoose()
        showWinner(cPlayer)
