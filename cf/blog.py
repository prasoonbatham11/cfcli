from cf.util import *
from cf.classes import *
import pydoc
import time
import textwrap

def blog(res, comm):
    b = BlogEntry(res['result'])
    root = Comment({'id':0,'parentCommentId':-1})
    c = []
    comm = comm['result']
    for i in range(len(comm)):
        c.append(Comment(comm[i]))
    
    title = get_mark(b.title).strip()
    auth = get_colored(b.authorHandle, 'blue')
    rating = get_colored(str(b.rating), 'blue')
    content = get_mark(b.content)
    curr = int(round(time.time()))
    created = get_colored(seconds_to_ago(curr-b.creationTimeSeconds), 'blue')
    modified = get_colored(seconds_to_ago(curr-b.modificationTimeSeconds), 'blue')
    
    blog_ = title+"\n"
    blog_ +=get_colored("By: ", 'magenta')+auth+"\n"
    blog_ +=get_colored("Rating: ",'magenta')+rating+"\n"
    blog_ +=get_colored("Created: ",'magenta')+created+get_colored(" ago\n",'blue')
    blog_ +=get_colored("Modified: ",'magenta')+modified+get_colored(" ago\n\n\n",'blue')
    blog_ += content
    
    for i in range(len(c)):
        c[i].creationTimeSeconds = seconds_to_ago(int(round(time.time()))-c[i].creationTimeSeconds)
        c[i].text = get_mark(c[i].text)
        
    c = [root]+c

    tree = []
    indx = []
    tree.append(root)
    indx.append(0)
    
    for i in range(1,len(c)):
        for j in range(len(tree)):
            if c[i].parentCommentId == tree[j].id:
                break
        tree.append(c[i])
        indx.append(indx[j]+1)
    
    comm_ = get_commthread(c, indx)
    
    final_blog = blog_+"\n\n\n"+comm_
    pydoc.pager(final_blog)

def get_commthread(c,indx):

    # Create comment thread
    th = [0]
    j = 0
    while j<len(th):
        k = th[j]
        y = j+1
        for l in range(len(c)):
            if c[k].id == c[l].parentCommentId:
                th.insert(y, l)
                y+=1
        j+=1
    
    comm_ = get_colored('COMMENTS:\n\n', 'magenta')
    tab_ = "\t"
    for i in range(1,len(th)):
        comm_ += tab_*indx[th[i]]
        comm_ += get_colored(c[th[i]].commentatorHandle, 'blue')+"\n"
        comm_ += tab_*indx[th[i]]
        comm_ += get_colored(c[th[i]].creationTimeSeconds+" ago", 'green')+"\n"
        comm_ += tab_*indx[th[i]]
        comm_ += ("\n"+tab_*indx[th[i]]).join(textwrap.wrap(c[th[i]].text, 150))+"\n\n"
    return comm_
