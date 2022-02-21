import sys
sys.path.append('../src')

import unittest

from randomAlgorithm import RandomAlgorithm
from scheduler import *
from datetime import datetime

class TestGetCost(unittest.TestCase):
    def test_cost_zero_for_optimal(self):
        """
        Test that the cost calculated from an optimal solution is zero
        """
        i1 = Individual("i1", [])
        i2 = Individual("i2", [])
        i3 = Individual("i3", [])
        i4 = Individual("i4", [])
        i5 = Individual("i5", [])

        m1 = Meeting([i1,i3,i4,i5], i1, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,9))
        m2 = Meeting([i1,i3,i4,i5], i3, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,11))
        m3 = Meeting([i4,i5], i4, 2, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,16))

        I=[]
        M=[m1,m2,m3]    
        S=[m1,m2,m3]

        randomAlgorithm = RandomAlgorithm(I, M)
        C = randomAlgorithm.getCost(S)

        assert C == 0

    def test_correct_cost(self):
        """
        Test that the cost calculated from different solutions is correct
        """
        i1 = Individual("i1", [])
        i2 = Individual("i2", [])
        i3 = Individual("i3", [])
        i4 = Individual("i4", [])
        i5 = Individual("i5", [])

        m1 = Meeting([i1,i3,i4,i5], i1, 1, 2, datetime(2021,12,10,18),  datetime(2021,12,10,9))
        m2 = Meeting([i1,i3,i4,i5], i3, 1, 1.5, datetime(2021,12,10,18),  datetime(2021,12,10,11))
        m3 = Meeting([i4,i5], i4, 2, 0.5, datetime(2021,12,10,18),  datetime(2021,12,10,16))

        I=[]
        M=[m1,m2,m3]

        randomAlgorithm = RandomAlgorithm(I, M)

        S1=[m1]         # cost = 1 - (2/4) = 0.5
        S2=[m2]         # cost = 1 - (1.5/4) = 0.625
        S3=[m3]         # cost = 1 - (0.5/4) = 0.875
        S12=[m1,m2]     # cost = 1 - (3.5/4) = 0.125
        S13=[m1,m3]     # cost = 1 - (2.5/4) = 0.375
        S23=[m2,m3]     # cost = 1 - (2/4) = 0.5

        assert randomAlgorithm.getCost(S1) == 0.5
        assert randomAlgorithm.getCost(S2) == 0.625
        assert randomAlgorithm.getCost(S3) == 0.875
        assert randomAlgorithm.getCost(S12) == 0.125
        assert randomAlgorithm.getCost(S13) == 0.375
        assert randomAlgorithm.getCost(S23) == 0.5


class TestRemoveOverlap(unittest.TestCase):
    def test_remove_overlap(self):
        """
        Test that overlaps are removed when there is a clash with time and individuals
        """
        i1 = Individual("i1", [])
        i2 = Individual("i2", [])
        i3 = Individual("i3", [])
        i4 = Individual("i4", [])
        i5 = Individual("i5", [])

        m1 = Meeting([i1,i2,i3], i1, 6, 1, datetime(2021,12,10,9),  datetime(2021,12,10,15))
        m2 = Meeting([i1,i3,i4,i5], i3, 4, 1, datetime(2021,12,10,13),  datetime(2021,12,10,17))
        m3 = Meeting([i2,i5], i4, 4, 0, datetime(2021,12,10,11),  datetime(2021,12,10,16))
        m4 = Meeting([i3,i4,i5], i4, 4, 0, datetime(2021,12,10,10),  datetime(2021,12,10,14))
        m5 = Meeting([i4,i5], i4, 4, 0, datetime(2021,12,10,12),  datetime(2021,12,10,16))

        I=[i1,i3,i4,i5]
        M=[m1,m2,m3,m4,m5]

        S1=[m1,m2,m5]

        randomAlgorithm = RandomAlgorithm(I, M)

        S1=randomAlgorithm.removeOverlaps(S1)

        assert S1 == {m1,m5} or S1 == {m2}

if __name__ == '__main__':
    unittest.main()