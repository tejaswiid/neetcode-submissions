class Twitter:

    def __init__(self):
        self.Twitter = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.Twitter[userId].append(userId)
        self.posts[userId].append((self.time,tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.Twitter[userId] | {userId}
        heap = []
        for user in users:
            tweets = self.posts[user]
            for tweet in tweets:
                heapq.heappush(heap,tweet)
        
        res = [val[1] for val in sorted(heap,reverse=True)]
        return res[:10]
        

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.Twitter[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.Twitter[followerId].discard(followeeId)
    

    # we need to have list of users a user follows 
    # and that list will have for each user you need to know what they are posting 
    # need to represent the user ids and then also need to get their posts 


        
