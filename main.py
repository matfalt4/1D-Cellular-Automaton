import numpy as np

# from AC_lib import periodic_neighbours, absorbing_neighbours, fire_rule
from FireRule import iteration

size = int(input("Provide a size of cellular automat: "))
number_of_steps = int(input("Provide a number of iterations: "))

automat = np.random.randint(0,3,size)

print("Automaton before the fire:")
print(automat)

print("Periodic:")
automat_per = iteration(automat, "periodic")
print(automat_per)

print("Absorbing:")
automat_ab = iteration(automat, "absorbing")
print(automat_ab)

