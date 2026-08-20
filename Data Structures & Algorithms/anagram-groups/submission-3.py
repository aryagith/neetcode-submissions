class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        known_words = {}
        for word in strs:
            if tuple(sorted(word)) not in known_words:
                known_words[tuple(sorted(word))] = []
            
            known_words[tuple(sorted(word))].append(word)
        
        anagrams = []
        for value in known_words.values():
            anagrams.append(value)
        
        return anagrams
