import sys
sys.path.append("D:\Python\Matrix")

from vec import Vec
from GF2 import one
from factoring_support import *
from echelon import *
from math import sqrt

from matutil import *
from independence import *

# 8.8.1
def root_method(N):
    count=1

    root_n=intsqrt(N)

    while True:
        a = root_n+count

        b=intsqrt(a**2 - N)

        if sqrt(a**2 - N) == b:
            return (a+b,a-b)

        # If below-condition is met,
        # There is no integer factor A, B
        if a>=N:
            print('No A, B exists')
            return

        count+=1

# 8.8.5
def int2GF2(i): return 0 if i%2==0 else one

# 8.8.6
def make_Vec(primeset,factors): return Vec(primeset,{key:int2GF2(val) for key,val in factors })

# 8.8.7
def find_candidates(N, primeset):
    count=2
    root_n=intsqrt(N)

    roots=[]
    rowlist=[]

    while len(roots) <= len(primeset):
        x = root_n + count

        # If x*x - N is divided by N in prime-set,
        if dumb_factor(x**2 - N, primeset) != []:
            roots.append(x)
            rowlist.append(make_Vec(primeset,dumb_factor(x**2-N,primeset)))

        count+=1

    return roots,rowlist

# 8.8.10
def find_a_and_b(v, roots, N):
    # v from M,
    # Chosen roots from v are perfect square
    # Because of this, b exists so does a
    alist=[roots[k] for k in v.f.keys() if v.f[k]==one]

    a=prod(alist)

    blist=[x**2-N for x in alist]

    b=intsqrt(prod(blist))

    return a,b

# 8.8.11
def find_factors(N,primelist):
    roots,rowlist = find_candidates(N,primelist)

    M_rows = transformation_rows(rowlist,sorted(primelist,reverse=True))

    for i,row in enumerate(M_rows):
        # Backward search 11, 10, 9, ..., 1, 0
        idx = len(M_rows)-(1+i)

        # When M * A = U,
        # Basically, we should not execute M's rows whose U's row is not 0
        # But every N can be factorized
        # So before reaching M's rows whose U's row is not 0, solution will be found.
        a,b = find_a_and_b(M_rows[idx],roots,N)

        # When GCD is 1, it means there's no common factor between (a,b) and N
        # So these a,b are failure. Start over.
        if gcd(a-b,N) != 1:
            print(gcd(a-b,N))
            return a,b