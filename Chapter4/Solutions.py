import sys
sys.path.append("D:\Python\Matrix")

from vec import Vec
from GF2 import one
from itertools import product

D=set(range(3))
lists=[Vec(D,{0:1,1:5,2:3}),
       Vec(D,{0:2,1:10,2:3}),
       Vec(D,{0:2,1:11,2:23})]

# 4.2.13
# def standard(D,one): return [Vec(D,{k:one}) for k in D]

# 4.8.1.1
def vec_select(veclist,k): return [Vec(v.D,{key:0 if key==k else v[key]  for key in v.D}) for v in veclist]

# 4.8.1.2
def vec_sum(veclist,D): return Vec(D,{k:sum([v[k] for v in veclist])for k in D})

# 4.8.1.3
def vec_select_sum(D,veclist,k): return vec_select([vec_sum(veclist,D)],k)

# 4.8.2
def scale_vecs(vecdict): return [(1/k)*Vec(v.D,v.f) if k in v.D else Vec(v.D,v.f) for k,v in vecdict.item()]

# 4.8.3
def GF2_span(L): return [sum([a*v if a*v else [0 for each in range(len(L[0]))] for (a,v) in zip(i,L)]) for i in product([0,one],repeat=len(L))]