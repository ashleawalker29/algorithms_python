def get_player_choice(opponent, player):
    choice = ''
    # If the round should be a loss.
    if player.lower() == 'x':
        if opponent.lower() == 'a':
            choice = 'c'
        elif opponent.lower() == 'b':
            choice = 'a'
        elif opponent.lower() == 'c':
            choice = 'b'
    # If the round should be a draw.
    if player.lower() == 'y':
        choice = opponent.lower()
    # If the round should be a win.
    if player.lower() == 'z':
        if opponent.lower() == 'a':
            choice = 'b'
        elif opponent.lower() == 'b':
            choice = 'c'
        elif opponent.lower() == 'c':
            choice = 'a'

    return choice

def get_status_score(opponent, player):
    status = 'loss'
    # Get player's win/lose/draw score for the round.
    if opponent.lower() == player.lower():
        status = 'draw'
    elif ((opponent.lower() == 'a' and player.lower() == 'b') or
          (opponent.lower() == 'b' and player.lower() == 'c') or
          (opponent.lower() == 'c' and player.lower() == 'a')):
        status = 'win'

    if status == 'loss':
        return 0
    elif status == 'draw':
        return 3
    elif status == 'win':
        return 6

def single_round(opponent, player):
    """ Returns the total number of points gained for the round. """

    choice = get_player_choice(opponent, player)

    score = get_status_score(opponent, choice)

    # If it was a win or a draw, calculate added score with object used
    if choice.lower() == 'a':
        score += 1
    elif choice.lower() == 'b':
        score += 2
    elif choice.lower() == 'c':
        score += 3

    return score

def eval_rounds_p2(file):
    total_score = 0

    f = open(file, 'r')

    for line in f:
        # Santize line
        line = line.strip('\n').split()
        if line:
            total_score += single_round(line[0], line[1])

    f.close()

    return total_score
