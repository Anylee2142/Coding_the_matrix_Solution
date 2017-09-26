# import matplotlib.pyplot as plt
import sys
sys.path.append("D:\Python\Matrix")
from plotting import plot
from vec import Vec

# plt.ylim(-8,8)
# plt.xlim(-8,8)

L=[[2,2],[3,2],[1.75,1],[2,1]]

#3,3,2
#
# plot(L,4)

#3.4.2
# def move(L): return [L[0]+1,L[1]+2]

#3,4,3
def add2(List,trsprt): return [[each[0]+trsprt[0],each[1]+trsprt[1]] for each in List]
plot(add2(L,[1,2]),4)

#3.4.4
# def addn(L1,L2): return [val+L2[idx] for (idx,val) in enumerate(L1)]

#3.4.6
# plt.arrow(0,0,-2,4,color='red')
# plt.arrow(1,1,-2,4,color='blue')
# plt.show()

#3.4.7
# plt.arrow(0,0,-2,4,color='red')
# plt.arrow(-2,4,1,2,color='blue')
# plt.arrow(0,0,-2+1,4+2,color='yellow')
# plt.show()

#3.5.3
def scalar_vector_mult(alpha,v): return [alpha*scalar for scalar in v]

#3.5.4
# plot([[0.5*x,0.5*y] for [x,y] in L],4)
# plot([[-0.5*x,-0.5*y] for [x,y] in L],4)

#80page
# line=[scalar_vector_mult(i/100,[3,2]) for i in range(101)]
#
# translation_line=add2(line,[0.5,1])
#
# plot(translation_line,4)

#3.6.1
# w = [3,4], vector = [2,3]

#3.6.2
# { a*[5,-1] + [1,4] | a(R and 0<=a<=1}
# plt.arrow(1,4,5,-1)
# plt.arrow(0,0,5,-1)
# plt.show()

#3.6.9
# convex combination = a*v + b*u
# def segment(pt1,pt2): return [[i/100*pt1[0]+(1-i/100)*pt2[0],i/100*pt1[1]+(1-i/100)*pt2[1]] for i in range(101)]
#
# plot(segment([3.5,3],[0.5,1]),4)

#--------------------------------------------------------

# v : String -> Real Number
# v=Vec({'A','B','C'},{'A':1})
# u=Vec(v.D,{'A':5,'C':10})
# setitem(v,'B',2)
# setitem(v,'C',3)
# v = 1,2,3
# u = 5,0,10

# print(scalar_mul(v,3).f)
#
# for d in v.D:
#     if d in v.f:
#         print(v.f[d])
#
# print(getitem(v,'B'))
# print(getitem(v,'C'))
#
# print(add(u,zero_vec(v.D)).f)
# print(neg(add(v,u)).f)

# 3.9.3 == Dot product
def list_dot(u,v): return sum([a*b for (a,b) in zip(u,v)])
#
# print(list_dot([getitem(u,each) for each in u.D],[getitem(v,each) for each in v.D]))

# 3.9.7
# D={'memory','radio','sensor','CPU'}
# rate=Vec(D,{'memory':0.06,'radio':0.1,'sensor':0.004,'CPU':0.0025})
# duration=Vec(D,{'memory':1.0,'radio':0.2,'sensor':0.5,'CPU':1.0})
# print(list_dot(rate.f.values(),duration.f.values()))

# 3.9.13
# long_seg=[1,-1,1,1,1,-1,1,1,1]
# small_seg=[1,-1,1,1,-1,1]

# for each in range(len(long_seg)-len(small_seg)+1):
#     print(list_dot(long_seg[each:len(small_seg)+each],small_seg))

# 3.9.15
# def dot_product_list(needle,haystack):
#     return [list_dot(haystack[each:len(needle)+each],needle) for each in range(len(haystack)-len(needle)+1)]

# print(dot_product_list(small_seg,long_seg))

# 3.10.1
# def list2vec(L): return Vec(set(range(len(L))),{i:L[i] for i in range(len(L))})

# 3.11.4
# Backward substitution with Upper triangular system
# to get root of Linear equation ( a*x = b )

# def triangular_solve_n(a,b):
#     D=len(b)
#     x=[0 for each in range(len(b))]
#     for i in reversed(range(D)):
#         rest=[a[i][D-(idx+1)]*x[D-(idx+1)] for idx in range(D-(i+1))]
#         x[i]=(b[i] - sum(rest))/a[i][i]
#     return x
#
# a=[[2,3,-4],[0,1,2],[0,0,5]]
# b=[10,3,15]
#
# c=[[1,-3,-2],[0,2,4],[0,0,-10]]
# d=[7,4,12]
#
# print(triangular_solve_n(a,b))
# print(triangular_solve_n(c,d))

v = Vec({'a','b','c', 'd'},{'a':2,'c':1,'d':3})
u = Vec({'a','b','c', 'd'},{'c':1,'d':3})

print(v+u)
print(v*u)

print(10*v)
print(-u)