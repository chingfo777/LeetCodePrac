from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        result = []

        # Check each offset from 0 to word_len - 1
        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            words_used = 0

            while right + word_len <= len(s):
                word = s[right : right + word_len]
                right += word_len

                if word in word_counts:
                    current_counts[word] += 1
                    words_used += 1

                    # If the word occurs more times than required, shrink from the left
                    while current_counts[word] > word_counts[word]:
                        left_word = s[left : left + word_len]
                        current_counts[left_word] -= 1
                        words_used -= 1
                        left += word_len

                    # If we matched all words, record the starting position
                    if words_used == num_words:
                        result.append(left)
                else:
                    # Reset window if word is not in words list
                    current_counts.clear()
                    words_used = 0
                    left = right

        return result