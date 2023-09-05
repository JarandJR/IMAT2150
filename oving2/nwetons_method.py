import numpy as np


def newton_solve(f, df, x0, tol, max_iter=100):
    iter_count = 0
    while True:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol or iter_count >= max_iter:
            return x1
        x0 = x1
        iter_count += 1


f = lambda radius: ((2 / 3) * np.pi * radius ** 3 + 1/3 * np.pi * radius ** 2 * cone_height) - total_volume
df = lambda radius: 2 * np.pi * radius * (radius + cone_height)



cone_height, total_volume = 10, 60

initial_radius_guess, tolerance = 2, 1e-8

radius = newton_solve(f, df, initial_radius_guess, tolerance, max_iter=100)
