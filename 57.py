# print in series

from pandas import Series
se = Series([1, 3, 5, 7, 9])
print(se)


print(se[2])


se2 = Series([100, 200, 300], index=['a', 'b', 'c'])
print(se2)

print(se2['b'])
