from cf.util import *
from cf.classes import *
import pydoc
from cmd import Cmd
import requests
import json
from cf.blog import *

bu = []

def get_req(url):
    return requests.get(url)

def print_ind(idx):
    com = get_colored(str(idx)+": "+str(bu[idx].id)+" ", 'cyan')
    com += get_mark(bu[idx].title).strip()
    print(com)

def view_blog(blogid):
    res = get_req("https://codeforces.com/api/blogEntry.view?blogEntryId={}".format(blogid))
    comm = get_req("https://codeforces.com/api/blogEntry.comments?blogEntryId={}".format(blogid))
    blog(json.loads(res.text), json.loads(comm.text))

class Prompt(Cmd):
    prompt = 'cf> '
    idx = 0
    def do_list(self, num):
        num = int(num)
        num = min(num, 15)
        while self.idx<len(bu) and num>0:
            print_ind(self.idx)
            self.idx += 1
            num -= 1
    def help_list(self):
        print_c("\nPrints 'n' number of blog entries at a time\n", 'red')

    def do_viewi(self, idx):
        view_blog(bu[int(idx)].id)
    def help_viewi(seld):
        print_c("\nView ith blog\n", 'red')

    def do_vidx(self, idx):
        view_blog(int(idx))
    def help_vidx(self):
        print_c("\nView blog with id i\n", 'red')
    
    def do_reset(self, num):
        if num:
            self.idx = int(num)
        else:
            self.idx=0
    def help_reset(self):
        print_c("\nResets starting variable to 0 or specified argument\n", 'red')

    def do_exit(self, inp):
        return True
    def help_exit(self):
        print_c("\nExits the terminal\n",'red')

    def default(self, inp):
        if inp=='q':
            return self.do_exit(inp)
        elif inp=='l':
            self.do_list(10)

def bloguser(res):
    res = res['result']
    for r in res:
        bu.append(BlogEntry(r))
    Prompt().cmdloop()
