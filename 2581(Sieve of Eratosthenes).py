# 두 정수를 입력 받는다.
M = int(input())
N = int(input())

sieve = [False for i in range(N + 1)]

# 에라토스테네스의 체를 이용
for i in range(2, int(N ** 0.6)):
    if sieve[i] == False:
        for j in range(2 * i, N + 1, i):
            sieve[j] = True

# 결과값으 저장할 리스트를 생성
result = []

for i in range(M, N + 1):
    if i >= 2:
        if sieve[i] == False:
            result.append(i)

# 요구사항을 출력 해볼까요!
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
