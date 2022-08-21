import collections
import heapq

class Twitter:

    def __init__(self):
        self.follows = collections.defaultdict(set) # uid: set(uids)
        self.tweets = collections.defaultdict(list) # uid: stack <time, tweetID>
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = list()
        heap = []
        self.follows[userId].add(userId) # when they only follow themselves
        
        for followeeId in self.follows[userId]:
            if followeeId in self.tweets:
                idx = len(self.tweets[followeeId]) - 1
                count, tweet = self.tweets[followeeId][idx]
                heap.append([count, tweet, followeeId, idx - 1])
                
        heapq.heapify(heap)
        
        while heap and len(res) < 10:
            time, tweet, followeeId, idx = heapq.heappop(heap)
            res.append(tweet)
            if idx >= 0:
                # also push this onto heap
                count, tweet = self.tweets[followeeId][idx]
                heapq.heappush(heap, [count, tweet, followeeId, idx - 1])
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)