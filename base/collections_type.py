names = ["zs", "ls", "ww"]
names.append("sss")
print(names[-1])
del names[0]
names.insert(0, "zs")
names.remove("ww")
print(names)

# tuple元组不可变
ages = (12, "zs")
x, y = ages
print(x, y)

grades = {
    "math": 50,
    "english": 100
}
grades["art"] = 30
print(grades.keys())
print(grades.values())
grades2 = dict(yuwen=3, tiyu=100)
print(grades)

a = {1, 2, 3}
b = {4, 5, 6}
print(a|b)
print(a&b)
print(a-b)
