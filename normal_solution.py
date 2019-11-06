from prime_decomposition import prime_Decomposition
from data_process import Data
from my_crt import Crt


class Nst(object):
    def __init__(self, congruence):
        self.num_equation = congruence.num_equation
        self.remainder = congruence.remainder
        self.mod = congruence.mod
        self.solution = 0

        self.remainder2 = []
        self.base2 = []
        self.exponent = []
        self.num_equation2 = 0

        self.remainder3 = []
        self.base3 = []
        self.exponent3 = []
        self.num_equation3 = 0

    def nst_compute(self):
        for i in range(self.num_equation):
            a, b = prime_Decomposition(self.mod[i])
            self.base2.extend(a)
            self.exponent.extend(b)
            for j in range(len(a)):
                self.remainder2.append(self.remainder[i])
                self.num_equation2 += 1
        # print("********************")
        # print(self.base2)
        # print(self.exponent)
        # print(self.num_equation)
        # print(self.num_equation2)
        # print("********************")
        for i in range(self.num_equation2):
            for j in range(i+1, self.num_equation2):
                if self.base2[i] == self.base2[j]:
                    flag = int(self.exponent[i] > self.exponent[j])
                    c = [self.exponent[j], self.exponent[i]][self.exponent[j] > self.exponent[i]]
                    b = [self.exponent[i], self.exponent[j]][self.exponent[j] > self.exponent[i]]
                    if abs(self.remainder2[i] - self.remainder2[j]) % pow(self.base2[i], c) == 0:
                        if flag:
                            self.remainder3.append(self.remainder2[i])
                        else:
                            self.remainder3.append(self.remainder2[j])
                        self.base3.append(self.base2[i])
                        self.exponent3.append(b)
                        self.num_equation3 += 1
                    else:
                        print("矛盾，该同余式组无解")

        for index, value in enumerate(self.base2):
            if self.base2.count(value) == 1:
                self.remainder3.append(self.remainder2[index])
                self.base3.append(self.base2[index])
                self.exponent3.append(self.exponent[index])
                self.num_equation3 += 1

        # print("&&&&&&&&&&&&&&&&&&&&&&")
        # print(self.base3)
        # print(self.exponent3)
        # print(self.num_equation3)
        # print(self.remainder3)
        # print("&&&&&&&&&&&&&&&&&&&&&&")

        with open("transformed_data.txt", 'w') as f:
            for i in range(self.num_equation3):
                f.write("x=%d(mod%d)\n" % (self.remainder3[i], pow(self.base3[i], self.exponent3[i])))

        transformed_data = Data("./transformed_data.txt")
        if transformed_data.crt_judge():
            print("该同余式组可以用中国剩余定理")
            tcrt = Crt(transformed_data)
            return tcrt.crt_compute()
        else:
            print("以一般方法 递归 求解")
            return Nst(transformed_data).nst_compute()







