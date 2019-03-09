from .util import *
from .classes import *
import pydoc
import time

def blog(res):
    b = BlogEntry(res['result'])
    title = get_mark(b.title)
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
    pydoc.pager(blog_)
    
