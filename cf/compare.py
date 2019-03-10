from cf.util import *
from cf.classes import *
import os

def compare(res):
    res = res['result']
    u1 = User(res[0])
    u2 = User(res[1])
    f = open('compare_prof.dat', mode='w')
    f.write("@ "+u1.handle+","+u2.handle+"\n")
    f.write("Rating,"+str(u1.rating)+","+str(u2.rating)+"\n")
    f.write("Max Rating,"+str(u1.maxRating)+","+str(u2.maxRating)+"\n")
    f.close()

    os.system('termgraph compare_prof.dat --color blue red')
    os.system('rm compare_prof.dat')
    
