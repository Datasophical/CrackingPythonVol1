class Gatekeeper:
    def containsDuplicateQR(self, guests: List[int]) -> bool:
        scanner = set(guests)
        return len(guests) != len(scanner)
