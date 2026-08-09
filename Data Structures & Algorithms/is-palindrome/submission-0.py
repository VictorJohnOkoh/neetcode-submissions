class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ""
        for word in s.lower():
            if word.isalnum():
                clean_string += word
        return clean_string == clean_string[::-1]