"""
Tests for the figure module

Includes one smoke test, one-shot test, and edge tes
"""

import unittest
import numpy as np
import pandas as pd

from skimage.metrics import structural_similarity as ssim
from PIL import Image

from .figure import *


class TestDashboard(unittest.TestCase):
    """
    create class for unittests
    """

    def test_smoke_figure(self):
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
        for location in ["East Coast", "West Coast", "Southwest", "Midwest", "All"]:
            imageA = display_arrest_fy(location)
            imageB = Image.open(location + ".png")
            s = ssim(imageA, imageB)
            assert np.isclose(1, s, atol=.1), "image for " + location + "does not match"
        

