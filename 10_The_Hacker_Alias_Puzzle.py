class ICPCode:
    def groupAliases(self, aliases):
        aliasGroups = collections.defaultdict(list)
        for alias in aliases:
            charCount = [0] * 26
            for char in alias:
                charCount[ord(char) - ord('a')] += 1
            aliasGroups[tuple(charCount)].append(alias)
        return aliasGroups.values()
