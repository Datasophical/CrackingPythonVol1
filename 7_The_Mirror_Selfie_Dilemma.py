class SelfieFixer:
    def reverseShirtSlogan(self, slogan: List[str]) -> None:
        left, right = 0, len(slogan) - 1
        while left < right:
            # Swap characters
            slogan[left], slogan[right] = slogan[right], slogan[left]
            left += 1
            right -= 1
