from propositional_logic import *

A = BoolVar('A')
B = BoolVar('B')
C = BoolVar('C')

# write code using A, B, and C, along with 
# the classes from propositional_logic.py
# and the .format() mathod to output the
# following expression:

f1 = Implies(A, B)
f2 = Implies(B, C)
f3 = Implies (A, C)
f4 = And(f1, f2)
f5 = Implies(f4, f3)
print(f5)
print(f5.format())
print()
# (((A => B) & (B => C)) => (A => C))
