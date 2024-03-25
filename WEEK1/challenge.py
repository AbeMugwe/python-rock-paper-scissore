player1=input('Player 1:')
player2=input('Player 2:')


match player1:
    case 'paper':
        if player2=='rock':
            print('Player 1 Wins')
        elif player2=='paper':
            print('A BORING DRAW')
        else:
            print('Player 2 Wins')
        
    case 'scissors':
        if player2=='rock':
            print('Player 2 Wins')
        elif player2=='scissors':
            print('A BORING DRAW')
        else:
            print('Player 1 Wins')
    case 'rock':
        if player2=='paper':
            print('Player 2 Wins')
        elif player2=='rock':
            print('A BORING DRAW')
        else:
            print('Player 1 Wins')
    







