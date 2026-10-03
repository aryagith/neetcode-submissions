class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charcount = {}
        for char in chars:
            charcount[char] = charcount.get(char,0) + 1

        result = 0
        for word in words:
            cur_word = defaultdict(int)
            good = True
            for char in word:
                if char in charcount and cur_word[char]<charcount[char]:
                    cur_word[char] += 1
                else:
                    good = False
                    break 
            if good:
                result += len(word)

        return result

                     

        


            