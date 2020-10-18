import json
from rastermap import RasterMap

args = json.load(open('args.json'))

current_map = RasterMap(args['tif'])
