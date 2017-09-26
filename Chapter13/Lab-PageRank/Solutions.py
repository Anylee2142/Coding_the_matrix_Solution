import sys
sys.path.append("D:\Python\Matrix")

from GF2 import one

from math import *
from vecutil import *
from matutil import *
from pagerank import *

#test case
D = set(range(1,7))
f = [(1,1),(1,4),(2,3),(2,4),(2,5),(2,6),(3,2),(4,5),(5,6),(6,5)]
small_links = Mat((D, D), {x:1 for x in f})
A2= Mat(small_links.D, {(r, c):1/6 for r in small_links.D[0] for c in small_links.D[1]})

#normalize(ra)
#pra = power_method(ra,d,250)

# 13.12.1
def find_num_links(L):
    # If L is really large, variable like 'col_vecs' can be calculated once and use it as parameter

    print('num_links started')

    num_links=Vec(L.D[1],{c:sum(L[r,c] for r in L.D[0]) for c in L.D[1]})

    print('num_links done')

    return num_links

# 13.12.2
def make_Markov(L):
   num_links=find_num_links(L)

   print('Markov started')

   for r in L.D[0]:
       for c in L.D[1]:
           L[r,c]=L[r,c]/num_links[c]

   print(len(L.D[0]))
   print('Markov done')
   return L

# 13.12.3
def power_method(L,t):

    x=Vec(L.D[1],{d:1 for d in L.D[1]})

    print('power method started')

    for iter in range(t):
        print(iter)
        x = L * x

    print('power method done')

    return x

# 13.12.5
def wikigoogle(w,k,p):
    print('wikigoogle started')

    related=find_word(w)
    related.sort(key=lambda x:p[x], reverse=True)

    print('wikigoogle done')
    return related[:k]