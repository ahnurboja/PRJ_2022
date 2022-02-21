import unittest

from algorithms.enumeration import EnumerationAlgorithm
from algorithms.scheduler import *
from datetime import datetime

class TestGetSolution(unittest.TestCase):
    def test_get_solution(self):
        """
        Test that 
        """

        i1 = Individual("i1", [])
        i2 = Individual("i2", [])
        i3 = Individual("i3", [])
        i4 = Individual("i4", [])
        i5 = Individual("i5", [])

        m1 = Meeting([i1,i3,i4,i5], i1, 3, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,9))
        m2 = Meeting([i1,i3,i4,i5], i3, 2, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,11))

        enumerationAlgorithm = EnumerationAlgorithm
        
        enumerationAlgorithm