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