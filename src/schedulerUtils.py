from copy import deepcopy
from scheduler import *
from datetime import timedelta
import copy
import heapq

def binSearch(S, iStart):

    lo = 0
    hi = iStart - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if S[mid].t+timedelta(hours=S[mid].l) <= S[iStart].t or set(S[mid].A).isdisjoint(S[iStart].A):
            if S[mid+1].t+timedelta(hours=S[mid+1].l) <= S[iStart].t or set(S[mid+1].A).isdisjoint(S[iStart].A):
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1

def getUtility(S):

    S = sorted(S, key = lambda j: j.t+timedelta(hours=j.l))

    n = len(S)
    table = [0 for _ in range(n)]

    table[0] = S[0].w

    for i in range(1, n):
        inclProf = S[i].w
        l = binSearch(S, i)
        if (l != -1):
            inclProf += table[l]
        
        table[i] = max(inclProf, table[i-1])

    return table[n-1]

def intersect(m1, m2):
        return max(m1.t,m2.t) < min(m1.t+timedelta(hours=m1.l),m2.t+timedelta(hours=m2.l)) and not set(m1.A).isdisjoint(m2.A)
