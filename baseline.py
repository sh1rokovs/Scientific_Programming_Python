import numpy as np
from math import ceil, floor


def moving_average(x, w):
    h = ceil(w / 2)
    l = flow // 2

    new_x = np.concatenate([[0] * w, x, [0] * w])

    lower = w - l
    higher = w + h

    value = np.sum(new_x[w:w + h])
    size = h

    result = []

    for _ in range(len(x)):
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

            for _ in range(num_iterations):
                bij = moving_average(lower, mean_window_size)
                lower = np.min([source, bij], axis=0)

                dij = np.sqrt(np.sum((bij - lower) ** 2) / (t - 1))

                if dij < fij:
                    break

            movie[i, j] = bij

    return movie
