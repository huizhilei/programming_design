from data_process import Data
from my_crt import Crt
from normal_solution import Nst
import os

dir = 'src_data'


def main():
    equation = []

    if not os.path.exists(dir):
        os.mkdir(dir)
        os.chdir(dir)
        num = int(input("请输入一共有多少个同余方程："))
        with open('da ta.txt', 'w') as f:
            for i in range(num):
                equation.append(input("请输入第%d个方程：" % i) + "\n")
                f.write(equation[i])
    else:
        print("目录已存在")
        os.chdir(dir)

    data = Data('./data.txt')
    if data.solution_judge():
        print("该同余式组有解")
        if data.crt_judge():
            print("该同余式组可以用中国剩余定理")
            print("解为: x=%d(mod %d)" % Crt(data).crt_compute())
        else:
            print("该同余式组不可以用中国剩余定理，以一般方法求解")
            print("解为: x=%d(mod %d)" % Nst(data).nst_compute())
    else:
        print("该同余式组无解")
        return False


if __name__ == '__main__':
    main()

