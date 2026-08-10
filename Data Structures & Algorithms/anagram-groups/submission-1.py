class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dir = {}
        anagram_dir = {}
        group = []
        for index,string in enumerate(strs):
            for char in string:
                char_dir[char] = char_dir.get(char, 0) + 1
            key = tuple(sorted(char_dir.items()))
            if key in anagram_dir:
                anagram_dir[key].append(string)
            else:
                anagram_dir[key] = [string]
            char_dir.clear()

        for key in anagram_dir:
            group.append(anagram_dir[key])
        return group