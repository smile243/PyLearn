nums = [1, 3, 5, 6, 2]
# a[start:stop:step]
# a[start:stop]
# a[start:]
# a[:stop]
# a[:]
print(nums[3:6])
print(nums[::2])

names = ["Lisa", "John", "Susan", "Alex"]

for i, name in enumerate(names):
    print(i, name)

prices = [12.3, 5.2, 8.7, 1.2, 8.0]
gross = [price * 1.2 for price in prices if price > 8]


def reassign(_list):
    _list = [0, 1]


def append(_list):
    _list.append(1)


test_list = [0]
reassign(test_list)
print(test_list)
append(test_list)
print(test_list)
