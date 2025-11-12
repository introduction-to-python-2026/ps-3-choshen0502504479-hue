def approximate_pi(n_terms):
import random
num_points = 10000000
in_or_out = []
for X in range(10000000) :
    in_or_out.append(((random.random() - 0.5)**2 + (random.random()-0.5)**2)**0.5 <= 0.5)
tozaa = 4 * sum(in_or_out)/num_points
print(tozaa)
