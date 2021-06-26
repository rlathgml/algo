# 파이썬 알고리즘 인터뷰 p.173
from typing import List


nums = [2,7,11,15]
target = 9


# 내 코드
# 브루트 포스 방식
def my_two_sum(nums: List, target: int) -> List:
    for i in range(len(nums) -1):
        for j in range(i+1, len(nums) ):
            if target == nums[i] + nums[j]:
                return [i, j]


print("내가 짠 코드 : ", end=" ")
print(my_two_sum(nums, target))


# in을 이용한 탐색
# 타겟에서 첫번째 값을 뺀 값 (taraget - n) 이 존재하는지 탐색해보기
# 오,,,
def two_sum2(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1 :]:
            return [i, nums[i+1:].index(complement) + (i+1)]

print("in을 이용한 탐색 : ", end=" ")
print(two_sum2(nums, target))


# 첫번째 수를 뺀 결과 키 조회
# 비교나 탐색 대신 한번에 정답을 찾을 수 있는 방법
def two_sum3(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    #키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
