import sys
sys.path.append("D:\Python\Matrix")

from Solutions import *
import random
from QR import *

# 9.4.1
A,b=read_training_data('train.data')

# print(A)
# print(b)

# 9.4.3
# w=Vec(A.D[1],{each: 1 for each in A.D[1]})
# u=Vec(A.D[1],{each:-1 for each in A.D[1]})
w=Vec(A.D[1],{each:1 if random.randrange(2)==1 else -1 for each in A.D[1]}) # random-w

# print(w)
# print(fraction_wrong(A,b,w))
# print(loss(A,b,w))
#
# print(fraction_wrong(A,b,u))
# print(loss(A,b,u))

# 9.4.9
# print(find_grad(A,b,w))
# print(find_grad(A,b,u))

# 9.4.10
# original w
# print(w)
step_one=2E-9
step_two=1E-9
# next w
# print(gradient_descent_step(A,b,w,step))

# 9.4.11, 12
# w=Vec(A.D[1],{each: 1 for each in A.D[1]})    # 1-w
w=Vec(A.D[1],{each: 0 for each in A.D[1]})      # 0-w, most accurate
# print(gradient_descent(A,b,w,step_two,270))

# 9.4.13
# final_w=gradient_descent(A,b,w,step_two,270)
# test_A,test_b=read_training_data('validate.data')
#
# print(fraction_wrong(test_A,test_b,final_w))
# print(loss(test_A,test_b,final_w))

x=QR_solve(A,b)
print(x)
print(A*x)

print(fraction_wrong(A,b,x))
print(loss(A,b,x))