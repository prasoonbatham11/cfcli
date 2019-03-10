class Contest:
    def __init__(self, contest):
        self.id = contest.get("id")
        self.name = contest.get("name")
        self.type = contest.get("type")
        self.phase = contest.get("phase")
        self.frozen = contest.get("frozen")
        self.durationSeconds = contest.get("durationSeconds")
        self.startTimeSeconds = contest.get("startTimeSeconds")
        self.relativeTimeSeconds = contest.get("relativeTimeSeconds")
        self.preparedBy = contest.get("preparedBy")
        self.websiteUrl = contest.get("websiteUrl")
        self.description = contest.get("description")
        self.difficulty = contest.get("difficulty")
        self.kind = contest.get("kind")
        self.icpcRegion = contest.get("icpcRegion")
        self.country = contest.get("country")
        self.city = contest.get("city")
        self.season = contest.get("season")

class RatingChange:
    def __init__(self, user):
        self.contestId = user.get("contestId")
        self.contestName = user.get("contestName")
        self.handle = user.get("handle")
        self.rank = user.get("rank")
        self.ratingUpdateTimeSeconds = user.get("ratingUpdateTimeSeconds")
        self.oldRating = user.get("oldRating")
        self.newRating = user.get("newRating")

class User:
    def __init__(self, user):
        self.handle = user.get("handle")
        self.email = user.get("email")
        self.vkld  = user.get("vkld")
        self.openId = user.get("openId")
        self.firstName = user.get("firstName")
        self.lastName = user.get("lastName")
        self.country = user.get("country")
        self.city = user.get("city")
        self.organization = user.get("organization")
        self.contribution = user.get("contribution")
        self.rank = user.get("rank")
        self.rating = user.get("rating")
        self.maxRank = user.get("maxRank")
        self.maxRating = user.get("maxRating")
        self.lastOnlineTimeSeconds = user.get("lastOnlineTimeSeconds")
        self.registrationTimeSeconds = user.get("registrationTimeSeconds")
        self.friendOfCount = user.get("friendOfCount")
        self.avatar = user.get("avatar")
        self.titlePhoto = user.get("titlePhoto")
    
class Problem:
    def __init__(self, problem):
        self.contestId = problem.get("contestId")
        self.problemsetName = problem.get("problemsetName")
        self.index = problem.get("index")
        self.name = problem.get("name")
        self.type = problem.get("type")
        self.points = problem.get("points")
        self.rating = problem.get("rating")
        self.tags = problem.get("tags")

class ProblemStatistics:
    def __init__(self, ps):
        self.contestId = ps.get("contestId")
        self.index = ps.get("index")
        self.solvedCount = ps.get("solvedCount")

class BlogEntry:
    def __init__(self, b):
        self.id = b.get("id")
        self.originalLocale = b.get("originalLocale")
        self.creationTimeSeconds = b.get("creationTimeSeconds")
        self.authorHandle = b.get("authorHandle")
        self.title = b.get("title")
        self.content = b.get("content")
        self.locale = b.get("locale")
        self.modificationTimeSeconds = b.get("modificationTimeSeconds")
        self.allowViewHistory = b.get("allowViewHistory")
        self.tags = b.get("tags")
        self.rating = b.get("rating")

class Comment:
    def __init__(self, c):
        self.id = c.get("id")
        self.creationTimeSeconds = c.get("creationTimeSeconds")
        self.commentatorHandle = c.get("commentatorHandle")
        self.locale = c.get("locale")
        self.text = c.get("text")
        self.parentCommentId = c.get("parentCommentId")
        self.rating = c.get("rating")
        if not self.parentCommentId:
            self.parentCommentId = 0

class Member:
    def __init__(self, m):
        self.handle = m.get("handle")

class Party:
    def __init__(self, p):
        self.contestId = p.get("contestId")
        self.members = [Member(i) for i in p.get("members")]
        self.participantType = p.get("participantType")
        self.teamId = p.get("teamId")
        self.teamName = p.get("teamName")
        self.ghost = p.get("ghost")
        self.room = p.get("room")
        self.startTimeSeconds = p.get("startTimeSeconds")

class Submission:
    def __init__(self, p):
        self.id = p.get("id")
        self.contestId = p.get("contestId")
        self.creationTimeSeconds = p.get("creationTimeSeconds")
        self.relativeTimeSeconds = p.get("relativeTimeSeconds")
        self.programmingLanguage = p.get("programmingLanguage")
        self.verdict = p.get("verdict")
        self.testset = p.get("testset")
        self.passedTestCount = p.get("passedTestCount")
        self.timeConsumedMillis = p.get("timeConsumedMillis")
        self.memoryConsumedBytes = p.get("memoryConsumedBytes")
        self.problem = Problem(p.get("problem"))
        self.author = Party(p.get("author"))

class ProblemResult:
    def __init__(self, p):
        self.points = p.get("points")
        self.penalty = p.get("penalty")
        self.rejectedAttemptCount = p.get("rejectedAttemptCount")
        self.type = p.get("type")
        self.bestSubmissionTimeSeconds = p.get("bestSubmissionTimeSeconds")

class RanklistRow:
    def __init__(self, r):
        self.party = Party(r.get("party"))
        self.rank = r.get("rank")
        self.points = r.get("points")
        self.penalty = r.get("penalty")
        self.successfulHackCount = r.get("successfulHackCount")
        self.unsuccessfulHackCount = r.get("unsuccessfulHackCount")
        self.lastSubmissionTimeSeconds = r.get("lastSubmissionTimeSeconds")
        self.problemResults = [ProblemResult(i) for i in p.get("problemResults")]
