from .util import *
from .classes import *
from cmd import Cmd
    
problems = []
probStat = []

def list_prob(p, ps):
    print_c(p.name)

def det_prob(i):
    p = problems[i]
    ps = probStat[i]
    print_head("Problem Details", 'red')
    print_color("Name", p.name)
    if p.contestId:
        print_color("Contest ID", p.contestId)
    if p.index:
        print_color("Index", p.index)
    if p.points:
        print_color("Points", p.points)
    if p.rating:
        print_color("Rating", p.rating)
    print_color("Solved By", ps.solvedCount)


class Prompt(Cmd):
    idx = 0
    jdx = 0
    prompt = 'cf> '
    def do_list(self, num):
        num = int(num)
        num = min(num, 15)
        while self.idx<len(problems) and num>0:
            print_c(str(self.idx)+":", 'cyan', end=' ')
            list_prob(problems[self.idx], probStat[self.idx])
            self.idx = self.idx+1
            num = num-1
    def help_list(self):
        print_c("\nLists 'n' number of problems, Max 15 at a time\n", 'red')

    def do_reset(self, num):
        if num:
            self.idx = int(num)
            self.jdx = int(num)
        else:
            self.idx=0
            self.jdx=0
    def help_reset(self):
        print_c("\nResets starting variable to 0 or specified argument\n", 'red')

    def do_prob(self, num):
        num = int(num)
        det_prob(num)
    def help_prob(self):
        print_c("\nLists information about the problem\n", 'red')

    def do_listn(self, name):
        l = len(problems)
        for i in range(l):
            if problems[i].name==name:
                self.do_prob(i)
    def help_listn(self):
        print_c("\nLists the problem specified by name\n", 'red')

    def do_listi(self, index):
        l = len(problems)
        num = 10
        while self.jdx<l and num>0:
            if index in problems[self.jdx].index:
                print_c(str(self.jdx)+":", 'cyan', end=' ')
                list_prob(problems[self.jdx], probStat[self.jdx])
                num = num-1
            self.jdx = self.jdx+1
    def help_listi(self):
        print_c("\nLists 10 problems specified by index\n",'red')

    def do_listc(self, cont):
        cont = int(cont)
        l = len(problems)
        i = 0
        while i<l:
            if cont == problems[i].contestId:
                print_c(str(i)+":", 'cyan', end=' ')
                list_prob(problems[i], probStat[i])
            i = i+1
    def help_listc(self):
        print_c("\nLists problems specified by contestId\n", 'red')
        
    def do_exit(self, inp):
        return True
    def help_exit(self):
        print_c("\nExits the terminal\n",'red')

    def default(self, inp):
        if inp=='q':
            return self.do_exit(inp)
        elif inp=='l':
            self.do_list(10)
    
    
def p_main(res):
    
    l = len(res['result']['problems'])

    for i in range(l):
        problems.append(Problem(res['result']['problems'][i]))
        probStat.append(ProblemStatistics(res['result']['problemStatistics'][i]))

    Prompt().cmdloop()

    
