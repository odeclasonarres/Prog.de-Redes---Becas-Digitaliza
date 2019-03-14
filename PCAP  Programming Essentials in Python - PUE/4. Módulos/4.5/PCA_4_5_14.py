import math
x = float(input())
assert x>=0.0
x = math.sqrt(x)
print(x)





""" VERSIÓN CORREGIDA CON try-except:
import math
x = float(input())

try:
    assert x>=0.0
    x = math.sqrt(x)
    print(x)
except AssertionError:
    print("No puedes calcular la raíz")
"""
