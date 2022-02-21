import sys
sys.path.append('../src')

import unittest

from enumeration import EnumerationAlgorithm
from scheduler import *
from datetime import datetime
from copy import copy

class TestClash(unittest.TestCase):

    def test_when_only_I_clash(self):
        '''
            Test that clash(m1, m2) returns false when m1 and m2 share some
            of the same attendees but no time overlap.
        '''

        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")

        m1 = Meeting('m1', [i1,i2,i3], i1, 2, 1.0, datetime(2021,12,10,18), datetime(2021,12,10,9))
        m2 = Meeting('m2', [i1,i3], i2, 2, 1.0, datetime(2021,12,10,18), datetime(2021,12,10,11))

        enumerate = EnumerationAlgorithm([],[])
        assert not enumerate.clash(m1, m2)

    def test_when_only_T_clash(self):
        '''
            Test that clash(m1, m2) returns false when m1 and m2 overlap time
            but share no attendees.
        '''

        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")

        m1 = Meeting('m1', [i1,i2], i1, 2, 1.0, datetime(2021,12,10,18), datetime(2021,12,10,9))
        m2 = Meeting('m2', [i3], i2, 2, 1.0, datetime(2021,12,10,18), datetime(2021,12,10,10))

        enumerate = EnumerationAlgorithm([],[])
        assert not enumerate.clash(m1, m2)
    
    def test_when_clash(self):
        '''
            Test that clash(m1, m2) returns true when m1 and m2 overlap time
            and share some attendees
        '''

        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")

        m1 = Meeting('m1', [i1,i2,i3], i1, 2, 1.0, datetime(2021,12,10,18), datetime(2021,12,10,9))
        m2 = Meeting('m2', [i1,i3], i2, 2, 1.0, datetime(2021,12,10,18), datetime(2021,12,10,10))

        enumerate = EnumerationAlgorithm([],[])
        assert enumerate.clash(m1, m2)

class TestGetSolution(unittest.TestCase):

    def test_simple_case_with_optimal(self):
        '''
            Test that getSolution() with 4 meetings that always clash returns 
            correct optimal solution.
        '''
    
        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")

        m1 = Meeting('m1', [i1,i2,i3], i1, 2, 4.0, datetime(2021,12,10,16), None)
        m2 = Meeting('m2', [i1,i2,i3], i2, 2, 3.0, datetime(2021,12,10,16), None)
        m3 = Meeting('m3', [i1,i2,i3], i2, 4, 2.0, datetime(2021,12,10,16), None)
        m4 = Meeting('m4', [i1,i2,i3], i2, 3, 1.0, datetime(2021,12,10,16), None)

        enumerate = EnumerationAlgorithm([i1,i2,i3],[m1,m2,m3,m4])
        S = enumerate.getSolution()

        expectedm1 = copy(m1)
        expectedm1.t = datetime(2021,12,10,5)
        expectedm2 = copy(m2)
        expectedm2.t = datetime(2021,12,10,7)
        expectedm3 = copy(m3)
        expectedm3.t = datetime(2021,12,10,9)
        expectedm4 = copy(m4)
        expectedm4.t = datetime(2021,12,10,13)
        expectedS = [expectedm1, expectedm2, expectedm3, expectedm4]

        assert S == expectedS
    
    def test_simple_case_with_no_optimal(self):
        '''
            Test that getSolution() with 4 meetings that always clash returns 
            correct solution when there is no optimal.
        '''

        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")

        m1 = Meeting('m1', [i1,i2,i3], i1, 2, 4.0, datetime(2021,12,10,17), None)
        m2 = Meeting('m2', [i1,i2,i3], i2, 2, 3.0, datetime(2021,12,10,8), None)
        m3 = Meeting('m3', [i1,i2,i3], i2, 4, 2.0, datetime(2021,12,10,17), None)
        m4 = Meeting('m4', [i1,i2,i3], i2, 3, 1.0, datetime(2021,12,10,13), None)

        enumerate = EnumerationAlgorithm([i1,i2,i3],[m1,m2,m3,m4])
        S = enumerate.getSolution()

        expectedm1 = copy(m1)
        expectedm1.t = datetime(2021,12,10,5)
        expectedm3 = copy(m3)
        expectedm3.t = datetime(2021,12,10,7)
        expectedS = [expectedm1, expectedm3]

        assert S == expectedS


    def test_complex_case_with_optimal(self):
        '''
            Test that getSolution() with 5 meetings where some clash and
            some do not clash returns correct optimal solution.
        '''

        i1 = Individual("i1")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")

        m1 = Meeting('m1', [i1,i2], i1, 2, 5.0, datetime(2021,12,10,20), None)
        m2 = Meeting('m2', [i1,i4], i2, 2, 4.0, datetime(2021,12,10,20), None)
        m3 = Meeting('m3', [i2], i2, 4, 3.0, datetime(2021,12,10,20), None)
        m4 = Meeting('m4', [i1,i3], i2, 3, 2.0, datetime(2021,12,10,20), None)
        m5 = Meeting('m5', [i3,i4], i2, 2, 1.0, datetime(2021,12,10,20), None)

        enumerate = EnumerationAlgorithm([i1,i2,i3],[m1,m2,m3,m4,m5])
        S = enumerate.getSolution()

        expectedm1 = copy(m1)
        expectedm1.t = datetime(2021,12,10,5)
        expectedm2 = copy(m2)
        expectedm2.t = datetime(2021,12,10,7)
        expectedm3 = copy(m3)
        expectedm3.t = datetime(2021,12,10,7)
        expectedm4 = copy(m4)
        expectedm4.t = datetime(2021,12,10,9)
        expectedm5 = copy(m5)
        expectedm5.t = datetime(2021,12,10,5)
        expectedS = [expectedm1, expectedm2, expectedm3, expectedm4, expectedm5]


        assert S == expectedS


    # def test_complex_case_with_no_optimal(self):
    #     '''
    #         Test that getSolution() with 5 meetings where some clash and
    #         some do not clash returns correct solution when there is no optimal.
    #     '''