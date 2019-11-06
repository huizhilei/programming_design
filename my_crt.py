from invserse_solution import getInv


class Crt(object):
    def __init__(self, congruence):
        self.num_equation = congruence.num_equation
        self.remainder = congruence.remainder
        self.mod = congruence.mod
        self.solution_unknown = congruence.solution_unknown
        self.M = 1
        self.mm = 1
        self.Mi = []
        self.Ti = []
        self.solution = 0

    def crt_compute(self):

        def data_check():
            for solution_un in self.solution_unknown:
                if len(solution_un) != 1:
                    print("这不是一次同余式组")
                    return 0

        def inverse_element():
            for ii in range(self.num_equation):
                self.Ti.append(getInv(self.Mi[ii], self.mod[ii]))

        for m in self.mod:
            self.M *= m
        for i in range(self.num_equation):
            self.Mi.append(int(self.M / self.mod[i]))

        data_check()
        inverse_element()
        for i in range(self.num_equation):
            self.solution += self.remainder[i]*self.Mi[i]*self.Ti[i]
        self.solution %= self.M
        print("&&&&&&&&&&&&&&&&&&&&&&")
        print(self.num_equation)
        print(self.remainder)
        print(self.Mi)
        print(self.Ti)
        print("&&&&&&&&&&&&&&&&&&&&&&")
        self.solution %= self.M
        return self.solution, self.M
