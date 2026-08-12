class Twitter:
    def __init__(self):
        self.userPosts = [[] for _ in range(100)]
        self.userFollowList = [[] for _ in range(100)]
        self.timestamp = -1

    def quickSort(self, array):
        if len(array) <= 1:
            return array

        pivot = array[len(array) // 2][1]

        left = [i for i in array if i[1] < pivot]
        mid = [i for i in array if i[1] == pivot]
        right = [i for i in array if i[1] > pivot]

        return self.quickSort(left) + mid + self.quickSort(right)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.userPosts[userId].append([tweetId, self.timestamp])

    def getNewsFeed(self, userId: int):
        result = []
        
        listFollowing = self.userFollowList[userId][:]
        listFollowing.append(userId)

        candidates = []

        for uid in listFollowing:
            posts = self.userPosts[uid]
            for tweet in posts[-10:]:
                candidates.append(tweet)

        sortedCandidates = self.quickSort(candidates)

        top10sorted = sortedCandidates[-10:][::-1]

        return [tweetId for tweetId, _ in top10sorted]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId not in self.userFollowList[followerId]:
            self.userFollowList[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.userFollowList[followerId]:
            self.userFollowList[followerId].remove(followeeId)