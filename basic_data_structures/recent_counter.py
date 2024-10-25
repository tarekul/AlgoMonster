class RecentCounter:
    def __init__(self):
        self.requests = []
        self.counter = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests and self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)

recentCounter = RecentCounter()
print(recentCounter.ping(1))
print(recentCounter.ping(100))
print(recentCounter.ping(3001))
print(recentCounter.ping(3002))