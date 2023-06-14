class BankSecurity:
    def findRobbers(self, customers: List[int], robbersWeight: int) -> List[int]:
        weightMap = {}
        for index, weight in enumerate(customers):
            potentialMatch = robbersWeight - weight
            if potentialMatch not in weightMap:
                weightMap[weight] = index
            else:
                return [weightMap[potentialMatch], index]
