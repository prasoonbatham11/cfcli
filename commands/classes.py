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
    
        
