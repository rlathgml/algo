# 파이썬 알고리즘 인터뷰 P.145
# 투포인터 이용
from typing import List


def reverse_string(s: List[str]):
    left, right = 0, len(s) -1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# 파이썬다운 방식
def reverse_string2(s: List[str]):
    s.reverse()



a = ["a","b","c","d"]
reverse_string2(a)
print(a)