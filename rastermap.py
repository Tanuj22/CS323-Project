import rasterio


class RasterMap(object):
    def __init__(self, tif):
        # Open the elevation dataset
        self.data = rasterio.open(tif)

        # ignore values less than 0
        band = self.data.read(1)
        band[band <= 0] = 0

        self.band = band

    def get_elevation(self, lat, lon):
        vals = self.data.index(lon, lat)
        return self.band[vals]

    def compute_cost(self, theta):
        lat, lon = theta[0], theta[1]
        j = self.get_elevation(lat, lon)

        return j
