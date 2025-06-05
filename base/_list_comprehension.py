# 列表推导式
# variable = [out_exp for out_exp in input_list if out_exp == 2]
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
v=" zs ,ls,ww"
# i.strip()去除空格
list = [i.strip() for i in v.split(",")]
print(list)
raise ValueError(v)