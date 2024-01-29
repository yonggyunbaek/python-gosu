# 헬스장 N명, 1 ~ N 번호 부여
# i번 회원의 역기 무게 Wi
# M개의 친분관계 (Aj,Bj)
# i번 회원은 친분 관계가 있는 사람보다 자기가 더 무겁게 들면 최고라고 생각, 친분 없어도 본인이 최고라고 생각
# 최고라고 생각하는 회원 몇 명?
# N명 M개 관계
# W1 W2 W3 .. N번째 무게
# A1 B1
# A2 B2 
# ..M번째 관계

# 예시 입력 
# 5 3
# 1 2 3 4 5
# 1 3
# 2 4
# 2 5


def solution():
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    graph = {i: [] for i in range(N)}
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
#    answer = sum(all(weights[i] > weights[other] for other in graph[i]) for i in graph)
    answer = 0
    for i in graph:
        all_true = all(weights[i] > weights[other] for other in graph[i]) 
        # all 안의 조건이 참이면 True / list comprehension일 때는 True, False로 이루어진 리스트를 확인해서 모두 True이면 True 반환
        # [True,True,True] --> True
        answer += all_true
    print(answer)


if __name__ == "__main__":
    solution()