# Jogo-da-Velha
Jogo da Velha em Phyton
#Tic-Tac-Toe#

from time import sleep
from random import random
import sys

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 

pts_player = 0
pts_pc = 0

while True:

    j = ''
    first = ''
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    lv = 'free'
    pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = lv, lv, lv, lv, lv, lv, lv, lv, lv
    move = 0
    play_adv = 0
    random_play = 0
    shifts = 1
    winner = ''

    start_board = '''
--- HOW TO PLAY ---
When it's your turn, enter the number corresponding to the position on the board to make your move on it.
For example, let's say you want to play center, so you type 5.
     | |
  1 | 2 | 3
_____|_____|_____
     | |
  4 | 5 | 6
_____|_____|_____
     | |
  7 | 8 | 9
     | |
    '''

    print(initial_board)

    print('Do you want to be the X (X) or the O (ball)?', end=' ')

    while j != 'O' and j != 'X':
        j = str(input('Type X or O and press Enter to choose: ')).strip().upper()
        if j != 'O' and j != 'X':
            print('\nInvalid choice!\n')

    if j == 'O':
        adv = 'X'
        print('\nSo I keep the X.')
    elif j == 'X':
        adv = 'O'
        print('\nSo I'll take O.')

    print('\nWho plays first?', end=' ')

    while first != 'EU' and first != 'PC':
        instr = 'Type EU and press Enter to get you started, or type PC and press Enter to get me started: '
        first = str(input(instr)).strip().upper()
        if first != 'ME' and first != 'PC':
            print('\nInvalid choice!\n')

    if first == 'I':
        print('\nSo you play first.\n')
    elif first == 'PC':
        print('\nThen I play first.\n')

    def update_board():
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        board = '''
     | |
  {} | {} | {}
_____|_____|_____
     | |
  {} | {} | {}
_____|_____|_____
     | |
  {} | {} | {}
     | |
        '''.format(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print(board)

    def play_j1():
        global play

        while True:
            try:
                move = int(input('Enter the position of your move (1 to 9) and press Enter: '))
                break
            except ValueError:
                print('\nInvalid value entered. Enter an integer from 1 to 9!\n')

    def routine_j1():
        global play
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9
        msg_occupied = '\nThis space is already occupied!\n'

        move_j1()

        while played not in range(1, (9 + 1)):
            move_j1()

            if played not in range(1, (9 + 1)):
                print('\nInvalid number!\n')

        while played == 1 and pos1 == 'busy' or \
            move == 2 and pos2 == 'busy' or \
            move == 3 and pos3 == 'busy' or \
            move == 4 and pos4 == 'busy' or \
            move == 5 and pos5 == 'busy' or \
            move == 6 and pos6 == 'busy' or \
            move == 7 and pos7 == 'busy' or \
            move == 8 and pos8 == 'busy' or \
                move == 9 and pos9 == 'busy':
            print(msg_busy)
            routine_j1()

    def update_plays_j1():
        global play
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        if play == 1:
            p1 = j
            pos1 = 'busy'
        elif played == 2:
            p2 = j
            pos2 = 'busy'
        elif played == 3:
            p3 = j
            pos3 = 'busy'
        elif played == 4:
            p4 = j
            pos4 = 'busy'
        elif played == 5:
            p5 = j
            pos5 = 'busy'
        elif played == 6:
            p6 = j
            pos6 = 'busy'
        elif played == 7:
            p7 = j
            pos7 = 'busy'
        elif played == 8:
            p8 = j
            pos8 = 'busy'
        elif played == 9:
            p9 = j
            pos9 = 'busy'

    def update_plays_j2():
        global play, random_play, adv
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        print('Let me think about my move...')
        sleep(1.5)
        random_play = randint(1, 9)
        while random_play == 1 and pos1 == 'busy' or \
            random_play == 2 and pos2 == 'busy' or \
            random_play == 3 and pos3 == 'busy' or \
            random_play == 4 and pos4 == 'busy' or \
            random_play == 5 and pos5 == 'busy' or \
            random_play == 6 and pos6 == 'busy' or \
            random_play == 7 and pos7 == 'busy' or \
            random_play == 8 and pos8 == 'busy' or \
                random_play == 9 and pos9 == 'busy':
            random_play = randint(1, 9)

        print('\nI play at position {}!'.format(random_play))

        if random_play == 1:
            p1 = adv
            pos1 = 'busy'
        elif random_play == 2:
            p2 = adv
            pos2 = 'busy'
        elif random_play == 3:
            p3 = adv
            pos3 = 'busy'
        elif random_play == 4:
            p4 = adv
            pos4 = 'busy'
        elif random_play == 5:
            p5 = adv
            pos5 = 'busy'
        elif random_play == 6:
            p6 = adv
            pos6 = 'busy'
        elif random_play == 7:
            p7 = adv
            pos7 = 'busy'
        elif random_play == 8:
            p8 = adv
            pos8 = 'busy'
        elif random_play == 9:
            p9 = adv
            pos9 = 'busy'

    def check_winner():
        global j, adv, turns, winner, pts_player, pts_pc
        global p1, p2, p3, p4, p5, p6, p7, p8, p9

        if p1 == j and p2 == j and p3 == j or \
           p1 == j and p4 == j and p7 == j or \
           p1 == j and p5 == j and p9 == j or \
           p2 == j and p5 == j and p8 == j or \
           p3 == j and p5 == j and p7 == j or \
           p3 == j and p6 == j and p9 == j or \
           p4 == j and p5 == j and p6 == j or \
           p7 == j and p8 == j and p9 == j:
            print('YOU WON!\n')
            pts_player += 1
            winner = 'I'
            turns = 10
            if p1 == adv and p2 == adv and p3 == adv or \
           p1 == adv and p4 == adv and p7 == adv or \
           p1 == adv and p5 == adv and p9 == adv or \
           p2 == adv and p5 == adv and p8 == adv or \
           p3 == adv and p5 == adv and p7 == adv or \
           p3 == adv and p6 == adv and p9 == adv or \
           p4 == adv and p5 == adv and p6 == adv or \
           p7 == adv and p8 == adv and p9 == adv:
            print('I WON!\n')
            pts_pc += 1
            winner = 'PC'
            turns = 10

    def update_all():
        global play
        global shifts
        overall winner

        if first == 'I':
            routine_j1()
            update_plays_j1()
            update_board()
            check_winner()

            if shifts == 5:
                print('WE DRAW IT!\n')
                turns = 10
                winner = 'DRAW'

            if winner == '':
                update_plays_j2()
                update_board()
                check_winner()

        elif first == 'PC':
            update_plays_j2()
            update_board()
            check_winner()

            if shifts == 5:
                print('WE DRAW IT!\n')
                turns = 10
                winner = 'DRAW'

            if winner == '':
                routine_j1()
                update_plays_j1()
                update_board()
                check_winner()

        move = 0
        shifts += 1

    while shifts <= 5:
        update_all()

    print('-------- SCORE --------')
    print('You: {} | Computer: {}'.format(pts_player, pts_pc))
    print('------------------------')

    while True:
        restart = input('\nWant to play again? Type Y for yes or N for no: ').lower()

        if restart in ('s', 'n', '"s"', '"n"'):
            break
        print('\nInvalid response!')

    if restart == 's' or restart == '"s"':
        print('\n-------------------------------------------- --------')
        continues
    else:
        sys.exit(0)
        main()
