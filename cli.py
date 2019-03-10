import argparse
from commands.user_info import *
from commands.user_rating import *
from commands.contest_list import *
from commands.problems import *
from commands.blog import *
from commands.ratingchange import *
from commands.bloguser import *
from commands.userstatus import *
import requests
import json

def get_req(url):
    return requests.get(url)

def get_parser():
    parser = argparse.ArgumentParser(description="Codeforces CLI")

    # Add parameters
    parser.add_argument('-u','--user', help="Handle of user")
    parser.add_argument('-g','--graph', help="Provides rating chart of user");
    parser.add_argument('-c','--contest',type=int,help="id of contest to display");
    parser.add_argument('--gym', action='store_true', help="Optional argument to list gym contests");
    parser.add_argument('-p','--problem', action='store_true', help="Retrieve all problems");
    parser.add_argument('--tag', help="Tag of problems to retrieve");
    parser.add_argument('-b','--blog',help="View the blog entry specified by id")
    parser.add_argument('-rc', '--ratingchange', help="Get Rating change of contest id")
    parser.add_argument('--handle', help="Specify handle for rating change")
    parser.add_argument('-bu','--bloguser',help="Get blog entries of user")
    parser.add_argument('-us','--userstatus', help="Get submissions of specified user")
    parser.add_argument('--fr', help="1-based index of the first submission to return")
    parser.add_argument('--count', help="Number of returned submissions")
    
    # return parser
    return parser

def main():
    parser = get_parser()

    # Get Arguments
    args = parser.parse_args()

    user = args.user
    graph = args.graph
    contest = args.contest
    gym = args.gym
    problem = args.problem
    tag = args.tag
    blogid = args.blog
    cid = args.ratingchange
    handle = args.handle
    bloguser_ = args.bloguser
    user_status = args.userstatus
    from_ = args.fr
    count = args.count
    
    if user:
        res = get_req("http://codeforces.com/api/user.info?handles={0}".format(user))
        user_info(json.loads(res.text))
    elif graph:
        res = get_req("http://codeforces.com/api/user.rating?handle={0}".format(graph))
        user_rating(json.loads(res.text))
    elif contest:
        if gym:
            res = get_req("http://codeforces.com/api/contest.list?gym=true");
        else:
            res = get_req("http://codeforces.com/api/contest.list");
        contest_list(json.loads(res.text), contest)
    elif problem:
        if tag:
            res = get_req("https://codeforces.com/api/problemset.problems?tags={}".format(tag))
        else:
            res = get_req("https://codeforces.com/api/problemset.problems")
        p_main(json.loads(res.text))
    elif blogid:
        res = get_req("https://codeforces.com/api/blogEntry.view?blogEntryId={}".format(blogid))
        comm = get_req("https://codeforces.com/api/blogEntry.comments?blogEntryId={}".format(blogid))
        blog(json.loads(res.text), json.loads(comm.text))
    elif cid:
        res = get_req("https://codeforces.com/api/contest.ratingChanges?contestId={}".format(cid))
        if handle:
            rath(json.loads(res.text), handle)
        else:
            ratc(json.loads(res.text))
    elif bloguser_:
        res = get_req("https://codeforces.com/api/user.blogEntries?handle={}".format(bloguser_))
        bloguser(json.loads(res.text))
    elif user_status:
        if not from_ and not count:
            res = get_req("https://codeforces.com/api/user.status?handle={}".format(user_status))
        else:
            if not from_:
                from_ = 1
            if not count:
                count = 10
            res = get_req("https://codeforces.com/api/user.status?handle={}&from={}&count={}".format(user_status, from_, count))
        userstatus(json.loads(res.text))

main()
