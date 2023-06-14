import collections
import heapq

class CipherFrequency:   
    def topKFrequent(self, encrypted: List[int], k: int) -> List[int]:
        count = collections.Counter(encrypted)
        return heapq.nlargest(k, count.keys(), key=count.get)
