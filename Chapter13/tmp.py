import sys
sys.path.append("D:\Python\Matrix")

from GF2 import one

from math import *
from vecutil import *
from matutil import *

#test case
D = set(range(1,7))
f = [(1,1),(1,4),(2,3),(2,4),(2,5),(2,6),(3,2),(4,5),(5,6),(6,5)]
small_links = Mat((D, D), {x:1 for x in f})
A2= Mat(small_links.D, {(r, c):1/6 for r in small_links.D[0] for c in small_links.D[1]})

#normalize(ra)
#pra = power_method(ra,d,250)

print(A2)