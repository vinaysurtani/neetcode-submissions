class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list) # [(count, tweetId)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # news feed
        minHeap = [] # counts are negative, so lowest count will be on root
        self.followMap[userId].add(userId) #self add user, it follows itself
        for followeeId in self.followMap[userId]: #go through each of the followers of that userId
            if followeeId in self.tweetMap: #first check if that Id even exists in tweetMap
                index = len(self.tweetMap[followeeId]) - 1 #start from last value of that list(latest value) 
                count, tweetId = self.tweetMap[followeeId][index] #pull value of that specific index
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1]) # add all 4 vars, for while loop later, index is reduced as we have to traverse thru the list
        while minHeap and len(res) < 10: 
            count, tweetId, followeeId, index = heapq.heappop(minHeap) # take all vals
            res.append(tweetId)
            if index >= 0: #check for index val, i <0 then moves to next followeeId
                count, tweetId = self.tweetMap[followeeId][index] #note: its index - 1  here actually, so we moved downa value
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1]) #pushed value to heap and done index -1 
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)