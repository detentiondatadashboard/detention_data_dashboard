"""
Tests for the data_download module

Includes one smoke test, one-shot test, and edge tes
"""

import unittest
import numpy as np
import pandas as pd

from .data_download import *


class TestDashboard(unittest.TestCase):
    """
    create class for unittests
    """

    def test_smoke_data(self):
        """
        Simple smoke test to make sure the data downloaded is a dataframe
        """
        foo = data_download("arrests")
        assertEqual(type(foo) == "DataFrame")

    def test_edge_data(self):
        """
        Edge test to make sure data  will not download if given bad inputs
        """
        with self.assertRaises(NameError):
            data_download("jumping_jacks")

    def test_oneshot_data(self):
        """
        One shot test for data to make sure download has the correct information included (eg correct number of rows and columns)
        """
        data = np.array([[dataset, rows, columns],
                         [arrests, 544059, 9],
                         [encounters, 1689378, 8],
                         [removals, 963972, 10]])
        foo = data_download("arrests")
        assertEqual(foo.columns == data[[arrests,2]]
