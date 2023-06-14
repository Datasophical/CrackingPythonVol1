class PalindromeRapper:
    def isPalindrome(self, lyrics_quote: str) -> bool:
        cleaned_lyrics_quote = ''.join(char.lower() for char in lyrics_quote if char.isalnum())
        return cleaned_lyrics_quote == cleaned_lyrics_quote[::-1]
