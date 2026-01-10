class A:
    
    _instance = None

    _num = 0
    _num += 1

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            
        return cls._instance
    
    def __init__(self, a):
        self.a = a

if __name__ == '__main__':

    a = A(8)
    b = A(9)

    assert a == b
    assert a.a == 9
    assert a.a == b.a

    print(a.a)

    print(b._num)

print('Default data loading'.upper())