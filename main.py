import json
from rastermap import RasterMap
import algorithms as algo

args = json.load(open('args.json'))

current_map = RasterMap(args['tif'])


algorithms = {
    'Gradient Decent' : {'function' : }
}