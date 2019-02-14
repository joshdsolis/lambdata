#!/usr/bin/env python

import unittest
import numpy as np
import pandas as pd
from __init__ import *

# testing __init__ functions


class LambTest(unittest.TestCase):
    """Test lambdata_joshdsolis functions"""

    # def test_checknulls(self):
    #   df = pd.DataFrame(np.ones(100))
    #   self.assertEqual(check_nulls(df).tolist(), df.isna().sum()).tolist()

    # Testing more_rows functions in init
    def test_morerows(self):
        df = pd.DataFrame(np.ones(100))
        more_rows(df, 100)
        self.assertEqual(df.shape, (200, 1))


if __name__ == '__main__':
    unittest.main()
