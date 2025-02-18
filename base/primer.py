# 1:代替{}
# 2没有;
# 3
list = [1, 2, 3]
minimum = list[0]
for n in list:
    if n < minimum:
        minimum = n
        print("min num is:", minimum)
