import os

from list_func.process import process, walk


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


def test_walk():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    my_data_path = os.path.join(current_dir, 'testdata')

    assert walk(my_data_path) == [
        'lib.dir2.foo_bar:FooClass.test_method1',
        'lib.dir2.foo_bar:FooClass.test_method2',
        'lib.dir2.foo_bar:BarClass.test_method1',
        'lib.dir2.foo_bar:BarClass.test_method2',
        'lib.dir1.sample:TestClass.test_method1',
        'lib.dir1.sample:TestClass.test_method2',
        'lib.dir1.sample:func1',
    ]
