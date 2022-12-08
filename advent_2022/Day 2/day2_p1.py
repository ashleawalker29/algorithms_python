def single_round(opponent, player):
    """ Returns the total number of points gained for the round. """

    status = 'loss'
    # Get player's win/lose/draw score for the round.
    if ((opponent.lower() == 'a' and player.lower() == 'x') or
        (opponent.lower() == 'b' and player.lower() == 'y') or
        (opponent.lower() == 'c' and player.lower() == 'z')):
        status = 'draw'
    elif ((opponent.lower() == 'a' and player.lower() == 'y') or
          (opponent.lower() == 'b' and player.lower() == 'z') or
          (opponent.lower() == 'c' and player.lower() == 'x')):
        status = 'win'

    score = 0
    if status == 'loss':
        score += 0
    elif status == 'draw':
        score += 3
    elif status == 'win':
        score += 6

    # If it was a win or a draw, calculate added score with object used
    if player.lower() == 'x':
        score += 1
    elif player.lower() == 'y':
        score += 2
    elif player.lower() == 'z':
        score += 3

    return score

def eval_rounds(file):
    total_score = 0

    f = open(file, 'r')

    for line in f:
        # Santize line
        line = line.strip('\n').split()
        if line:
            total_score += single_round(line[0], line[1])

    f.close()

    return total_score
