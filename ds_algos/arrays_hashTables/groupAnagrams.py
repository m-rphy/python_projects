# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)

    for s in strs:
        # creating a list of 26 zeros
        count = [0] * 26
        for c in s:
            #  counting the number of occurrences of each letter in a string,
            # using the ASCII value of the letters to determine their index in the count list
            count[ord(c) - ord("a")] += 1
        # this line is grouping the strings by their character counts.
        # All the anagrams have the same counts and hence end up in the
        # same list in the dictionary
        ans[tuple(count)].append(s)
    return list(ans.values())


print(
    groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
)  # -> dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])


# NOTE more detail:
# ord(c): This is a built-in function in Python that returns an
# integer representing the Unicode character.
#
# For example, ord('a') will return 97
