class Twitter:

    def __init__(self):
        self.Twitter = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.Twitter[userId].append(userId)
        self.posts[userId].append((self.time,tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.Twitter[userId].add(userId)
        users =  self.Twitter[userId]
        heap = []
        for user in users:
            if user in self.posts:
                index = len(self.posts[user]) - 1
                count, tweet = self.posts[user][index]
                heapq.heappush(heap,[count,tweet,user,index-1])
        res = []
        while heap and len(res) < 10:
            count,tweet,user,index = heapq.heappop(heap)
            res.append(tweet)
            if index >= 0:
                new_c, new_t = self.posts[user][index]
                heapq.heappush(heap,[new_c,new_t,user,index-1])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.Twitter[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.Twitter[followerId].discard(followeeId)
    

    # we need to have list of users a user follows 
    # and that list will have for each user you need to know what they are posting 
    # need to represent the user ids and then also need to get their posts 


        
