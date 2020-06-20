
class Test:
    var_of_class = 'Class Var'

    def __init__(self):
        self.var_of_instance = 'Instance Var'


def division_line_print(message):
    print('***************'+message+'***************')


if __name__ == '__main__':

    # 类对象与实例对象
    division_line_print('类对象与实例对象')
    # 类对象
    print(Test)
    # 实例对象
    class_instance = Test()
    print(class_instance)

    # 类变量
    division_line_print('类变量')
    # 类对象引用类变量
    print(f'类对象引用类变量 ：{Test.var_of_class}')
    class_instance_1 = Test()
    class_instance_2 = Test()
    # 实例对象引用类变量
    print(f'实例对象1引用类变量 ：{class_instance_1.var_of_class}')
    print(f'实例对象2引用类变量 ：{class_instance_2.var_of_class}')
    # 修改类变量实例对象共享修改
    Test.var_of_class = 'Changed Class Var'
    print(f'实例对象1引用类变量 ：{class_instance_1.var_of_class}')
    print(f'实例对象2引用类变量 ：{class_instance_2.var_of_class}')

    # 实例变量
    division_line_print('实例变量')
    # 实例变量
    class_instance_1 = Test()
    class_instance_2 = Test()

    print(f'实例对象1实例变量 ：{class_instance_1.var_of_instance}')
    print(f'实例对象2实例变量 ：{class_instance_2.var_of_instance}')
    class_instance_1.var_of_instance = 'changed instance var'

    print(f'修改实例对象1后实例对象1实例变量 ：{class_instance_1.var_of_instance}')
    print(f'修改实例对象1后实例对象2实例变量 ：{class_instance_2.var_of_instance}')

    # 类对象不能引用实例变量
    # print(Test.var_of_instance)

    # 属性绑定
    division_line_print('属性绑定')
    # 类属性
    # 定义时绑定类属性
    print(f'定义时绑定类属性：{Test.var_of_class}')
    # 运行时绑定类属性
    Test.var_of_class_defined_during_running = 'a long var of class'
    print(f'运行时绑定类属性：{Test.var_of_class_defined_during_running}')
    # 实例属性
    class_instance = Test()
    # 实例生成时绑定的实例属性
    print(f'实例生成时绑定的实例属性：{class_instance.var_of_instance}')
    # 实例运行时绑定的实例属性
    class_instance.var_of_instance = 'defined during running'
    print(f'实例运行时绑定的实例属性：{class_instance.var_of_instance}')

    # 属性引用
    division_line_print('属性引用')
    class_instance = Test()
    class_instance.var_of_class = 'instance var with a same name of a class var'
    print(f'类对象引用冲突属性：{Test.var_of_class}')
    print(f'实例对象引用冲突属性：{class_instance.var_of_class}')
