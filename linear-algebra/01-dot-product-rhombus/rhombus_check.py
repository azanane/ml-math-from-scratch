import random
import sys
import os
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from vectorops import dot, add, get_normalize_vector, get_negative_vector


def generate_two_rhombus_sides(dim):

    if dim < 2:
        sys.exit("Error, the minimum dimension to generate a rhombus is 2.")

    start_point = [random.randint(-1000, 1000) for _ in range(dim)]
    second_point = [random.randint(-1000, 1000) for _ in range(dim)]
    third_point = [random.randint(-1000, 1000) for _ in range(dim)]

    vector_1 = [0 for _ in range(dim)]
    vector_2 = [0 for _ in range(dim)]

    for i in range(dim):

        vector_1[i] = second_point[i] - start_point[i]
        vector_2[i] = third_point[i] - start_point[i]

    return (get_normalize_vector(vector_1), get_normalize_vector(vector_2))


if __name__ == "__main__":

    a, b = generate_two_rhombus_sides(5)
    a_negative = get_negative_vector(a)
    ret = dot(add(a, b), add(b, a_negative))

    if math.isclose(ret, 0.0, abs_tol=1e-9):
        print("The two diagonals of a rhombus are perpendicular.")
    else:
        print("The two diagonals of a rhombus are not perpendicular.")
