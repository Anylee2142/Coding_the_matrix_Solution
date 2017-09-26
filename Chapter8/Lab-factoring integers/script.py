from Solutions import *

# 8.8.1
# list=[55,77,146771,118]

# for each in list:
#     print(root_method(each))

# 8.8.2
# r=100
# s=120
# t=10
#
# a,b = r*s, s*t
#
# print(gcd(a,b))

# 8.8.3
# N=367160330145890434494322103
# a=67469780066325164
# b=9429601150488992
#
# print(gcd(a-b,N))
# print(gcd(a+b,N))

# 8.8.4
# print(dumb_factor(75,{2,3,5,7}))

primeset=primes(13)
# x=[12,154,2*3*3*3*11*11*13,2*17,2*3*5*7*19]
#
# for each in x:
#     print(dumb_factor(each,primeset))

# 8.8.5
# print(int2GF2(3))
# print(int2GF2(4))

# 8.8.6
# print(make_Vec(primeset,dumb_factor(3,primeset)))
# print(make_Vec(primeset,dumb_factor(2**17*5*11**3,primeset)))

# 8.8.7
primeset=primes(32)
N=2419
roots,rowlist=find_candidates(N, primeset)

# 8.8.8
# a=53*77
# b=2*3**2*5*13
# print(gcd(a-b,N))
#
# a=52*67*71
# b=2*3**2*5*19*23
# print(gcd(a-b,N))

# M_rows=transformation_rows(rowlist,sorted(primeset,reverse=True))
M_rows=transformation_rows(rowlist,sorted(primeset,reverse=True))

M=rowdict2mat({idx:val for idx,val in enumerate(M_rows) })

A=rowdict2mat({ idx:val for idx,val in enumerate(rowlist) })

for each in M_rows:
    print(each)

print(M)

# print(A)

# M*A = U
print(M*A)

# for k,v in M_rows[11].f.items():
#     print(k, v)

# len(rowlist) = rank A + nullity A

# 8.8.10
# a,b=find_a_and_b(M_rows[10],roots,N)
# print(find_factors(2419,primes(32)))
# print(gcd(a-b,N))

# 8.8.11
N=2461799993978700679
primelist=primes(10000)

# a,b=find_factors(N,primelist)
# print(a)
# print(b)