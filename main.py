import csv
import os
import json
import numpy as np
from src.rastermap import RasterMap
import src.algorithms as algo
import matplotlib.pyplot as plt

args = json.load(open('args.json'))

current_map = RasterMap(args['tif'])

algorithms = {
    'Gradient Decent': {'function': algo.gradient_descent, 'color': '#FF0000'},
    'Momentum': {'function': algo.gradient_descent_w_momentum, 'color': '#009933'}
}

# clean before running the experiment
for csv_file in os.listdir('outputs/'):
    os.remove(f'outputs/{csv_file}')

plt.style.use('ggplot')
fig = plt.figure()

for k, v in algorithms.items():
    print(f"\n{'-' * 10} {k} {'-' * 10}")
    theta, j_history = v['function'](current_map, np.array([args['center']['lat'],
                                                            args['center']['lng']]),
                                     num_iters=args['iters'])
    with open(f'{args["output"]}{"-".join(k.strip().split())}.csv',
              'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([v['color']])
        for weight in j_history:
            writer.writerow([weight[1], weight[2]])
    plt.plot(range(j_history.shape[0]), j_history[:, 0], label=k, c=v['color'])

plt.xlabel('Iterations')
plt.ylabel('Elevation')
plt.title('Hill Climbing Algorithms')
plt.legend()
plt.tight_layout()

# save the plot
fig.savefig('Cost_Plot.png', dpi=fig.dpi)
plt.show()
