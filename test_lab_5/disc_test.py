import cProfile
from multiprocessing import Pool, cpu_count

import numpy as np


def multiply_matrices(args):
    a, b = args
    return np.dot(a, b)


def parallel_matrix_multiplication(matrices):
    with Pool(cpu_count()) as pool:
        result = pool.map(multiply_matrices, matrices)
    return result


def main():
    M = 100
    N = 10
    matrices_A = [np.random.rand(M, M) for _ in range(N)]
    matrices_B = [np.random.rand(M, M) for _ in range(N)]

    matrices_to_multiply = zip(matrices_A, matrices_B)
    result = parallel_matrix_multiplication(matrices_to_multiply)


if __name__ == "__main__":
    cProfile.run("main()", filename="profile_results.txt")
