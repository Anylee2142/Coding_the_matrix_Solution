from Solutions import *

D={'a','b','c','d'}
a0=Vec(D,{'a':1})
a1=Vec(D,{'b':1})
a2=Vec(D,{'c':1})
a3=Vec(D,{'a':1,'c':3})

A=[a0,a1,a2]
L=[a0,a1,a2,a3]
u=Vec(set(range(len(A))),{0:2,1:4,2:6})

sample_A=[ list2vec([1,0,2,0]),list2vec([1,2,5,1]),list2vec([1,5,-1,3]) ]

# 6.14.13
# print(rep2vec(u,A))

# print(rep2vec(list2vec([5,3,-2]),sample_A))

# 6.14.14
# print(vec2rep(A,Vec(D,{'a':3,'c':-2})))

# print(vec2rep(sample_A ,list2vec([6,-4,27,-3]) ))

# 6.14.15
# print(is_superfluous(L,3))
# print(is_superfluous(L,0))
# print(is_superfluous(L,1))

# ------------------------------------------
# If there is no script for specific problem,
# find it at definition of function of doctest
# ------------------------------------------
