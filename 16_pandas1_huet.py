import pandas as pd
import numpy as np

print("cau 1")
a = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(a)

print("cau 2")
c = {'a': 13,'b':10,'c':16,'d':22,'e':32,'f':66}
d = pd.Series(c, index = ['a','b','c','d','e','f'])
print(d)

print("cau 3")
e = pd.Series(a, index = ["a1","b2","c3","d1","e2","a3","g1","a2","i3","j1"])
print(e)

print("cau 4")
print(d[4])

print("cau 5")
print(c["a"], c["b"], c["c"])

print("cau 6")
print(e[[name.startswith("a") or name.endswith("1") for name in e.index]])


print("cau 7")
a.index.name = "cot 1"
a.name = "cot 2"
print(a)

print("cau 8")
x = np.log(e)
print(x)

print("cau 9")
print(a[1:15])




