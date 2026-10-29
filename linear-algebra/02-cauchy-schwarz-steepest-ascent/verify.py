import sys
import os
import random
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from vectorops import dot, get_normalize_vector, norm


def generate_vector(dim):

    if dim < 2:
        sys.exit("Error, the minimum dimension to generate a vector is 2.")

    vector = [0 for _ in range(dim)]

    for i in range(dim):

        vector[i] = random.randint(-1000, 1000)

    return vector


# First check : Generate 10000 unit-vectors and make sure f(x) does not surpass ||v|| #
dim = random.randint(2, 1000)
vector = generate_vector(dim)
norm_vector = norm(vector)
for _ in range(10000):
    vector_2 = generate_vector(dim)
    normalized_vector = get_normalize_vector(vector_2)
    dot_product = dot(vector, normalized_vector)

    if dot_product > norm_vector:
        exit("||v|| is not the upper bound of f(x)")

print("f(x) does not surpass ||v|| in 10 000 tests")


# Second check : Verify that the upper bound is reached when x = v/||v||#
vector = generate_vector(random.randint(2, 1000))
normalized_vector = get_normalize_vector(vector)
dot_product = dot(vector, normalized_vector)
norm_vector = norm(vector)

if math.isclose(dot_product, norm_vector):
    print("f(x) equals ||v|| at x = v/||v||")
else:
    print("f(x) does not equal ||v|| at x = v/||v||")
