d = {'name': 'jason', 'age': 20}
print(d.get('name'))
print(d.get('location'))

print(10/4)
print(10//4)

pi = 3.14159
# 格式化
print(f"pi:{pi:.2f}")

filename = "test.text"
# r :read w: write w+:r&w
with open(filename, "w") as f:
    f.write("hello\n")
    f.write("yjl\n")
with open(filename, "r") as f:
    for line in f.read().splitlines():
        print(line)
