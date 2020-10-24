import numpy as np
from .helpers import calculate_gradient, get_possible_steps


def tabu_search(rmap, theta, tabu_size=10, num_iters=10000):
    elevation = rmap.get_elevation(*theta)
    j_history = np.zeros(shape=(num_iters, 3))
    j_history[0] = [elevation, theta[0], theta[1]]

    best_t = cand_t = theta
    tabu_list = [(tuple(theta))]

    for i in range(1, num_iters):
        steps = get_possible_steps(cand_t)

        cand_t = steps[0]
        for s in steps:
            if s not in tabu_list and rmap.get_cost(*s) < rmap.get_cost(*cand_t):
                cand_t = s

        if rmap.get_cost(*cand_t) < rmap.get_cost(*best_t):
            best_t = cand_t

        tabu_list.append(cand_t)
        if len(tabu_list) < tabu_size:
            del tabu_list[0]

        elevation = rmap.get_elevation(*best_t)
        j_history[i] = [elevation, best_t[0], best_t[1]]

        print(f'Elevation at {best_t} is {elevation}')
        print(f'({i}/{num_iters}): Update is {best_t}')

    return best_t, j_history[:i]


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
