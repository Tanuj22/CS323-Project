import numpy as np
from .helpers import calculate_gradient


def gradient_descent(rmap, theta, alpha=.01, num_iters=10000):
    j_history = np.zeros(shape=(num_iters, 3))

    for i in range(num_iters):
        slope = calculate_gradient(rmap, theta, j_history, i)
        if slope is None:
            break

        step = -alpha * slope
        print(f'({i}/{num_iters}): Update is {step}')
        theta += step

    return theta, j_history[:i]


def gradient_descent_w_momentum(rmap, theta, alpha=.01, gamma=.99, num_iters=10000):
    j_history = np.zeros(shape=(num_iters, 3))
    velocity = np.zeros_like(theta)

    for i in range(num_iters):
        slope = calculate_gradient(rmap, theta, j_history, i)
        if slope is None:
            break

        velocity = gamma * velocity - alpha * slope
        print(f'({i}/{num_iters}): Update is {velocity}')

        theta += velocity

    return theta, j_history[:i]
