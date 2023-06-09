import math
# num = "01011101"
num = '01110000'
exp = num[1:4]
sign = num[0:1]
men = num[4:]
# print(sign, type(sign))
# print(int(sign) + 1, type(sign))


a = 0
for index, y in enumerate(reversed(exp)):
    a = a +  int(y)*(2**index)

m = 0
for index, y in enumerate(men):
    m = m +  int(y)*(2**(-(index+1)))

print(a)
print(1+m, type(m))
print(type(a))
val = math.nan
print(val)
# print(val)
