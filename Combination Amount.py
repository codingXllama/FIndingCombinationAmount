import math

n = int(input("Enter size: "))
r = int(input("Enter number of choice: "))
ncr = math.factorial(n) / (math.factorial(r) * (math.factorial(n - r)))
print(ncr)

