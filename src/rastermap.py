import numpy as np
import rasterio


class RasterMap(object):
    def __init__(self, tif):
        # Open the elevation dataset
        self.data = rasterio.open(tif)

        band = self.data.read(1)
        band[band <= 0] = 0  # ignore values less than 0

        self.band = band
        self.max_val = np.max(band)

    def get_elevation(self, lat, lng):
        vals = self.data.index(lng, lat)
        return self.band[vals]

    def get_cost(self, lat, lng):
        return self.get_elevation(lat, lng) * -1 + self.max_val  # invert elevation for accent rather than decent
