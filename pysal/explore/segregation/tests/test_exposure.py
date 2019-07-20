import unittest
import pysal.lib
import geopandas as gpd
import numpy as np
from pysal.explore.segregation.aspatial import Exposure


class Exposure_Tester(unittest.TestCase):
    def test_Exposure(self):
        s_map = gpd.read_file(pysal.lib.examples.get_path("sacramentot2.shp"))
        df = s_map[['geometry', 'HISP_', 'TOT_POP']]
        index = Exposure(df, 'HISP_', 'TOT_POP')
        np.testing.assert_almost_equal(index.statistic, 0.7680384513540848)


if __name__ == '__main__':
    unittest.main()
