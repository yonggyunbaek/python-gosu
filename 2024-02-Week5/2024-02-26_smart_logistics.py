# softeer 스마트 물류

# 라인 길이 N, 부품 잡기 가능 거리 K
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
location = list(input().strip())


cnt = 0
# 반복문을 통해 로봇을 찾는다.
for i in range(n):
    if location[i] == "P":
        # 로봇의 위치에서 바로 옆에 인접한 거리가 K이하인 부품을 찾는다.
        for j in range(i-k,i+k+1):
            # 부품을 집는 거리는 라인의 길이를 넘지않게 한다.
            if j < 0 or j > n:
                continue
            # 집은 부품은 다른 이름으로 바꿔 구분한다.
            elif location[j] == "H":
                # 부품을 집는 순간 카운트 해주고 break
                cnt += 1
                location[j] = "A"
                break

print(cnt)

