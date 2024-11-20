import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# : 1436 _ 영화감독 숌

# <등급>
# : 실버 5
    
# <내가 파악한 요구사항>
# : 구현

# <실제 요구사항>
# : 브루트포스
    
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
'''
입력으로 n을 받음
n번째 영화 제목 = (n-1)666

187 -> 66666
500 -> 166699
의 예제로 확인 했을때 위의 수도코드와 같은 방법으로는
예제 출력값을 일치 시킬 수 없다.
'''
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>

n = int(input())
count = 0
current = 666

while True:
    if "666" in str(current):
        count += 1
        if count == n:
            print(current)
            break
    current += 1

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>

N = int(input())  # N번째 영화 제목
count = 0         # "666"이 포함된 숫자의 개수
current = 666     # 현재 확인 중인 숫자

while True:
    if "666" in str(current):  # 숫자에 "666"이 포함되어 있는지 확인
        count += 1             # 포함되면 카운트를 증가
        if count == N:         # N번째 숫자를 찾으면 출력 후 종료
            print(current)
            break
    current += 1  # 숫자를 증가시켜 다음 숫자 확인

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>