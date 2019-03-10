from cf.classes import *
from cf.util import *

def contest_list(contests, num):
    contests = contests['result']
    n = len(contests)
    p = []
    for i in range(n):
        p.append(Contest(contests[i]))

    found = False
    for i in range(n):
        if p[i].id==num:
            disp_contest(p[i])
            found = True
            break
    if not found:
        print_head("No Contest with the provided id", 'red')
    
    
def disp_contest(contest):
    print("\n")
    print_head("Contest Details", 'red')
    print_color("ID", contest.id, 'cyan')
    print_color("Name", contest.name, 'cyan')
    print_color("Type", contest.type, 'cyan')
    print_color("Phase", contest.phase, 'cyan')
    print_color("Duration", seconds_to_hrs(-contest.durationSeconds), 'cyan')
    if contest.startTimeSeconds:
        print_color("Start Time", format_date(contest.startTimeSeconds), 'cyan')
    if contest.relativeTimeSeconds:
        print_color("Time Left", seconds_to_hrs(contest.relativeTimeSeconds), 'cyan')
    if contest.preparedBy:
        print_color("Prepared By", contest.preparedBy, 'cyan')
    if contest.websiteUrl:
        print_color("Website Url", contest.websiteUrl, 'cyan')
    if contest.difficulty:
        print_color("Difficulty", contest.difficulty, 'cyan')
    if contest.kind:
        print_color("Kind", contest.kind, 'cyan')
    if contest.description:
        print_color("Description", contest.description, 'cyan')
    if contest.icpcRegion:
        print_color("IcpcRegion", contest.icpcRegion, 'cyan')
    if contest.country:
        print_color("Country", contest.country, 'cyan')
    if contest.city:
        print_color("City", contest.city, 'cyan')
    if contest.season:
        print_color("Season", contest.season, 'cyan')

