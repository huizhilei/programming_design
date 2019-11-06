import re
from format_check import FormatError
import os


class Data(object):
    @staticmethod
    def gcd(a, b):
        if a < b:
            a, b = b, a
        if a % b == 0:
            return b
        return Data.gcd(b, a % b)

    def __init__(self, path):
        self.path = path
        self.re_exp = re.compile(r'([a-zA-Z]\d?)=(\d+)\(mod(\d+)\)')
        with open(path, 'r') as f:
            os.chdir('../src_data')
            self.f_list = f.readlines()
        self.num_equation = len(self.f_list)
        self.remainder = []
        self.mod = []
        self.solution_unknown = []

        for equation in self.f_list:
            self.remainder.append(self.re_exp.search(equation).group(2))
            self.mod.append(self.re_exp.search(equation).group(3))
            self.solution_unknown.append(self.re_exp.search(equation).group(1))
            self.remainder = [int(r) for r in self.remainder]
            self.mod = [int(mm) for mm in self.mod]

        for solution_un in self.solution_unknown:
            try:
                if len(solution_un) != 1:
                    raise FormatError("该同余式组含有高次项")
            except FormatError as e:
                print(e)
        print(self.path)
        print(self.remainder)
        print(self.mod)

    def solution_judge(self):
        flag = 1

        for i in range(self.num_equation):
            for j in range(self.num_equation):
                if (self.remainder[i] - self.remainder[j]) % Data.gcd(self.mod[i], self.mod[j]) != 0:
                    flag = 0
        print("此处为检查点 gcd_flag:%d" % flag)
        return flag

    def crt_judge(self):
        flag = 1
        for i in self.mod:
            for j in self.mod:

                if i != j and Data.gcd(i, j) != 1:
                    flag = 0
        return flag




































