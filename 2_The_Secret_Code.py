class SecretCode:
   def isAnagram(self, s: str, t: str) -> bool:
       return sorted(s) == sorted(t)
