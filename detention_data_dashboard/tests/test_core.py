"""
Tests for the data_detention_dashboard

Includes one smoke test,  one-shot test, and edge test
"""

import unittest
import numpy as np

from .app import *


class TestEntropy(unittest.TestCase):
    """
    create class for unittests
    """

    @classmethod
    def test_smoke_figure(cls):
        """
        Simple smoke test to make sure figure appears.
        """

    def test_edge_figure(self):
        """
        Edge test to make sure figure will not display if given bad inputs
        """

    @classmethod
    def test_oneshot_figure(cls):
        """
        One shot test for figure by using fuzzy comparison of figure with known results
        """

    def test_smoke_dataself):
        """
        Simple smoke test to make sure data downloads.
        """

    def test_edge_dataself):
        """
        Edge test to make sure data  will not download if given bad inputs
        """

    @classmethod
    def test_oneshot_data(cls):
        """
        One shot test for data to make sure download has the correct information included (eg correct number of rows and columns)
        """
