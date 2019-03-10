from datetime import datetime
import numpy as np
import subprocess
from colorama import Fore, Back, Style
import html2text as ht
import mdv

def get_mark(html):
    return mdv.main(ht.html2text(html))

def get_colored(val, color='white'):
    c = ""
    if color is 'green':
        c = Fore.GREEN
    elif color is 'cyan':
        c = Fore.CYAN
    elif color is 'red':
        c = Fore.RED
    elif color is 'magenta':
        c = Fore.MAGENTA
    elif color is 'blue':
        c = Fore.BLUE
    return c+val+Style.RESET_ALL

def print_c(val, color='green', end='\n'):
    c = ""
    if color is 'green':
        c = Fore.GREEN
    elif color is 'cyan':
        c = Fore.CYAN
    elif color is 'red':
        c = Fore.RED
    elif color is 'magenta':
        c = Fore.MAGENTA
    elif color is 'blue':
        c = Fore.BLUE
    print(c+val+Style.RESET_ALL, end=end)

def print_color(key, attr, color='cyan'):
    c = Fore.CYAN
    attr = str(attr)
    if color is 'cyan':
        c = Fore.CYAN
    elif color is 'red':
        c = Fore.RED
    elif color is 'blue':
        c = Fore.BLUE
    elif color is 'magenta':
        c = Fore.MAGENTA
    print("\t|"+c+'{:15s} {:5s}'.format(key, ":")+Style.RESET_ALL+'{:10s}'.format(attr));

def print_head(key, color='cyan'):
    c = Fore.CYAN
    if color is 'cyan':
        c = Fore.CYAN
    elif color is 'red':
        c = Fore.RED
    elif color is 'blue':
        c = Fore.BLUE
    elif color is 'magenta':
        c = Fore.MAGENTA
    print(c+"\t|"+key+"\n"+Style.RESET_ALL);


def plotterm(x,y):
    x=np.array(x)
    y=np.array(y)
    gnuplot = subprocess.Popen(["/usr/bin/gnuplot"], stdin=subprocess.PIPE)
    gnuplot.stdin.write(bytes("set term dumb 100 30\n", "utf-8"))
    gnuplot.stdin.write(bytes("set xdata time;\n", "utf-8"))
    gnuplot.stdin.write(bytes("set timefmt \"%d%m%Y\"\n", "utf-8"))
    gnuplot.stdin.write(bytes("plot '-' using 1:2 with lines notitle \n", "utf-8"))
    for i,j in zip(x,y):
        gnuplot.stdin.write(bytes("%s %f\n" % (i,j), "utf-8"))
    gnuplot.stdin.write(bytes("exit\n", "utf-8"))
    gnuplot.stdin.flush()
    gnuplot.stdin.close()

def seconds_to_hrs(time):
    if time>0:
        return "FINISHED"
    else:
        time = -time
        days = time//86400
        time = time%86400
        hrs = time//3600
        time = time%3600
        min = time//60
        time = time%60
        sec = time
        ans = ""
        if days>0:
            ans += str(days)+" days "
        if hrs>0:
            ans += str(hrs)+" hours "
        if min>0:
            ans += str(min)+" minutes "
        if sec>0:
            ans += str(sec)+" seconds "
        return ans

def seconds_to_ago(time):
    days = time//86400
    year = days//365
    days = days%365
    time = time%86400
    hrs = time//3600
    time = time%3600
    min = time//60
    time = time%60
    sec = time
    ans = ""
    if year>0:
        ans+=str(year)+" year(s) "
    if days>0:
        ans += str(days)+" days "
    elif hrs>0:
        ans += str(hrs)+" hours "
    elif min>0:
        ans += str(min)+" minutes "
    elif sec>0:
        ans += str(sec)+" seconds "
    return ans
    
def format_date(time):
    a = datetime.fromtimestamp(time).strftime("%B %d, %Y %H:%M:%S")
    return a
