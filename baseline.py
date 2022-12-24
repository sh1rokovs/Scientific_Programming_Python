import numpy as np
from math import ceil, floor


def moving_average(x, w):
    h = ceil(w / 2)
    l = floor(w // 2)
    new_x = np.concatenate([[0] * w, x, [0] * w])
    lower = w - l
    higher = w + h
    value = np.sum(new_x[w:w + h])
    size = h
    result = []

    for el in range(len(x)):
        result.append(value / size)
        value += new_x[higher]
        value -= new_x[lower]
        lower += 1
        higher += 1

        if lower > w:
            size -= 1

        if higher <= len(x) + w:
            size += 1
    return np.array(result)


def compute_baseline(movie, f_noise_sigma, mean_window_size, num_iterations):
    n, m, t = movie.shape

    for i in range(n):
        for j in range(m):
            bij = movie[i, j]
            fij = f_noise_sigma[i][j]

            source = movie[i, j]
            lower = np.min([source, bij], axis=0)

            for el in range(num_iterations):
                bij = moving_average(lower, mean_window_size)
                lower = np.min([source, bij], axis=0)

                dij = np.sqrt(np.sum((bij - lower) ** 2) / (t - 1))

                if dij < fij:
                    break

            movie[i, j] = bij

    return movie


movie = np.array(
[[[ 3, -5,  1, -1, -3,  0], [ 4, 4, 1, -5, -3, -1]],
 [[-2, -4, -2,  0,  2, -3], [-2, 2, 2,  3, -2, 0]]], dtype = np.float64)

f_noise_sigma = np.array([[1, 1], [1, 0]], dtype = np.float64)
mean_window_size = 6
num_iterations = 4

print(compute_baseline(movie, f_noise_sigma, mean_window_size, num_iterations))
# np.array([[[1.0, 1.111111, 0.777777, 1.111111, 1.0, 1.5, 1.25]]])
