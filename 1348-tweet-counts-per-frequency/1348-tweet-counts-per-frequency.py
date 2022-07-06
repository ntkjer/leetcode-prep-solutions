class TweetCounts:

    def __init__(self):
        self.tweets = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        period = 60
        if freq == "hour":
            period *= 60
        elif freq == "day":
            period *= 60 * 24
        
        res = [0] * ((endTime - startTime) // period + 1)
        
        start_idx = bisect.bisect_left(self.tweets[tweetName], startTime)
        end_idx = bisect.bisect_right(self.tweets[tweetName], endTime)
        
        for i in range(start_idx, end_idx):
            ts = (self.tweets[tweetName][i] - startTime) // period
            res[ts] += 1
            
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)