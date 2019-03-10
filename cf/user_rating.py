from cf.classes import *
from colorama import Fore, Back, Style
from cf.util import *
from datetime import datetime


def user_rating(user):
    user = user['result']
    n = len(user)
    ratings = []
    for i in range(n):
        ratings.append(RatingChange(user[i]))
    x = []
    y = []
    
    for i in range(n):
        a = ratings[i].ratingUpdateTimeSeconds
        a = datetime.fromtimestamp(a).strftime("%d%m%Y")
        x.append(a)
        y.append(ratings[i].newRating)

    print("\n\tRating Chart for user : "+Fore.BLACK+Back.YELLOW+'{:10s}'.format(" "+ratings[0].handle+" ")+Style.RESET_ALL);
    plotterm(x,y)
    
