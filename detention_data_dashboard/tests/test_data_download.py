"""
Tests for the data_download module

Includes three tests for the each of the two data functions
"""

import unittest

from detention_data_dashboard.data_download import *

class TestDashboard(unittest.TestCase):
    """
    create class for unittests
    """

    def test_smoke_data1(self):
        """
        Simple smoke test to make sure the data downloaded is a dataframe
        """
        fob = data_download_reg("West Coast")
        self.assertTrue(str(type(fob)) == "<class 'pandas.core.frame.DataFrame'>")

    def test_edge_data1(self):
        """
        Edge test to make sure data will not download if given bad inputs
        """
        with self.assertRaises(NameError):
            data_download_reg("jumping_jacks")

    def test_pattern_data1(self):
        """
        Pattern test for data to make sure download has the correct information included
        (eg correct number of rows and columns)
        """
        for location in ["East Coast", "West Coast", "Southwest", "Midwest", "All"]:
            fob = data_download_reg(location)
            self.assertTrue(fob.shape == (4, 4))

    def test_smoke_data2(self):
        """
        Simple smoke test to make sure the data downloaded is a dataframe
        """
        fob = data_download_arrests_aor("LOS")
        self.assertTrue(str(type(fob)) == "<class 'pandas.core.frame.DataFrame'>")

    def test_edge_data2(self):
        """
        Edge test to make sure data  will not download if given bad inputs
        """
        with self.assertRaises(NameError):
            data_download_arrests_aor("jumping_jacks")

    def test_pattern_data2(self):
        """
        Pattern test for data to make sure download has the correct information included
        (eg correct number of rows and columns)
        """

        for location in ['ATL', 'BAL', 'BOS', 'BUF', 'CHI', 'DAL', 'DEN', 'DET', 'ELP',
                         'HOU', 'HQ', 'LOS', 'MIA', 'NEW', 'NOL','NYC', 'PHI', 'PHO',
                         'SEA', 'SFR', 'SLC', 'SNA', 'SND', 'SPM', 'WAS']:
            fob = data_download_arrests_aor(location)
            self.assertTrue(fob.shape == (4, 2))
