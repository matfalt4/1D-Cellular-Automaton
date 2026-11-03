def periodic_neighbours(automat, i):

    left = automat[(i-1)%len(automat)]
    right = automat[(i+1)%len(automat)]

    return left, right

##################################################################################################

# We assume there are a zero elements outside the automaton considered as a "walls"
# example:
# automaton = 1,1,0,0,1,1,1,2,1
# walls: automaton = 0|1,1,0,0,1,1,1,2,1|0
def absorbing_neighbours(automat, i):

    if i == 0:
        left = 0

    else:
        left = automat[i-1]


    if i == len(automat)-1:
        right = 0

    else: 
        right = automat[i+1]

    return left, right

##################################################################################################

def fire_rule(cond, left, right):

    if cond == 0:
        return 0

    elif cond == 1:
        if left == 2 or right == 2:
            return 2

        else: return 1

    elif cond == 2: return 0

