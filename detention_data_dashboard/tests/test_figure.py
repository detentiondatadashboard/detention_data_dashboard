"""
Tests for the figure module

Includes one smoke test, one-shot test, and edge tes
"""

import os
import numpy as np
import pandas as pd
import unittest

from detention_data_dashboard.figure import *
from matplotlib.testing.compare import compare_images

data_path = os.path.join(detention_data_dashboard.__path__[0], 'tests')

class TestDashboard(unittest.TestCase):
    """
    create class for unittests
    """

    def test_smoke_figure(self):
        """
        Simple smoke test to make sure object is created of the right type
        """
        foo = display_aor_plot("West Coast")
        self.assertTrue(str(type(foo)) == "<class 'plotly.graph_objs._figure.Figure'>")

    def test_edge_figure(self):
        """
        Edge test to make sure figure will not display if given bad inputs
        """
        with self.assertRaises(NameError):
            display_aor_plot("jumping_jacks")

    def test_oneshot_figure(self):
        """
        One shot test for figure by using fuzzy comparison of figure with known results
        """
        for location in ["East Coast", "West Coast", "Southwest", "Midwest", "All"]:
            temp = display_aor_plot(location)
            temp.write_image(data_path + "/test_images/" + location + "1.png")
            imageA = data_path + "/test_images/" + location + "1" + ".png"
            imageB = data_path + "/test_images/" + location + ".png"
            self.assertTrue(str(type(compare_images(imageA, imageB, tol=.1))) == "<class 'NoneType'>")
