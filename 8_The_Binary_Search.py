class CyberSearch:
    def binarySearch(self, db: list[int], target: int) -> int:
        low = 0
        high = len(db) - 1
        while low <= high:
            mid = (low + high) // 2
            if db[mid] == target:
                return mid
            elif db[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
