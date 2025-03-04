x_int = 1
x_double = 3.0
x_complex = 1 + 3j
# 用于大数字提高可读性
x_speed = 10_000_000_000
# 科学计数法
x_pow = 28.9e+12
x_ascii = 0x3f
x_bit = 0b1011_1001
print(x_speed)
# //才相当于java的/
x_a = 3 / 2
x_b = 3 // 2
print(x_b)

print(str(x_b))
result = " ".join(["how", "are", "you"])
print(result)

port = 0b1011_1111
bitmask = 0b0010_0000
xxx = port & (bitmask >> 1)
print(f"bin:{xxx:08b}")
