'''
L=[list2vec(v) for v in [[8,-2,2],[0,3,3],[1,0,0],[0,1,0],[0,0,1]]]
vstarlist,sigma=aug_orthogonalize(L)
coldicts={idx:val for idx,val in enumerate(sigma)}
U=coldict2mat(coldicts)
print(U)
print(vstarlist[2])
print(L[2] - (1/9)*vstarlist[0])
'''


''' b on A if A*x == b else approximation
x that residual = || A*x - b || is minimum.

D={'metal','concrete','plastic','water','electricity'}
v_gnome=Vec(D,{'concrete':1.3,'plastic':.2,'water':.8,'electricity':.4})
v_hoop=Vec(D,{'plastic':1.5,'water':.4,'electricity':.3})
v_slinky=Vec(D,{'metal':.25,'water':.2,'electricity':.7})
v_putty=Vec(D,{'plastic':.3,'water':.7,'electricity':.5})
v_shooter=Vec(D,{'metal':.15,'plastic':.5,'water':.4,'electricity':.8})

rowdict={'gnome':v_gnome,'hoop':v_hoop,'slinky':v_slinky,'putty':v_putty,'shooter':v_shooter}
M=rowdict2mat(rowdict)

b=Vec(D,{'water':1485,'concrete':1300,'plastic':677,'metal':226.25,'electricity':1409.5})
x=solve(transpose(M),b)
# print(x)
# print(x*M)
# print(b)

b_=Vec(D,{'water':1000,'concrete':1331.62,'plastic':679.32,'metal':223.23,'electricity':1492.64})
x_=solve(transpose(M),b_)
# print(x_)
# print(x_*M)
# print(b_)

D={'radio','sensor','memory','CPU'}
b=list2vec([140,170,60,170])
d1=Vec(D,{'radio':0.1,'CPU':0.3})
d2=Vec(D,{'sensor':0.2,'CPU':0.4})
d3=Vec(D,{'memory':0.3, 'CPU':0.1})
d4=Vec(D,{'memory':0.5, 'CPU':0.4})
d5=Vec(D,{'radio':0.2,'CPU':0.5})
d6=Vec(D,{'sensor':0.3, 'radio':0.8, 'CPU':0.9, 'memory':0.8})
d7=Vec(D,{'sensor':0.5, 'radio':0.3, 'CPU':0.9, 'memory':0.5})
d8=Vec(D,{'radio':0.2, 'CPU':0.6})

rowdicts={0:d1, 1:d2, 2:d3, 3:d4}
A=rowdict2mat(rowdicts)
x=solve(A,b)
# print(x)
# print(A*x)
# print(b)

b_=list2vec([141.27, 160.59, 62.47, 181.25])
x_=solve(A,b_)
# print(x_)
# print(A*x_)
# print(b)

rowdicts={0:d1, 1:d2,2:d3,3:d4,4:d5,5:d6,6:d7,7:d8}
A=rowdict2mat(rowdicts)
b=list2vec([141.27, 160.59, 62.47, 181.25, 247.74, 804.58, 609.10, 282.09])
x=solve(A,b)

# print(x)
# print(A*x)
# print(b)
'''