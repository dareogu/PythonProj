# -*- coding: utf-8 -*-

'''
@Time    : 2025/10/5 11:05
@Author  : Dareo Gu
@FileName: test_class.py
@Software: PyCharm

在定义 Python 类时，通常使用的定义方法包括：

1.__init__()：构造方法，用于初始化实例。
2.实例方法：普通的方法，用于操作实例属性或执行类的功能。
3.类方法：使用 @classmethod 装饰器，作用于类而非实例。
4.静态方法：使用 @staticmethod 装饰器，不依赖实例或类。
5.__str__() 和 __repr__()：分别用于定义打印和调试时的对象表示。
6.__del__()：析构方法，在对象销毁时调用。
7.@property：将方法变为属性，通常用于动态计算或封装类属性。
'''


class Person:
    population = 0  # 类属性

    # 构造方法
    def __init__(self, name, age):
        self._name = name
        self._age = age
        Person.population += 1

    # 打印对象时调用
    def __str__(self):
        return f'{self.name} {self.age} years old'

    # 定义小于比较，__lt__ 方法定义了两个 Person 对象之间的比较规则。在这个例子中，我们通过比较他们的 age 属性来决定哪个对象更小
    # 我们可以进一步使用 __lt__() 来自定义排序行为，我们希望根据年龄进行排序
    def __lt__(self, other):
        if isinstance(other, Person):  # 确保比较的是同类型的对象
            return self.age < other.age
        else:
            raise TypeError(
                f"Cannot compare with different type: {type(other)}")  # 如果其他对象不是 Person 类型，返回 NotImplemented

    # __del__() 是类的析构方法，当程序结束对象被销毁时，__del__() 会被自动调用
    # 如果只是简单的输出一些信息，不会有太大问题。但如果涉及复杂的资源管理，最好使用 __enter__ 和 __exit__ 方法来进行清理，或者通过 weakref 来管理引用
    def __del__(self):
        print(f'{self.name} is deleted')

    # 实例方法
    def introduce(self):
        print(f'{self.name} is {self.age} years old.')

    @classmethod  # 类方法
    def person_count(cls):
        print(f'current population is {cls.population}.')

    @staticmethod
    def static_method(name, age):
        print(f'static method: {name} is {age} years old.')

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def weight(self):
        return self._age * 3 - 1

    # 你可以通过 @property 结合 @setter，控制如何设置和获取某个属性。这对于验证输入、计算返回值或封装逻辑非常有用
    @weight.setter
    def weight(self, value):
        self._age = (value + 1) / 3


person1 = Person("Selina", 39)
print(person1.name)
print(person1.age)
person1.introduce()

person2 = Person("Fiona", 38)
person2.introduce()

print(person2 < person1)  # True

person3 = Person("Daisy", 28)
person3.weight = 80
print(person3.age)
person4 = Person("Yoyo", 42)
print(person4.weight)

persons = [person1, person2, person3, person4]
print("*****before sorting*****")
print(*persons, sep='\n')

persons.sort()
print("*****after sorting*****")
for person in persons:  # 等同于 print(*persons, sep='\n')
    print(person)

Person.person_count()

Person.static_method('Fiona', 88)
print("********Finally*********")
