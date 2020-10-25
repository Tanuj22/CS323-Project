import numpy as np


def get_step_costs(rmap, steps):
    cost = []
    for s in steps:
        cost.append(rmap.get_cost(*s))
    return cost


def get_possible_steps(theta, n_points=100, step_size=.002):
    c_s = 2 * np.pi / n_points
    lat, lng = theta[0], theta[1]
    steps = []
    for i in range(n_points):
        steps.append((lat + step_size * np.sin(c_s * i),
                      lng + step_size * np.cos(c_s * i)))
    return steps


# Fetch elevations at offsets in each dimension
def get_nesw_steps(theta, step_size=.005):
    lat, lng = theta[0], theta[1]
    try:
        step_north = (lat + step_size, lng)
        step_south = (lat - step_size, lng)
        step_east = (lat, lng + step_size)
        step_west = (lat, lng - step_size)
    except IndexError:
        print('The boundary is reached')
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
