class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list) # uid: stack<count, tweetID>
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        #self.follows[userId].add(userId)
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.follows[userId].add(userId)
        for followeeId in self.follows[userId]:
            if followeeId in self.tweets:
                idx = len(self.tweets[followeeId]) - 1
                count, tweet = self.tweets[followeeId][idx]
                heap.append([count, tweet, followeeId, idx - 1])
        heapq.heapify(heap)
        
        res = list()
        while heap and len(res) < 10:
            count, tweet, followeeId, index = heapq.heappop(heap)
            res.append(tweet)
            if index >= 0:
                count, tweet = self.tweets[followeeId][index]
                heapq.heappush(heap, [count, tweet, followeeId, index - 1])
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)