class TweetCounts:

    def __init__(self):
        self.data = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.data[tweetName], time) 
        
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        minute = 60
        hour = minute * 60
        day = hour * 24
        period = 0
        
        if freq == "minute":
            period = minute
        elif freq == "hour":
            period = hour
        else:
            period = day
        
        result = [0] * ((endTime - startTime) // period + 1)
        start = bisect.bisect_left(self.data[tweetName], startTime)
        end = bisect.bisect_right(self.data[tweetName], endTime)
        
        for i in range(start, end):
            ts = (self.data[tweetName][i] - startTime) // period
            result[ts] += 1
            
        return result
        
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)