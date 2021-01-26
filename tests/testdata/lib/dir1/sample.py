class TestClass:
    x = "変数1"

    def test_method1(self):
        print(self.x)

    @property
    def test_method2(self):
        return 'property'


def func1(arg1):
    print("引数1:" + arg1)