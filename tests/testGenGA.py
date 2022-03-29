import sys
sys.path.append('../src')

import unittest

from genGA import GeneticAlgorithm
from scheduler import *
from datetime import datetime

class TestRemoveOverlaps(unittest.TestCase):

    def test_intersect_returns_true(self):
        """
        Test that when two meetings overlap in both time and attendees, intersect returns true
        """
        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")

        m1 = Meeting('m1', [i1,i3], i1, 5, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,9))
        m2 = Meeting('m2', [i3,i4,i5], i3, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,11))

        I=[]
        M=[]

        GA = GeneticAlgorithm(I,M,1)
        assert GA.intersect(m1,m2)
    
    def test_intersect_returns_false_with_A_overlap(self):
        """
        Test that when two meetings overlap in attendees but not time, intersect returns false
        """
        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")

        m1 = Meeting('m1', [i1,i3], i1, 5, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,4))
        m2 = Meeting('m2', [i3,i4,i5], i3, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,14))

        I=[]
        M=[]

        GA = GeneticAlgorithm(I,M,1)
        assert not GA.intersect(m1,m2)
    
    def test_intersect_returns_false_with_t_overlap(self):
        """
        Test that when two meetings overlap in time but not attendees, intersect returns false
        """
        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")

        m1 = Meeting('m1', [i1,i2], i1, 5, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,13))
        m2 = Meeting('m2', [i3,i4,i5], i3, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,14))

        I=[]
        M=[]

        GA = GeneticAlgorithm(I,M,1)
        assert not GA.intersect(m1,m2)
    
    def test_intersect_returns_false_with_no_overlap(self):
        """
        Test that when two meetings never overlap in time nor attendees, intersect returns false
        """
        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")

        m1 = Meeting('m1', [i1,i2], i1, 5, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,4))
        m2 = Meeting('m2', [i3,i4,i5], i3, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,14))

        I=[]
        M=[]

        GA = GeneticAlgorithm(I,M,1)
        assert not GA.intersect(m1,m2)

    def test_remove_overlap(self):
        """
        Test that overlaps are removed when there is a clash with time and individuals
        """
        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")

        m1 = Meeting('m1', [i1,i2,i3], i1, 6, 1, datetime(2021,12,10,23),  datetime(2021,12,10,15))
        m2 = Meeting('m2', [i1,i3,i4,i5], i3, 4, 1, datetime(2021,12,10,23),  datetime(2021,12,10,17))
        m3 = Meeting('m3', [i2,i5], i4, 4, 0, datetime(2021,12,10,23),  datetime(2021,12,10,16))
        m4 = Meeting('m4', [i3,i4,i5], i4, 4, 0, datetime(2021,12,10,23),  datetime(2021,12,10,14))
        m5 = Meeting('m5', [i4,i5], i4, 4, 0, datetime(2021,12,10,23),  datetime(2021,12,10,16))

        I=[i1,i3,i4,i5]
        M=[m1,m2,m3,m4,m5]

        S1=[m1,m2,m5]

        ga = GeneticAlgorithm(I, M, 1)

        S1=ga.removeOverlaps(S1)

        print(S1)

        assert S1 == {m1,m5} or S1 == {m2}


if __name__ == '__main__':
    unittest.main()