class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        return [anagram for anagram in possible_anagrams if self._is_anagram(anagram)]

    def _is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        return sorted(candidate_lower) == sorted(self.word) and candidate_lower != self.word
