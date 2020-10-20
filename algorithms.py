import numpy as np


def get_step_costs(rmap, steps):
    return [rmap.get_cost(*s) for s in steps]


# Fetch elevations at offsets in each dimension
def get_nesw_steps(theta, step_size=.005):
    try:
        step_north = (theta[0] + step_size, theta[1])
        step_south = (theta[0] - step_size, theta[1])
        step_east = (theta[0], theta[1] + step_size)
        step_west = (theta[0], theta[1] - step_size)
    except IndexError:
        print('The boundary of elevation map has been reached')
        return None

    return step_north, step_east, step_south, step_west


def calculate_gradient(rmap, theta, j_history, n_iter):
    cost = rmap.get_cost(*theta)
    elevation = rmap.get_elevation(*theta)
    j_history[n_iter] = [elevation, theta[0], theta[1]]

    step_costs = get_step_costs(rmap, get_nesw_steps(theta))

    if cost <= 0 or step_costs is None:
        return None

    # Calculate slope
    lat_slope = step_costs[0] / step_costs[2] - 1
    lon_slope = step_costs[1] / step_costs[3] - 1
    print(f'Elevation at {theta} is {elevation}')

    return np.array((lat_slope, lon_slope))


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
