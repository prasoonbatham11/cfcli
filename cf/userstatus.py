from cf.util import *
from cf.classes import *
from prettytable import PrettyTable as PT
import pydoc

def userstatus(res):
    res = res['result']
    s = []
    for r in res:
        s.append(Submission(r))
    pt = PT()
    fn = ["Problem ID", "Problem Name", "Points","Language", "Verdict", "TestSet", "Passed Tests", "Time(ms)", "Memory(bytes)"]
    for i in range(len(fn)):
        fn[i] = get_colored(fn[i], 'magenta')
    pt.field_names = fn
    for i in s:
        pid = str(i.problem.contestId)+str(i.problem.index)
        pname = i.problem.name
        points = str(i.problem.points)
        lang = i.programmingLanguage
        verd = i.verdict
        ts = i.testset
        ptest = str(i.passedTestCount)
        time = str(i.timeConsumedMillis)
        mem = str(i.memoryConsumedBytes)
        lis = [pid,pname,points,lang,verd,ts,ptest,time,mem]
        for j in range(len(lis)):
            lis[j] = get_colored(lis[j], 'cyan')
        pt.add_row(lis)
    pydoc.pager(pt.get_string())
