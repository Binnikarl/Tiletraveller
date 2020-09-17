# Þufum fyrst tvær breytur sem segja okkur hvar upphafsstaður er, 
# og mun svo segja okkur hvar leikmaðurinn er staddur eftir því sem að við færum okkur
# Þurfum að búa til fall, tekur inn hvert leikmaður vill ferðast og updater staðsetninguna eða ekki(tjékkar hvort það virki)
# Þurfum að skilgreina öll "Tiles" og hvert leikmaðurinn má ferðast í því tilteknu "Tile"

#Upphafsstaða - í room1_1

x_pos,y_pos=1,1

N = '(N)orth'
S = '(S)outh'
E = '(E)ast'
W = '(W)est'

direction = ''
possible_moves = ''


def mover(x,y,direction):
    direction=direction.lower()

    if direction == 'n':
        return x, y+1
    elif direction == 's':
        return x, y-1
    elif direction == 'e':
        return x + 1, y
    elif direction == 'w':
        return x - 1, y

def print_moves(x,y):
    
    if (x_pos == 1 and y_pos == 1) or (x_pos == 2 and y_pos == 1):
        possible_moves='n'
        print("You can travel: {}.". format(N))

    elif (x_pos == 1 and y_pos == 2):
        possible_moves = 'n','s','e'
        print("You can travel: {} or {} or {}.". format(N,E,S))

    elif (x_pos == 1 and y_pos == 3):
        possible_moves = 'e', 's'
        print("You can travel: {} or {}.". format(E,S))

    elif (x_pos == 2 and y_pos == 3):
        possible_moves = 'w', 'e'
        print("You can travel: {} or {}.". format(E,W))
    elif (x_pos == 2 and y_pos == 2):
         possible_moves = 'w', 's'
         print("You can travel: {} or {}.". format(S,W))
        
    elif (x_pos == 3 and y_pos == 3):
       possible_moves = 'w', 's'
       print("You can travel: {} or {}.". format(S,W))
    elif (x_pos == 3 and y_pos == 2):
        possible_moves = 'n', 's'
        print("You can travel: {} or {}.". format(N,S))
    elif (x_pos == 3 and y_pos == 1):
        print('Victory!')

    return possible_moves

while 1: 

    if direction in possible_moves:

        possible_moves = print_moves(x_pos,y_pos)
        
    #if x_pos == 3 and y_pos ==1:
    #   break
        
    

    direction = input('Direction: ').lower()

    if direction in possible_moves:
        x_pos,y_pos = mover(x_pos,y_pos,direction)

    else:
        print('Not a valid direction!')
        print_moves(x_pos,y_pos)

