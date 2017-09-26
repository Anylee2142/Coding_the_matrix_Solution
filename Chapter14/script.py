from Solutions import *

# A=listlist2mat([[2,10],[2,1],[8,1],[0,1],[1,0]])
# b=list2vec([5,1,2,0,0])
#
# R_square={2,4}
#
# find_vertex(A,b,R_square)
#
# c=list2vec([1,1.7])
#
# A=listlist2mat([[2,10],[8,1]])
# b=list2vec([5,2])
# x1=solve(A,b)
#
# A=listlist2mat([[2,10],[2,1]])
# b=list2vec([5,1])
# x2=solve(A,b)
#
# A=listlist2mat([[2,1],[8,1]])
# b=list2vec([1,2])
# x3=solve(A,b)
#
# y=solve(A,c)
# print(x1)
# print(x2)
# print(x3)

A=listlist2mat([[1,1,0],[0,1,1],[1,0,1]])
x=list2vec([2,4,6])
w=find_move_direction(A,x,2)
# print(A*x)
# print(A*(x+w))

w,sigma=find_move(A,x,2)
print(w,sigma)