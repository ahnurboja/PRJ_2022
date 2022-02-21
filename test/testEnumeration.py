import sys
sys.path.append('../src')

import unittest

from enumeration import EnumerationAlgorithm
from scheduler import *
from datetime import datetime

class TestClash(unittest.TestCase):

    def test_when_only_I_clash(self):
        '''
            Test that clash(m1, m2) returns false when m1 and m2 share some
            of the same attendees but no time overlap.
        '''

        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")

        m1 = Meeting([i1,i2,i3], i1, 2, 1.0, datetime(2021,12,10,18), datetime(2021,12,10,9))
        m2 = Meeting([i1,i3], i2, 2, 1.0, datetime(2021,12,10,18), datetime(2021,12,10,11))

        enumerate = EnumerationAlgorithm([i1,i2,i3],[m1,m2])
        assert not enumerate.clash(m1, m2)

    def test_when_only_T_clash(self):
        '''
            Test that clash(m1, m2) returns false when m1 and m2 overlap time
            but share no attendees.
        '''

        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")

        m1 = Meeting([i1,i2], i1, 2, 1.0, datetime(2021,12,10,18), datetime(2021,12,10,9))
        m2 = Meeting([i3], i2, 2, 1.0, datetime(2021,12,10,18), datetime(2021,12,10,10))

        enumerate = EnumerationAlgorithm([i1,i2,i3],[m1,m2])
        assert not enumerate.clash(m1, m2)
    
    # def test_when_clash(self):
    #     '''
    #         Test that clash(m1, m2) returns true when m1 and m2 overlap time
    #         and share some attendees
    #     '''