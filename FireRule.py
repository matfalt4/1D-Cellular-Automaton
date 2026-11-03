import numpy as np

from AC_lib import periodic_neighbours, absorbing_neighbours, fire_rule

def iteration(automat, condition):

    new_automat = np.zeros_like(automat)
    
    for i in range(len(automat)):

        if condition == "periodic":
            left, right = periodic_neighbours(automat, i)

        elif condition == "absorbing":
            left, right = absorbing_neighbours(automat, i)

        new_automat[i] = fire_rule(automat[i], left, right)

    return new_automat

