# Remember that type hinting (related to the below "from" import)
# is completely optional but makes your code more clear.
# Review Ch 4. Functions - "What is a Function?"
from typing import List

# Run this code using this command on your Terminal or command line:
# python3 0b_Example_Test_Code.py 
class Gatekeeper:
    def containsDuplicateQR(self, guests: List[int]) -> bool:
        scanner = set(guests)
        return len(guests) != len(scanner)

# Instantiate the class
gate = Gatekeeper()

# Provide a list of guest QR codes
guests = [123, 456, 789, 123]  # This list contains a duplicate

# Use the method to check for duplicates
if gate.containsDuplicateQR(guests):
    print("There are duplicate QR codes.")
else:
    print("There are no duplicate QR codes.")
