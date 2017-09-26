import sys
sys.path.append("D:\Python\Matrix")

from orthonormalization import *
from QR import *
from read_data import *

# 10.11.9
L=[list2vec(v) for v in [[4,3,1,2],[8,9,-5,-5],[10,1,-1,5]]]
result=orthonormalize(L)
# for each in result:
#     print(each)
#     print(each*each)

# 10.11.10
L=[list2vec(v) for v in [[4,3,1,2],[8,9,-5,-5],[10,1,-1,5]]]

Qlist,Rlist=aug_orthonormalize(L)

# print(coldict2mat(Qlist)*coldict2mat(Rlist))

# 10.11.11
# 1.
V=[list2vec(v) for v in [[6,2,3],[6,0,3]]]
Qlist,Rlist=aug_orthonormalize(V)
# print(coldict2mat(V))
# print(coldict2mat(Qlist)*coldict2mat(Rlist))

# 2.
V=[list2vec(v) for v in [[2,2,1],[3,1,1]]]
Qlist,Rlist=aug_orthonormalize(V)
# print(coldict2mat(V))
# print(coldict2mat(Qlist)*coldict2mat(Rlist))

# 10.11.12
A=Mat(({'a','b','c'},{'A','B'}),
      {('a','A'):-1,('a','B'):2,('b','A'):5,('b','B'):3,('c','A'):1,('c','B'):-2})
b=Vec({'a','b','c'},{'a':1,'b':-1})
Q,R=factor(A)

x=QR_solve(A,b)
# print(b-A*x)
# print((b-A*x)*A)

A=listlist2mat([[1,0],[1,0],[0,1]])
# print(A)
b=list2vec([1,1,1])

x=QR_solve(A,b)
# print(x)

Q,R=factor(A)
# print(Q)
# print(R)
# print(Q*R)

# 10.11.13
# 1.
A=listlist2mat([[8,1],[6,2],[0,6]])
b=list2vec([10,8,6])
x=QR_solve(A,b)
Q,R=factor(A)
residual=(b-A*x)
norm=sqrt(residual*residual)
# print(x)
# print(A*x) # close approximation to b
# print((residual*A)*(residual*A))
# print(norm)

# 2.
A=listlist2mat([[3,1],[4,1],[5,1]])
b=list2vec([10,13,15])
x=QR_solve(A,b)
Q,R=factor(A)
residual=(b-A*x)
norm=sqrt(residual*residual)
# print(x)
# print(A*x) # close approximation to b
# print((residual*A)*(residual*A))
# print(norm)

# 10.11.14
# 1.
A=listlist2mat([[8,1],[6,1],[0,6]])
b=list2vec([10,8,6])
x=QR_solve(A,b)
# print(x)
# print(A*x)
# print(b)

# 2.
A=listlist2mat([[3,1],[4,1]])
b=list2vec([10,13])
Q,R=factor(A)
x=QR_solve(A,b)
# print(x)
# print(A*x)
# print(b)
# print(Q)
# print(R)

# 10.11.15
vlist=read_vectors('age-height.txt')

Arows=[Vec({'a','c'},{'a':1, 'c':each['age']})  for each in vlist]
A=rowdict2mat(Arows)

b=list2vec([each['height'] for each in vlist])

x=QR_solve(A,b)
print(A)
print(b)
print(x)