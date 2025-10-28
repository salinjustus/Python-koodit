import numpy as np
#1
a = 2.493
b = 0.911

print(np.degrees(a))
print(np.degrees(b))

print("")
#2
a=137.7
b=62.3
print(np.radians(a))
print(np.radians(b))

print("")
#3
A = np.array([30,45,60,90,120,135,150,180,270,360])
for i in A:
  print(np.radians(i))