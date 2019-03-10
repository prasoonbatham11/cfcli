from cf.util import *
from cf.classes import *
from cmd import Cmd
import urllib
from bs4 import BeautifulSoup
import textwrap
import pydoc
    
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

def prob_stat(i):
    p = problems[i]
    url = "http://codeforces.com/problemset/problem/"+str(p.contestId)+"/"+str(p.index)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    pstate = soup.find('div', attrs={'class':'problem-statement'})
    header = pstate('div', attrs={'class':'header'})
    title = header[0]('div', attrs={'class':'title'})[0].get_text()
    time_limit = header[0]('div', attrs={'class':'time-limit'})[0].get_text()[19:]
    mem_limit = header[0]('div', attrs={'class':'memory-limit'})[0].get_text()[21:]
    
    statement = pstate('div')[10]('p')
    state = []
    for s in statement:
        state.append(s.get_text().replace('$$$', ''))
    
    input_spec = pstate('div', {'class':'input-specification'})[0]('p')
    input_s = []
    for s in input_spec:
        input_s.append(s.get_text().replace('$$$', ''))
    output_spec = pstate('div', {'class':'output-specification'})[0]('p')
    output_s = []
    for s in output_spec:
        output_s.append(s.get_text().replace('$$$', ''))

    sample_test = pstate('div', {'class':'sample-test'})[0]
    sample_test_i = sample_test('div', {'class':'input'})
    sample_test_o = sample_test('div', {'class':'output'})
    sti = []
    sto = []
    for s in sample_test_i:
        sti.append(s.get_text().replace('Input',''))
    for s in sample_test_o:
        sto.append(s.get_text().replace('Output',''))

    paged = get_colored("\t"+title, "blue")+"\n"
    paged += get_colored("\tTime: ",'blue')+get_colored(time_limit, color='magenta')+"\n"
    paged += get_colored("\tMemory: ",'blue')+get_colored(mem_limit, color='magenta')+"\n\n\n"

    paged += get_colored("\tProblem Statement:\n", 'blue')+"\n"
    for s in state:
        paged += get_colored("\t"+"\n\t".join(textwrap.wrap(s, 150))+"\n")+"\n"

    paged += get_colored("\tInput:\n", 'blue')+"\n"
    for s in input_s:
        paged += get_colored("\t"+"\n\t".join(textwrap.wrap(s, 150))+"\n")+"\n"

    paged += get_colored("\tOutput:\n", 'blue')+"\n"
    for s in output_s:
        paged += get_colored("\t"+"\n\t".join(textwrap.wrap(s, 150))+"\n")+"\n"

    for i in range(len(sti)):
        paged += get_colored("\tSample Input "+str(i)+":", 'blue')+"\n"
        paged += get_colored("\t "+sti[i].replace('\n', '\n\t '), 'cyan')+"\n"
        paged += get_colored("\tSample Output "+str(i)+":", 'blue')+"\n"
        paged += get_colored("\t "+sto[i].replace('\n', '\n\t '), 'green')+"\n"
    
    pydoc.pager(paged)
    
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

    def do_stat(self, idx):
        l = len(problems)
        for i in range(l):
            if idx==str(problems[i].contestId)+str(problems[i].index):
                prob_stat(i)
                break
    def help_stat(self):
        print_c("\nLists the problem statement specified by contestId+index eg. 1133A\n", 'red')

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

    
