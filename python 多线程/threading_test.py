#
# 多线程运行 全局变量收集线程运行结果
#
import threading


def num_adder(num, res):
    res[0] += num


if __name__ == '__main__':
    threading_list = list()
    result = [0]
    for num in range(100):
        t = threading.Thread(target=num_adder, args=(num+1, result, ))
        threading_list.append(t)
        t.start()

    for t in threading_list:
        t.join()

    print(f"{result}")
    pass
