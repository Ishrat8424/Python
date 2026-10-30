class Demo:
    @classmethod
    def eating(cls):
        cls.a = 110

Demo.eating()
print(Demo.a)