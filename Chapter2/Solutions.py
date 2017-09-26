import matplotlib.pyplot as plt
from plotting import plot
from math import e
from math import pi

s=[2+2j,3+2j,1.75+1j,2+1j,2.25+1j,2.5+1j,2.75+1j,3+1j,3.25+1j,-2+3j]

abs_lists=[abs(each) for each in s]

# plt.axhline(0,color='black')
# plt.axvline(0,color='black')
plt.ylim(-8,8)
plt.xlim(-8,8)

# plot(s,10)

# print(abs_lists)

# plt.plotting()
# plt.plot([each.real for each in s],[each.imag for each in s],'ro')
# plt.xlabel('real numbers')
# plt.ylabel('imag numbers')
# plt.show()

# 2.4.3
# trans_lists=[(1+2j)+each for each in s]
#
#
# plt.plot([reals.real for reals in trans_lists],[imags.imag for imags in trans_lists],'ro')
# plt.show()

#2.4.6
# pos=[0+0j,1+0j,-2+3j,-3+3j]
#
# starts=[0+0j,1+0j]
# ends=[-3+3j,-2+3j]
#
# #plt.plot([reals.real for reals in pos],[imags.imag for imags in pos],'ro')
#
# ax=plt.axes()
#
# plt.arrow(0,2,-3,3,color='red')
# plt.arrow(1,0,-3,3,color='blue')
# plt.xlim(-6,6)
# plt.ylim(-6,6)
#
# plt.axhline(0,color='black')
# plt.axvline(0,color='black')
#
# plt.show()

# 2.4.7
# trans_lists=[((1+2j)+each)/2 for each in s]
#
# x_pos=[-reals.real for reals in trans_lists]
# y_pos=[imags.imag for imags in trans_lists]
#
# # plt.plot(x_pos,y_pos,'ro')
# plt.plot(y_pos,x_pos,'ro')
#
# plt.axhline(0,color='black')
# plt.axvline(0,color='black')
# plt.xlim(-10,10)
# plt.ylim(-10,10)
#
# plt.show()

#2.4.8
# Rotated_scaled=[((each*((0+1j)**3))/2) for each in s]
#
# plt.plot([each.real for each in Rotated_scaled],[each.imag for each in Rotated_scaled],'ro')
#
# plt.show()

#2.4.9
# Rotated_scaled=[((each*((0+1j)**3))/2)+(2-1j) for each in s]
#
# plt.plot([each.real for each in Rotated_scaled],[each.imag for each in Rotated_scaled],'ro')
#
# plt.show()

#2.4.10
# from image import *
#
# data=color2gray(file2image('img01.png'))
#
# pts=list()
#
# vrt_cnt=int(len(data))
# hrz_cnt=({len(each) for each in data}.pop())
#
#
# for (first,each_line) in enumerate(data):
#     for (second,datum) in enumerate(each_line):
#         if datum<=120:
#             pts.append(second+(vrt_cnt-first)*1j)
#
#
# plot(pts,vrt_cnt)
#
# def totheOrigin(pos):
#     return [(each.real-hrz_cnt/2) + (each.imag-vrt_cnt/2)*1j for each in pos]
#
# plot(totheOrigin(pts),len(data))

#2.4.17
#
# n=10
#
# cmplx=e**(2j*pi/n)
#
# w=[cmplx**each for each in range(n)]
#
# for each in w:
#     print(each)
#
# plot(w,3)

#2.4.18
# trans_s=[z*e**((pi*1j)/4) for z in s]

# plot(trans_s,5)
#-------------------------------------------------------
#2.4.19, 2.4.20
# from image import *
#
# # 'img01.png' = 189 X 166
# data=color2gray(file2image('img01.png'))
#
# pts=list()
#
# vrt_cnt=int(len(data))
# hrz_cnt=({len(each) for each in data}.pop())
#
# amid_real=0
# amid_imag=0
#
# for (first,each_line) in enumerate(data):
#     for (second,datum) in enumerate(each_line):
#         buf=(second+(vrt_cnt-first)*1j)*e**((pi*1j)/4)
#         if datum<=120:
#             pts.append(buf)
#         if first==int(vrt_cnt/2) and second==int(hrz_cnt/2):
#             amid_real, amid_imag = buf.real, buf.imag
#
# print(amid_real,amid_imag)
#
# #2.4.19
# plot(pts,vrt_cnt)
#
# def totheOrigin(pos):
#     return [(each.real-amid_real)+(each.imag-amid_imag)*1j for each in pos]
#
# #2.4.20
# plot([each/2 for each in totheOrigin(pts)],len(data))
#-------------------------------------------------------
# 1 quadrants, 2 quadrants
# from image import *
#
# data=color2gray(file2image('img01.png'))
#
# pts=list()
#
# vrt_cnt=int(len(data))
# hrz_cnt=({len(each) for each in data}.pop())
#
#
# amid_real=0
# amid_imag=0
#
# for (first,each_line) in enumerate(data):
#     for (second,datum) in enumerate(each_line):
#         buf=(second+(vrt_cnt-first)*1j)
#         if datum<=120:
#             pts.append(buf)
#         if first==int(vrt_cnt/2) and second==int(hrz_cnt/2):
#             amid_real, amid_imag = buf.real, buf.imag
#
# pts1=[each.real-2*amid_real + each.imag*1j for each in pts]
#
# plot(pts,vrt_cnt)
#
# plot(pts1,vrt_cnt)
#-------------------------------------------------------
# Prob 2.5.1 , 60p
# '''
# As problem states, 5-digit key is used 11 times
# and because it has small space, we can exhaustive-search.
# We'll get 'plain' via 'key' XOR 'cipher' using cartesian product
# (note that below code's cartesian product starts from 'key' to 'cipher')
# '''
#
# cipher=['10101','00100','10101','01011','11001','00011','01011','10101','00100','11001','11010']
#
# # making 5-digit-binary keys, from 0 to 26 in base 10
# key=["{0:0>5}".format(str(bin(each))[2:]) for each in range(27)]
#
# # every 5-digit-key is applied to each cipher
# for each in key:
#     plain=[]
#     # and this is it (= 'key' X 'cipher')
#     for every in cipher:
#         block=str()
#         for i in range(5):
#             # getting plain text via 'key' XOR 'cipher'
#             XOR_result=str((int(each[i])+int(every[i]))%2)
#             block=block.__add__(XOR_result)
#         # 'plain' will have same count as much as 'cipher' do
#         plain.append(block)
#
#     # exhaustive-searching via printing each in 'plain'
#     for each in plain:
#         print_chr=int(each,2)%27+65
#         print(chr(print_chr),end='')
#     print('\n')

# #2.7.1
# def my_filter(L,num): return [each for each in L if each%num!=0]
#
# #2.7.2
# def my_lists(L): return [L[0:idx+1] for idx in range(len(L)) if 0 not in L[0:idx+1]]
#
# #2.7.3
# def my_function_composition(f,g): return {k1:v2 for (k1,v1) in f.items() for (k2,v2) in g.items() if v1 == k2}
#
# #2.7.4
# def mySum(L):
#     current=0
#     for each in L:
#         current+=each
#     return current
#
# #2.7.5
# def myProduct(L):
#     current=1
#     for each in L:
#         current*=each
#     return current
#
# #2.7.6
# def myMin(L):
#     current=L[0]
#     for each in L:
#         if current>=each:
#             current=each
#     return current
#
# #2.7.7
# def myConcat(L):
#     current=''
#     for each in L:
#         current+=each
#     return current
#
# #2.7.8
# def myUnion(L):
#     current=set()
#     for each in L:
#         current=current.union(each)
#     return current

# 2.7.9
'''
1. 0+x=x, 0

2. 1*x=x, 1

3. min(infinity,x)=x, infinity

4. S='', S.concat(x)=x, ''

5. S=set(), S.union(x)=x, {}

6. S.intersection(x)=x
Above means S should always include set x,
but x is argument which means what's in x differs from every execution of intersection()
so in this case, S is not initializable
'''

# 2.7.10
# first_cmplx=[3+1j,-1+2j,2+0j,4*(0+2j)]
# second_cmplx=[2+2j,1-1j,-3+0.001j,0.001+1j]
#
# for (idx,cmplx) in enumerate(first_cmplx):
#     final_real,final_imag=cmplx.real+second_cmplx[idx].real,cmplx.imag+second_cmplx[idx].imag
#     plt.arrow(0,0,cmplx.real,cmplx.imag,head_width=0.1, head_length=0.1,color='red')
#     plt.arrow(cmplx.real,cmplx.imag,second_cmplx[idx].real,second_cmplx[idx].imag,head_width=0.1, head_length=0.1,color='yellow')
#     plt.arrow(0,0,final_real,final_imag,head_width=0.1, head_length=0.1,color='blue')
# plt.show()

# 2.7.11
# print(e**1j * e**2j)
# print(e**3j)
#
# print(e**(pi/4*1j) * e**(pi*2/3*1j))
# print(e**(pi*11/12*1j))
#
# print(e**(-pi/4*1j) * e**(pi*2/3*1j))
# print(e**(pi*5/12*1j))

#-------------------------------------------------------------------------
# # 2.7.12
# def transform(a,b,L): return [a*z +b for z in L]
#
# # 2.7.12.a
# # 2*e**(-pi*1j/2)*( z+(1+1j) )
# # can be represented using
# # a = e**(-pi*1j/2)*2
# # b = (1+1j) * e**(-pi*1j/2)*2
# def transform_a(L): return [( z+(1+1j) ) * e**(-pi*1j/2)*2 for z in L]
#
#
# # 2.7.12.b
# # e**(pi*1j/4)*( 2*z.real + 3j*z.imag ) + (-3-2j)
# # can't be represented using any a,b
# # beacuse of separate multiplication for real and imaginary number
# def transform_b(L): return [e**(pi*1j/4)*( 2*z.real + 3j*z.imag ) + (-3-2j) for z in L]
#
# # 2.7.12 a,b Test
# from image import *
#
# # 'img01.png' = 189 X 166
# data=color2gray(file2image('img01.png'))
#
# pts=list()
#
# vrt_cnt=int(len(data))
# hrz_cnt=({len(each) for each in data}.pop())
#
# amid_real=0
# amid_imag=0
#
# for (first,each_line) in enumerate(data):
#     for (second,datum) in enumerate(each_line):
#         buf=(second+(vrt_cnt-first)*1j)
#         if datum<=120:
#             pts.append(buf)
#         if first==int(vrt_cnt/2) and second==int(hrz_cnt/2):
#             amid_real, amid_imag = buf.real, buf.imag
#
# print(amid_real,amid_imag)
#
# # move the image to center
# def totheOrigin(pos):
#     return [(each.real-amid_real)+(each.imag-amid_imag)*1j for each in pos]
#
# plot(pts,500)
# plot(transform_a(pts),500)
# plot(transform_b(pts),500)

#-------------------------------------------------------------------------

#2.7.13
# from GF2 import one
# print(one+one+one+0)
# print(one*one+0*one+0*0+one*one)
# print((one+one+one)*(one+one+one+one))

#2.7.14
# Let suppose we are c in the problem,
# then we know b1 and b1 XOR b2.
# By using b1, we can derive b2 from b1 XOR b2.
# so network links can avoid racing condition
# have reliability