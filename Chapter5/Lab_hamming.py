import sys
sys.path.append("D:\Python\Matrix")
from mat import Mat
from matutil import *
from vec import Vec
from GF2 import one
from bitutil import *

# 5.14.1
lists=[[one,0,one,one],[one,one,0,one],[0,0,0,one],[one,one,one,0],[0,0,one,0],[0,one,0,0],[one,0,0,0]]

G=listlist2mat(lists)

lists=[[0,0,0,one,one,one,one],[0,one,one,0,0,one,one],[one,0,one,0,one,0,one]]

H=listlist2mat(lists)

# inverse matrix of G
lists=[[0,0,0,0,0,0,one],[0,0,0,0,0,one,0],[0,0,0,0,one,0,0],[0,0,one,0,0,0,0]]

R=listlist2mat(lists)

# [1, 0, 0, 1] = 4-Vector on GF(2) Field
p=Vec(set(range(4)),{0:one,1:0,2:0,3:one})

# print(H)

# 0 0 1 1 0 0 1
c=Vec(set(range(7)),{0:0,1:0,2:one,3:one,4:0,5:0,6:one})

# print(H*G)

tmp=G*p

# print(H*tmp)


# 5.14.4
# error syndrome returned is 3-Vector
# and error is at most 1
def find_error(err_syn):
    for (key,vector) in mat2coldict(H).items():
        if err_syn.f == vector.f:
            return Vec(set(H.D[1]),{key:one})

    return Vec(set(H.D[1]),{})

def find_error_matrix(S):
    return coldict2mat({key:find_error(vector) for (key,vector) in mat2coldict(S).items()})


# delivered_cipher=Vec(set(range(7)),{0:one,1:0,2:one,3:one,4:0,5:one,6:one})
# print(find_error(H*delivered_cipher))

# err_syn=listlist2mat([[one,0],[one,0],[one,one]])
# print(find_error_matrix(err_syn))

# 5.14.6
# print(str2bits('a'))
# print(str2bits('b'))
# print(str2bits('c'))
# print(bits2str(str2bits('B')))
# As result shows, Intel CPU is little-endian

# 5.14.7
# P=bits2mat(str2bits('a'))
# print(P)

# 5.14.8
str_neo="I'm trying to free your mind, Neo. But i can only show you the door. You're the one that has to walk through it"
P=bits2mat(str2bits(str_neo))
# print(P)

# 5.14.9
# this is codeword
P=bits2mat(str2bits(str_neo))
# print(mat2bits(P))

# this is error
e=noise(P,0.05)
# print(mat2bits(e))

# this is codeword + error
# print(mat2bits(P+e))

# this is noised string
# print(bits2str(mat2bits(P+e)))

# 5.14.10
C=G*P
# print(bits2str(mat2bits(P)))
# print(bits2str(mat2bits(G*P)))

# 5.14.11
# 7 x ?
# CTILDE=C+G*noise(P,0.05)
e=noise(G*P,0.02)
CTILDE=C+e

print(bits2str(mat2bits(R*CTILDE)))

# 5.4.12
# def correct(A):

# 3 * ?
err_syn=H*CTILDE

print(CTILDE)
print(err_syn)

err_set=find_error_matrix(err_syn)

c=CTILDE-err_set

# corrected codeword to text
print(bits2str(mat2bits(R*c)))