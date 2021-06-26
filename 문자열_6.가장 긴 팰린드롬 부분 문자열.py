# 파이썬 알고리즘 인터뷰 P.159


# 1. 중앙을 중심으로 확장하는 풀이
# 2칸, 3칸으로 구성된 투포인터가 슬라이딩 윈도우처럼 전진하다가
# 윈도우에 들어온 문자열이 팰린드롬인 경우
# 그 자리에 멈추고 투 포인터가 양 끝으로 점점 확장해 나가는 식
# 2칸, 3칸인 이유 --> 팰린드롬이 bb 처럼 짝수일 때도 있고, bab 처럼 홀수일 때도 있기 때문
def longest_palindrome(s: str) -> str:
    # 팰린드롬 판별 및 투포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right] # while 빠져나올 때 한칸씩 늘려서 나온 상태니까 left + 1, right는 슬라이싱에서는 미포함이니까 그대로 리턴

    # 예외처리
    if len(s) < 2 or s == s[::-1]:
        return s

    # 슬라이딩 윈도우 이동
    result = ''
    for i in range(0, len(s) - 1):
        result = max(result,
                     expand(i, i+1),
                     expand(i, i+2),
                     key=len)

    return result

print(longest_palindrome("12345432"))