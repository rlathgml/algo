# 파이썬 알고리즘 인터뷰 P.153
from typing import List
import collections


def anagram(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # anagrams[''.join(sorted(word))].append(word)
        print(sorted(word))
    return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagram(strs))