from cf.classes import *
from cf.util import *

def user_info(user):
    u1 = User(user['result'][0])
    print("\n")
    print_head("User Details", 'red')
    print_color("handle", u1.handle, 'cyan')
    if u1.email:
        print_color("Email", u1.email, 'cyan')
    if u1.firstName and u1.lastName:
        print_color("Name", u1.firstName+" "+u1.lastName, 'cyan')
    elif u1.firstName:
        print_color("Name", u1.firstName, 'cyan')
    elif u1.lastName:
        print_color("Name", u1.lastName, 'cyan')
    print_color("City", u1.city, 'cyan')
    print_color("Country", u1.country, 'cyan')
    print_color("Organization", u1.organization, 'cyan')
    print()
    print_head("Rating Statistics", 'red')
    print_color("Contribution", u1.contribution, 'cyan')
    print_color("Rank", u1.rank, 'cyan')
    print_color("Rating", u1.rating, 'cyan')
    print_color("Max Rank", u1.maxRank, 'cyan')
    print_color("Max Rating", u1.maxRating, 'cyan')    
