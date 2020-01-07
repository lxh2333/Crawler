from collections import deque

class Queue(object):
    mydequeue=deque(maxlen=100)
    def get(self,count):
        proxies=[]
        for i in range(count):
            proxy=self.mydequeue.popleft()
            proxies.append(proxy)
        return proxies

    def put(self,proxy):
        self.mydequeue.append(proxy)
    def pop(self):
        return self.mydequeue.pop()
    @property
    def queue_len(self):
        return len(self.mydequeue)
