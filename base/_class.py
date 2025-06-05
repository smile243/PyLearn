# 不支持构造函数、方法的重载的
class Passenger(object):
    # 属性可以动态创建，这里first_name,last_name都没有
    # 方法的第一个参数一般起名叫self
    def __init__(self, first_name:str, last_name:str):
        self.first_name = first_name
        self.last_name = last_name
        self.info = {
            'country':'Pakistan',
            'number':12345812
        }

    def display(self):
        print(f"Passenger: {self.first_name} {self.last_name}")

    @staticmethod
    # 静态方法省略self,不会使用class的properties
    def from_input():
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        return Passenger(first_name, last_name)
    # 允许其实例使用 []（索引器）运算符
    def __getitem__(self,i):
        return self.info[i]
if __name__ == "__main__":
    lisa = Passenger("Lisa", "Ha")
    user = Passenger.from_input()
    lisa.display()
    user.display()
    print(lisa['number'])
