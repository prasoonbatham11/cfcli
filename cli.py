import argparse
from commands.user_info import *
from commands.user_rating import *
from commands.contest_list import *
import requests
proxies = {"http": "http://edcguest:edcguest@172.31.102.29:3128",
           "https": "http://edcguest:edcguest@172.31.102.29:3128"}

import json

def get_req(url):
    return requests.get(url, proxies=proxies)

def get_parser():
    parser = argparse.ArgumentParser(description="Codeforces CLI")

    # Add parameters
    parser.add_argument('-u','--user', help="Handle of user")
    parser.add_argument('-g','--graph', help="Provides rating chart of user");
    parser.add_argument('-c','--contest',type=int,help="id of contest to display");
    parser.add_argument('--gym', action='store_true', help="Optional argument to list gym contests");
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

main()
