import sys
import math
import random


def dot(u, v):

    if len(u) != len(v) or len(u) < 1:
        sys.exit("Error, vector the two vectors should be of dimension n.")

    result = 0

    for i in range(len(u)):
        result += float(u[i] * v[i])

    return result


def add(u, v):

    if len(u) != len(v) or len(u) < 1:
        sys.exit("Error, vector the two vectors should be of dimension n.")

    result = [0 for _ in range(len(u))]

    for i in range(len(u)):
        result[i] += u[i] + v[i]

    return result


def norm(u):

    if len(u) < 1:
        sys.exit("Error, vector size must be >= 1.")

    result = 0
    for i in range(len(u)):
        result += math.pow(u[i], 2)

    return math.sqrt(result)


def get_normalize_vector(u):

    if len(u) < 1:
        sys.exit("Error, vector size must be >= 1.")

    u_norm = norm(u)
    if u_norm == 0:
        sys.exit("Don't use a vector with a norm equal to 0.")

    result = [0 for _ in range(len(u))]

    for i in range(len(u)):
        result[i] = u[i] / u_norm

    return result


def get_negative_vector(u):

    if len(u) < 1:
        sys.exit("Error, vector size must be >= 1.")

    result = [0 for _ in range(len(u))]

    for i in range(len(u)):
        result[i] -= u[i]

    return result


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


a, b = generate_two_rhombus_sides(5)
a_negative = get_negative_vector(a)
ret = dot(add(a, b), add(b, a_negative))
print(ret)
