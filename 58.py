# converting dictionaries to series

from pandas import Series

salary = {'John':3000, 'Tim':4500, 'Rob':5600}

print(salary)

se = Series(salary)
print(se)