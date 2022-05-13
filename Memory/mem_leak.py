import sys
import numpy as np
import weakref


if __name__ == '__main__':
    data = np.array([1])
    print(weakref.getweakrefcount(data))
    ref1 = weakref.ref(data)
    print(weakref.getweakrefcount(data))
    print(sys.getrefcount(ref1))
    ref2 = weakref.ref(data)
    print(weakref.getweakrefcount(data))
    print(sys.getrefcount(ref1))
    ref3 = weakref.ref(data)
    print(weakref.getweakrefcount(data))
    print(sys.getrefcount(ref1))
    print(sys.getrefcount(ref2))
    print(sys.getrefcount(ref3))
    print(ref1 is ref2)
    print(ref2 is ref3)

    pro1 = weakref.proxy(data)
    print(weakref.getweakrefcount(data))
    pro2 = weakref.proxy(data)
    print(weakref.getweakrefcount(data))
    print(pro1 is pro2)

    print(weakref.getweakrefs(data))
    pass