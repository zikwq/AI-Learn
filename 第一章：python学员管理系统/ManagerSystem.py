from student import *


class StudentManager(object):
    def __init__(self):
        # 定义一个初始化的列表，用来存储将来的学院信息
        self.student_list = []

    # 一、 定义程序入口函数，启动程序后执行的功能
    def run(self):
        # 1. 加载学院信息
        self.load_student()

        while True:
            # 2. 显示功能菜单
            self.show_menu()

            # 3. 用户输入功能序号
            menu_num = int(input('请输入您需要的功能序号：'))

            # 4. 根据用户输入的不同序号执行不同功能
            if menu_num == 1:
                # 添加学员
                self.add_student()

            elif menu_num == 2:
                # 删除学员
                self.del_student()

            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()

            elif menu_num == 4:
                # 查询学员信息
                self.search_student()

            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()

            elif menu_num == 6:
                # 保存修改
                self.save_student()

            elif menu_num == 7:
                break

    # 二、 系统功能函数定义
    # 2.1 显示功能菜单
    @staticmethod
    def show_menu():
        print('+-------系统功能菜单显示--------+')
        print('|     1:添加学员|2:删除学员     |')
        print('|     3:修改学员|4:查询学员     |')
        print('|     5:显示所有|6:保存修改     |')
        print('+----------------------------+')

    # 2.2 添加学员
    def add_student(self):
        # 1、 用户输入姓名、性别、手机号
        name = input("请输入您的姓名：")
        genter = input("请输入您的性别：")
        tel = input("请输入您的手机号：")

        # 2、 创建学员对象
        student = Student(name, genter, tel)

        # 3、 将该对象添加到学员列表
        self.student_list.append(student)

        print(self.student_list)
        print(student)

    # 2.3 删除学员
    def del_student(self):
        # 1、 用户输入目标学员姓名
        del_name = input('请输入要删除学员的姓名：')

        # 2、 如果用户输入的目标学员存在则删除，否则提醒学员不存在
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                print("学员删除成功")
                break
        else:
            print("Error：用户不存在")

    # 2.4 修改学员信息
    def modify_student(self):
        # 1、 用户输入学员姓名
        modify_name = input('请输入要修改的学员姓名：')

        # 2、 如果用户输入姓名在列表中，则进行修改姓名，性别，手机号。否则则提示用户不存在
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('请输入学员姓名：')
                i.gender = input('请输入学员性别：')
                i.tel = input('请输入学员手机号：')
                print(f'学员修改成功, 姓名{i.name}, 性别{i.gender}, 手机号{i.tel}')
                break

        else:
            print('Error：用户不存在')

    # 2.5 查询学员信息
    def search_student(self):
        # 1、 用户输入目标姓名
        search_name = input('请输入学员姓名：')

        # 2、 在列表中寻找
        for i in self.student_list:
            if i.name == search_name:
                print(f'姓名：{i.name}, 性别:{i.gender}, 手机号:{i.tel}')
                break
        else:
            print("Error:用户不存在")


    # 2.6 显示所有学员信息
    def show_student(self):
        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    # 2.7 保存修改
    def save_student(self):
        # 打开文件
        f = open('student.data', 'w')

        # 文件写入学员信息，注意文件写入的数据不是学员内存地址，而是需要吧学员数据转换成字典
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)

        # 注意文件内数据要求为字符串类型，故需要先将数据类型转换
        f.write(str(new_list))

        # 关闭文件
        f.close()


    # 2.8 加载学员信息
    def load_student(self):
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 读取数据
            data = f.read()

            # 文件读取到的时字典数据，将其转换成列表文件
            new_list = eval(data)

            # 将列表转换为学员对象
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]

        finally:
            f.close()





