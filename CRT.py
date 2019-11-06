import re
from invserse_solution import getInv


class Crt(object):
    def __init__(self, path):
        self.path = path
        self.re_exp = re.compile(r'([a-zA-Z]\d?)=(\d)\(mod(\d)\)')
        with open(path, 'rb') as f:
            self.f_list = f.readlines()
        self.num_equation = len(self.f_list)
        self.remainder = []
        self.mod = []
        self.solution_unknown = []
        self.M = 1
        self.Mi = []
        self.Ti = []
        self.solution = 0

    def crt_compute(self):

        def data_extract():
            for equation in self.f_list:
                self.remainder.append(self.re_exp.search(equation).group(2))
                self.mod.append(self.re_exp.search(equation).group(3))
                self.solution_unknown.append(self.re_exp.search(equation).group(1))

                self.remainder = [int(r) for r in self.remainder]
                self.mod = [int(mm) for mm in self.mod]

        def data_check():
            for solution_un in self.solution_unknown:
                if len(solution_un) != 1:
                    print("这不是一次同余式组")
                    return 0

        def inverse_element():
            for i in self.remainder:
                self.Ti[i] = getInv(self.Mi[i], self.mod[i])

        data_extract()
        data_check()
        inverse_element()

        for m in self.mod:
            self.M *= m
        for i in range(self.num_equation):
            self.Mi[i] = self.M / self.mod[i]
            self.solution += self.remainder[i]*self.Mi[i]*self.Ti[i]
        with open(self.path, 'w') as f:
            f.write("使用中国剩余定理，答案为"+str(self.solution))
        return self.solution




