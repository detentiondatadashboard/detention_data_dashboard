"""
Tests for the figure module

Includes one smoke test, one-shot test, and edge tes
"""

import detention_data_dashboard
import os
import numpy as np
import pandas as pd
import unittest


from detention_data_dashboard.figure import *
from detention_data_dashboard.data_download import *
from matplotlib.testing.compare import compare_images

data_path = os.path.join(detention_data_dashboard.__path__[0], 'tests')

class TestDashboard(unittest.TestCase):
    """
    create class for unittests
    """

    def test_smoke_figure1(self):
        """
        Simple smoke test to make sure object is created of the right type
        """
        data_WC = data_download_reg("West Coast")
        foo = display_reg_plot(data_WC)
        self.assertTrue(str(type(foo)) == "<class 'plotly.graph_objs._figure.Figure'>")

    def test_edge_figure1(self):
        """
        Edge test to make sure figure will not display if given bad inputs
        """
        with self.assertRaises(NameError):
            display_reg_plot("jumping_jacks")

    def test_oneshot_figure1(self):
        """
        One shot test for figure by using fuzzy comparison of figure with known results
        """
        for location in ["East Coast", "West Coast", "Southwest", "Midwest", "All"]:
            data = data_download_reg(location)
            temp = display_reg_plot(data)
            temp.write_image(data_path + "/test_images/" + location + "1.png")
            imageA = data_path + "/test_images/" + location + "1" + ".png"
            imageB = data_path + "/test_images/" + location + ".png"
            self.assertTrue(str(type(compare_images(imageA, imageB, tol=.1))) == "<class 'NoneType'>")

    def test_smoke_figure2(self):
        """
        Simple smoke test to make sure object is created of the right type
        """
        data_LOS = data_download_arrests_aor("LOS")
        foo = display_aor_arrests_plot(data_LOS)
        self.assertTrue(str(type(foo)) == "<class 'plotly.graph_objs._figure.Figure'>")

    def test_edge_figure2(self):
        """
        Edge test to make sure figure will not display if given bad inputs
        """
        with self.assertRaises(NameError):
            display_aor_arrests_plot("jumping_jacks")

    def test_oneshot_figure2(self):
        """
        One shot test for figure by using fuzzy comparison of figure with known results
        """
        for location in ['ATL', 'BAL', 'BOS', 'BUF', 'CHI', 'DAL', 'DEN', 'DET', 'ELP', 'HOU', 'HQ', 'LOS', 'MIA', 'NEW', 'NOL','NYC', 'PHI', 'PHO', 'SEA', 'SFR', 'SLC', 'SNA', 'SND', 'SPM', 'WAS']:
            data = data_download_arrests_aor(location)
            temp = display_aor_arrests_plot(data)
            temp.write_image(data_path + "/test_images/" + location + "1.png")
            imageA = data_path + "/test_images/" + location + "1" + ".png"
            imageB = data_path + "/test_images/" + location + ".png"
            self.assertTrue(str(type(compare_images(imageA, imageB, tol=.1))) == "<class 'NoneType'>")
