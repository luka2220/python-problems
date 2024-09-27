"""
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). 
The resulting string will be "dcbaefd".

Return the resulting string.
"""

def reversePrefix(word: str, ch: str) -> str:
        counter = 0
        for s in word:
            if s == ch:
                break
            counter += 1
        
        if counter == len(word):
            return word
        else:
            return word[:counter+1][::-1] + word[counter+1:]
