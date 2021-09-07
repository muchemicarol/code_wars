"""Find Next Perfect Square"""

import math 

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if sq % math.sqrt(sq) == 0:
        next_square = (math.sqrt(sq) + 1) ** 2
        
    else:
        next_square = -1
    return next_square
