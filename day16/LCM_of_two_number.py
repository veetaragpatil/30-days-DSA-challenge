import math
def lcm(n, m):
    return n // math.gcd(n, m) * m  
print(lcm(4, 6))
