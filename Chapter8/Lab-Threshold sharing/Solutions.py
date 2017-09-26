import sys
sys.path.append("D:\Python\Matrix")

from GF2 import one
from vec import Vec
from mat import Mat
from triangular import *
from echelon import *

from vecutil import *
from matutil import *
from bitutil import *
from dimension_function import *
from independence import *
from solver import solve

import itertools
import random

def randGF2(): return random.randint(0,1)*one

# 8.7.1
def choose_secret_vector(s,t):
    '''
    :param s: secret bit of GF(2)
    :param t: secret bit of GF(2)
    :return: random 6-vector that a0 * u = s and b0 * u = t
    '''

    a0 = list2vec([one, one, 0, one, 0, one])
    b0 = list2vec([one, one, 0, 0, 0, one])

    while True:
        u=list2vec([randGF2() for each in range(6)])
        if a0 * u == s and b0 * u == t:
            break;

    return u

# 8.7.2
def choose_rest():

    count=0

    a=[]
    b=[]

    while count != 6:
        # initialize for every loop
        count=0

        # Making 4 for each, a1,b1, a2,b2, a3,b3, a4,b4
        a=[list2vec([randGF2() for each in range(6)]) for i in range(4)]
        b=[list2vec([randGF2() for each in range(6)]) for i in range(4)]

        # Check whether independent for chosen 3 pairs of 6-vectors.
        # If below for-loop ends with count=6, it satisfies requirement.
                                   # nCr , n=4, r=3
        for each in itertools.combinations('0123',3):
            three_pairs=[]

            for idx in each:
                three_pairs.append(a[int(idx)])
                three_pairs.append(b[int(idx)])

            count+=1

            # rank == 6 means vectors in 'three_pairs' are linear-independent
            # Even if one case doesn't satisfy requirement, starts over for-loop
            if rank(three_pairs) != 6:
                break

        # If while-loop reach here with count == 6,
        # requirement is met

    for each in a:
        print(each)
    for each in b:
        print(each)

    return a,b