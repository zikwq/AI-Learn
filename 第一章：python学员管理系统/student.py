class Student(object):
    def __init__(self, name, gender, tel):
        # 包含姓名、性别、手机号
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name}, {self.gender}, {self.tel}'

# 测试代码
# aa = Student('aa','aa',11)
# print(aa)