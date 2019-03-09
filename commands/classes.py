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
