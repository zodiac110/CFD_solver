from Packages import *
import Finite_difference as FD

size = 11
accuracy = 4
bc_type = ['one-sided','one-sided']

A = np.linspace(0,size-1,size)
B = FD.FORMULA_GEN(size,accuracy,1,bc_type)
print(B,"\n")
c,d = FD.MD_GEN(B,bc_type)
print(c,"\n")
print(d)