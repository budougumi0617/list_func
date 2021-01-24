from list_func.process import process


def test_process():
    src = '''
class TestClass:
    x = "変数1"

    def test_method1(self):
        print(self.x)

    def test_method2(self, arg1):
        print("引数1:" + arg1)
        
def func1(arg1):
        print("引数1:" + arg1)
    '''

    assert process(src) == [
        'TestClass.test_method1',
        'TestClass.test_method2',
        'func1'
    ]
