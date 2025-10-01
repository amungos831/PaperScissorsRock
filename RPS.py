
# The example function below keeps track of the opponent's history and plays 
# whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, forward_play={}, opponent_history=[]):
    if not prev_play:
        prev_play = 'R'

    opponent_history.append(prev_play)  
    n = 7

    winning_moves = {
        'P': 'S', 
        'R': 'P', 
        'S': 'R'
    }

    if len(opponent_history) > n:
        last_n = "".join(opponent_history[-n:])
        forward_play[last_n] = forward_play.get(last_n, 0) + 1
        
        probable_plays = [
            "".join([*opponent_history[-(n-1):], v]) 
            for v in ['R', 'P', 'S']
        ]

        most_common = {
            k: forward_play[k]
            for k in probable_plays if k in forward_play
        }

        if most_common:
            guess = max(most_common, key=most_common.get)[-1]
        else:
            guess = 'R'
    else:
        guess = 'R'
    
    return winning_moves[guess]