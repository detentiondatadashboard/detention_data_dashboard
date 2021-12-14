"""
Tests for the data_detention_dashboard

Includes one smoke test,  one-shot test, and edge test
"""

import unittest
import numpy as np
import pandas as pd
import yaml

from skimage.metrics import structural_similarity as ssim
from PIL import Image

from .app import *


class TestDashboard(unittest.TestCase):
    """
    create class for unittests
    """

    def test_smoke_data(self):
        """
        Simple smoke test to make sure the data downloaded is a dataframe
        """
        foo = data_download(arrests)
	assertEqual(type(foo) == "DataFrame")

    def test_edge_data(self):
        """
        Edge test to make sure data  will not download if given bad inputs
        """
        with self.assertRaises(NameError):
            data_download(jumping_jacks)

    def test_oneshot_data(self):
        """
        One shot test for data to make sure download has the correct information included (eg correct number of rows and columns)
        """
        data = np.array([[dataset, rows, columns], 
                         [arrests, 544059, 9], 
                         [encounters, 1689378, 8], 
                         [removals, 963972, 10]])
        foo = data_download(arrests)
        assertEqual(foo.columns == data[[arrests,2]]

    def test_smoke_figure(self):
        """
        Simple smoke test to make sure object is created of the right type
        """
        foo = display_arrest_fy("West Coast")
        assertEqual(type(foo) == "plotly.graph_objects.Figure")

    def test_edge_figure(self):
        """
        Edge test to make sure figure will not display if given bad inputs
        """
        with self.assertRaises(NameError):
            display_arrest_fy("jumping_jacks")

    def test_oneshot_figure(self):
        """
        One shot test for figure by using fuzzy comparison of figure with known results
        """
        imageA = display_arrest_fy("West Coast")
        imageB = Image.open("saved_image")
        s = ssim(imageA, imageB)
        assert np.isclose(1, s, atol=.1)

