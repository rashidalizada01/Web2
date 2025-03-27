# ordering
# inmutable
# duplicate
# tup = (12,345)
# l = [12,34,23]
# print(type(l))
# l = tuple(l)
# print(type(l))
tup = (1, None, 'Tuple')
l = list(tup)
print(l)
l.append('New value')
tup = tuple(l)
print(tup)
