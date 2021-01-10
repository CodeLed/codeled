import random
from dictionary import quiz

data = quiz.data
choose = ''
ran = -1
chosenAns = ''
listPlayers = {}
cPlayer = 0
dice = 0
state = 'start'
manual = ''
# start
# throw
# card
# cardResult
# end
x = 1250
y = 300
boardX = 350
boardY = 0
boardWidth = 900
boardHeight = 600
boardPosBox = {}
def setup():
    global x, y,  boardPosBox, boardX, boardY, boardWidth, boardHeight
    frameRate(20)
    size(x, 600)
    for i in range(1, 11):
        val = boardPosBox[len(boardPosBox) - 1]['value'] if len(boardPosBox) - 1 > 0 else 'rood'
        temp = {len(boardPosBox): {
            'x' : boardX + boardWidth - i  * (boardWidth * 0.10) + (boardWidth * 0.025),
            'y' : boardY + boardHeight - 80,
            'value' : boxValue(val, len(boardPosBox) - 1)
        }}
        boardPosBox.update(temp)

    for i in range(11, 15):
        temp = {len(boardPosBox): {
            'x' : boardX + 22.5,
            'y' : (boardY + boardHeight) - i % 10 * 100 - 75,
            'value' : boxValue(boardPosBox[len(boardPosBox) - 1]['value'], len(boardPosBox) - 1)
        }}
        boardPosBox.update(temp)
        
    for i in range(9, 0, -1):
        temp = {len(boardPosBox): {
            'x' : boardPosBox[i]['x'],
            'y' : 25,
            'value' : boxValue(boardPosBox[len(boardPosBox) - 1]['value'], len(boardPosBox) - 1)
        }}
        boardPosBox.update(temp)
    for i in range(0,5):
        temp = {len(boardPosBox): {
            'x' :boardX + boardWidth - 65,
            'y' : (boardY + 100 * i + 25),
            'value' : boxValue(boardPosBox[len(boardPosBox) - 1]['value'], len(boardPosBox) - 1)
        }}
        boardPosBox.update(temp)

def board():
    global boardPosBox, boardX, boardY, boardWidth, boardHeight, listPlayers
    image(loadImage("game.png"), boardX, boardY, boardWidth, boardHeight)
    for i in listPlayers.items():
        pos = listPlayers[i[0]]['place']
        fill(i[1]['r'], i[1]['b'], i[1]['g'])
        rect(boardPosBox[pos]['x'] + i[1]['x'], boardPosBox[pos]['y'] + i[1]['y'], 20, 20)
        fill(0)
        text(str(i[0]+1), boardPosBox[pos]['x'] + i[1]['x'] + 6, boardPosBox[pos]['y'] + i[1]['y'] + 13)

def card():
    global data, choose, ran
    fill(255,255,255)
    rect(0,0,350, 250)
    if choose == 'rood':
        fill(255,0,0)
        rect(0,0, 350,75)
    elif choose == 'geel':
        fill(255,255,0)
        rect(0,0, 350,75)
    elif choose == 'oranje':
        fill(255,128,0)
        rect(0,0, 350,75)
    elif choose == 'groen':
        fill(0,128,0)
        rect(0,0, 350,75)
    else:
        fill(255,0,0)
        rect(0,0, 350,75)
    fill(0)
    text(data[choose][ran]['vraag'], 55, 40)
    text(data[choose][ran]['antwoorden']['A'], 55, 100)
    text(data[choose][ran]['antwoorden']['B'], 55, 140)
    text(data[choose][ran]['antwoorden']['C'], 55, 180)
    text(data[choose][ran]['antwoorden']['D'], 55, 220)

def diceButton():
    fill(192,192,192)
    rect(110, 450, 120, 40)
    fill(255,255,255)
    text("Gooi dobbelsteen", 120, 475)

def throwDice():
    dice = random.randint(1,6)
    return dice

def displayDice(throwDice):
    global dice
    if dice != 0:
        return text("Dobbelsteen gegooit je gaat \nmet " + str(throwDice) + " stappen verder", 100, 500)

def showCurrentPlayerTurn(current_player):
    return text("De speler " + str(current_player + 1) + " is aan de beurt", 100, 380)

def showWinner(current_player):
    return text("SPEL AFGELOPEN. Winnende speler " + str(current_player + 1), 100, 380)

def losers(winner, totalPlayers):
    loser = []
    for i in range(1, len(totalPlayers) + 1):
        if i != winner + 1:
            loser.append(i)
    return text("Spelers " + str(loser) + " hebben verloren.", 100, 480)
    
    
def scoreboard(listPlayers):
    player_number = 1
    vertical_height = 400
    fill(255,255,255)
    for points in listPlayers:
        text("Speler " + str(player_number) + ": " + str(listPlayers[points]['points']) + " punten", 100, vertical_height)
        player_number += 1
        vertical_height += 15

def displayManual():
    global manual
    if manual != 0:
        return image(loadImage("gamemanual.png"),550, 0, 700, 600)
    
def players():
    fill(192,192,192)
    rect(50, 50, 80, 40)
    fill(255,255,255)
    text("Een spelers", 60, 75)
    
    fill(192,192,192)
    rect(170, 50, 80, 40)
    fill(255,255,255)
    text("Twee spelers", 180, 75)
    
    fill(192,192,192)
    rect(50, 150, 80, 40)
    fill(255,255,255)
    text("Drie spelers", 55, 175)
    
    fill(192,192,192)
    rect(170, 150, 80, 40)
    fill(255,255,255)
    text("Vier spelers", 180, 175)
  
def boxValue(colorName, id):
    if id == -1:
        return 'start'
    elif id == 8:
        return 'times2'
    elif id == 13:
        return 'minus4'
    elif id == 22:
        return 'times3'
    elif colorName == 'rood' or colorName == 'start' or colorName == 'times2' or colorName == 'minus4' or colorName == 'times3':
        return 'groen'
    elif colorName == 'oranje':
        return 'geel'
    elif colorName == 'groen':
        return 'oranje'
    elif colorName == 'geel':
        return 'rood'
def reset():
    global choose, chosenAns, ran, listPlayers, dice, state, cPlayer
    choose = ''
    ran = -1
    chosenAns = ''
    listPlayers = {}
    cPlayer = 0
    dice = 0
    state = 'start'
    manuel = ''
    
def rematch():
    fill(255)
    rect(75, 50, 220, 75)
    fill(0)
    text("Wil je opnieuw spelen? Klik op mij! \n\n Zo niet, klik ergens anders", 95, 75)
  
def result(res, points):
    fill(255)
    rect(50,50,250,100)
    fill(0)
    text("Je antwoord is " + res, 80, 80)
    if points == 0:
        text("Je hebt geen punten gekregen.", 80, 100)
    else:
        text("Je hebt " + str(points) + " gekregen!", 80, 100)

    
def mousePressed():
    global chosenAns, data, choose, state, listPlayers, cPlayer, dice, ran, manuel
    if state == 'start':
        if 50 < mouseX < 50 + 80 and 50 < mouseY < 50 + 40:
            chosenPlayers = 1
            listPlayers = {0 : {'points' : 0, 'place': 0, 'x': 0, 'y': 0, 'r': 0, 'b': 128, 'g': 0}}
            
        elif 170 < mouseX < 170 + 80 and 50 < mouseY < 50 + 40:
            chosenPlayers = 2
            listPlayers = {0 : {'points' : 0, 'place': 0, 'x': 0, 'y': 0, 'r': 0, 'b': 128, 'g': 0}, 
                           1 : {'points' : 0, 'place': 0, 'x': 30, 'y': 0, 'r': 255, 'b': 255, 'g': 0}}
            
        elif 50 < mouseX < 50 + 80 and 150 < mouseY < 150 + 40:
            chosenPlayers = 3
            listPlayers = {0 : {'points' : 0, 'place': 0, 'x': 0, 'y': 0, 'r': 0, 'b': 128, 'g': 0}, 
                           1 : {'points' : 0, 'place': 0, 'x': 30, 'y': 0, 'r': 255, 'b': 255, 'g': 0}, 
                           2 : {'points' : 0, 'place': 0, 'x': 0, 'y': 30, 'r': 255, 'b': 128, 'g': 0}}
            
        elif 170 < mouseX < 170 + 80 and 150 < mouseY < 150 + 40:
            chosenPlayers = 4
            listPlayers = {0 : {'points' : 0, 'place': 0, 'x': 0, 'y': 0, 'r': 0, 'b': 128, 'g': 0}, 
                           1 : {'points' : 0, 'place': 0, 'x': 30, 'y': 0, 'r': 255, 'b': 255, 'g': 0}, 
                           2 : {'points' : 0, 'place': 0, 'x': 0, 'y': 30, 'r': 255, 'b': 128, 'g': 0}, 
                           3 : {'points' : 0, 'place': 0, 'x': 30, 'y': 30, 'r': 255, 'b': 0, 'g': 0}}
            

        elif 110 < mouseX < 110+ 80 and 450 < mouseY < 450 + 40:
            dice = throwDice()
        if len(listPlayers) > 0:
            state = 'throw'
               
    elif state == 'cardResult':
        cPlayer +=1 
        if cPlayer >= len(listPlayers):
            cPlayer = 0
        ran = -1
        chosenAns = ''
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
        
        print(chosenAns)
        if data[choose][ran]['goed'] == chosenAns:
            temp = data[choose]["punten"]
            print(boardPosBox[listPlayers[cPlayer]['place']]['value'])
            if boardPosBox[listPlayers[cPlayer]['place']]['value'] == 'times2':
                print(temp)
                temp *= 2
                print(temp)
            if boardPosBox[listPlayers[cPlayer]['place']]['value'] == 'times3':
                print(temp)
                temp *= 3
                print(temp)
            listPlayers[cPlayer]['points'] += temp
        
        if listPlayers[cPlayer]['points'] > 3:
            state = 'end'
        elif not chosenAns == '':
            state = 'cardResult'
            
    elif state == 'throw':
        global x, y, choose              
        if 110 < mouseX < 110+ 80 and 450 < mouseY < 450 + 40:
            dice = throwDice()
            throw = dice
            print(str(listPlayers[cPlayer]['place'] + throw) + '/' + str(len(boardPosBox)))
            if listPlayers[cPlayer]['place'] + throw >= len(boardPosBox):
                throw -= len(boardPosBox)
            listPlayers[cPlayer]['place'] += throw
            
            choose = boardPosBox[listPlayers[cPlayer]['place']]['value']
            if choose == 'times2' or choose == 'times3':
                print('times' + str(choose))
                c = random.randint(0, 3)
                print(c)
                if c == 0:
                    choose = 'groen'
                elif c == 1:
                    choose = 'rood'
                elif c == 2:
                    choose = 'geel'
                elif c == 3:
                    choose = 'oranje'

            if choose == 'minus4':
                ran = 0
                chosenAns = 'A'
                listPlayers[cPlayer]['points'] -= 4
                state = 'cardResult'
            elif choose == 'start':
                    cPlayer +=1 
                    if cPlayer >= len(listPlayers):
                        cPlayer = 0
            else:
                state = 'card'
        else:
            state = 'throw'
        
    elif state == 'end':
        if 75 < mouseX < 275 and 50 < mouseY < 125:
            reset()
        else:
            exit()
        
        
def draw():
    global data, choose, ran, chosenAns, chosenPlayers, listPlayers, cPlayer, dice, manuel
    clear()

    if state != 'start':
        board()
    scoreboard(listPlayers)
    displayDice(dice)
    if state == 'start':
        players()
        diceButton()
        displayDice(dice)
        displayManual()
    elif state == 'cardResult':
        if data[choose][ran]['goed'] == chosenAns:
            return result("goed.", data[choose]["punten"])
            
        else:
            return result("fout.", 0)
        
    elif state == 'card':
        if ran == -1:          
            ran = random.randint(0, len(data[choose]) -2)
        card()
    elif state == 'throw':
        dice = 0
        diceButton()
        showCurrentPlayerTurn(cPlayer)
    elif state == 'end':
        showWinner(cPlayer)
        losers(cPlayer, listPlayers)
        rematch()
