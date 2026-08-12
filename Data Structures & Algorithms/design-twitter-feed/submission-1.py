class Twitter:

    def __init__(self):
        self.followings = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        feed = []

        users = self.followings[userId]
        users.add(userId)

        for u in users:
            for tweet in self.tweets[u]:
                heapq.heappush(heap, (-tweet[0], tweet[1]))

        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followings[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].discard(followeeId)
        
