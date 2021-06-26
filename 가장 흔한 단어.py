# 파이썬 알고리즘 인터뷰 P.151
from typing import List
import re
import collections


def most_common_word(p: str, b: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', p)
        .lower().split()
             if word not in b]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
