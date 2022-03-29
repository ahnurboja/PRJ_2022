import sys
sys.path.append('../src')

import unittest

import schedulerUtils as su
from scheduler import *
from datetime import datetime, timedelta

class TestRemoveOverlaps(unittest.TestCase):

    def test_remove_overlaps_on_overlaps(self):

        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")

        m1 = Meeting('m1', [i1,i2,i3], i1, 5, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,9))
        m2 = Meeting('m2', [i3,i4,i5], i3, 2, 3.0, datetime(2021,12,10,18),  datetime(2021,12,10,11))
        m3 = Meeting('m3', [i3,i4,i5], i3, 3, 2.0, datetime(2021,12,10,18),  datetime(2021,12,10,11))
        m4 = Meeting('m4', [i3,i4,i5], i3, 2, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,15))
        m5 = Meeting('m5', [i1,i2], i3, 3, 2.0, datetime(2021,12,10,18),  datetime(2021,12,10,14))

        S = [m1,m2,m3,m4,m5]

        # print(su.removeOverlaps(S))
    
    def test_getCost_with_no_time_overlap_and_no_attendee_overlap(self):

        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")

        m1 = Meeting('m1', [i1,i2,i3], i1, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,9))
        m2 = Meeting('m2', [i4], i4, 2, 3.0, datetime(2021,12,10,18),  datetime(2021,12,10,11))
        m3 = Meeting('m3', [i5], i5, 3, 2.0, datetime(2021,12,10,18),  datetime(2021,12,10,15))

        S = [m1,m2,m3]

        assert su.getUtility(S) == 6

    def test_getCost_with_time_overlap_and_attendee_overlap(self):

        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")

        m1 = Meeting('m1', [i1,i2,i3], i1, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,9))
        m2 = Meeting('m2', [i3,i4], i4, 2, 3.0, datetime(2021,12,10,18),  datetime(2021,12,10,11))
        m3 = Meeting('m3', [i4,i5], i5, 3, 2.0, datetime(2021,12,10,18),  datetime(2021,12,10,12))

        S = [m1,m2,m3]

        assert su.getUtility(S) == 4

    def test_getCost_with_time_overlap_but_no_attendee_overlap(self):

        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")

        m1 = Meeting('m1', [i1,i2], i1, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,9))
        m2 = Meeting('m2', [i3,i4], i3, 2, 3.0, datetime(2021,12,10,18),  datetime(2021,12,10,15))
        m3 = Meeting('m3', [i5], i5, 3, 2.0, datetime(2021,12,10,18),  datetime(2021,12,10,15))

        S = [m1,m2,m3]

        assert su.getUtility(S) == 6

    def test_getCost_with_attendee_overlap_but_no_time_overlap(self):

        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")

        m1 = Meeting('m1', [i1,i2,i3], i1, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,6))
        m2 = Meeting('m2', [i3,i4,i5], i3, 2, 3.0, datetime(2021,12,10,18),  datetime(2021,12,10,10))
        m3 = Meeting('m3', [i5], i5, 3, 2.0, datetime(2021,12,10,18),  datetime(2021,12,10,15))

        S = [m1,m2,m3]

        assert su.getUtility(S) == 6

class TestIntersect(unittest.TestCase):

    def test_intersect_returns_true(self):
        """
        Test that when two meetings overlap in both time and attendees, intersect returns true
        """
        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")

        m1 = Meeting('m1', [i1,i2,i3], i1, 5, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,9))
        m2 = Meeting('m2', [i3,i4,i5], i3, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,11))

        I=[]
        M=[]

        assert su.intersect(m1,m2)
    
    def test_intersect_returns_false_with_A_overlap(self):
        """
        Test that when two meetings overlap in attendees but not time, intersect returns false
        """
        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")

        m1 = Meeting('m1', [i1,i2,i3], i1, 5, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,4))
        m2 = Meeting('m2', [i3,i4,i5], i3, 1, 1.0, datetime(2021,12,10,18),  datetime(2021,12,10,14))

        I=[]
        M=[]

        assert not su.intersect(m1,m2)
    
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

        assert not su.intersect(m1,m2)
    
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

        assert not su.intersect(m1,m2)

if __name__ == '__main__':
    unittest.main()