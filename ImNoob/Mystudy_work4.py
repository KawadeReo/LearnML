#class超基本

class person:
    def __init__(self,name,age):
        self.name =name
        self.age =age

    def introduce (self):
        print(f'私の名前は{self.name}です。年齢{self.age}歳です')


ppn = person(name="ふわちゃん",age=28)

ppn.introduce()

ppn = person(name="宮本",age=22)

ppn.introduce()

