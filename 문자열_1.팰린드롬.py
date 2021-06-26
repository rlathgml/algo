# 파이썬 알고리즘 인터뷰 P.138
# 유효한 팰린드롬
from typing import Deque
import collections
from collections import deque
import re


def ispalindrome1(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True



# 데크를 이용한 최적화
def ispalindrome2(s: str) -> bool:
    strs: Deque = collections.deque() # 데크 쓰면 속도 빨라짐

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True



#슬라이싱 활용
def ispalindrome3(s: str) -> bool:
    s.lower()

    s = re.sub('[^a-z0-9]' , '' , s)

    return s == s[::-1]



print(ispalindrome3("abcddcba"))