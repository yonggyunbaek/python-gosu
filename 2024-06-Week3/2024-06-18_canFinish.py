"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [[a,b]] : a를 수강하려면 b를 반드시 들어야 함.
        """
        1. 먼저 입력된 선수과목 정보를 활용하여 각 과목의 선수과목 목록을 구축하는 것이 중요합니다.
        2. 그리고 각 과목의 진입차수(indegree)를 계산하여, 진입차수가 0인 과목부터 순서대로 수강할 수 있는지 확인해야 합니다.
        3. 이를 위해 큐(queue) 자료구조를 활용하는 것이 좋습니다. 진입차수가 0인 과목부터 큐에 넣고, 해당 과목을 수강한 뒤 관련된 과목의 진입차수를 줄여나가는 식으로 진행하면 됩니다.
        4. 만약 큐에 남은 과목이 없고, 모든 과목의 진입차수가 0이 되었다면 True를 반환합니다. 그렇지 않다면 False를 반환합니다.
        5. 이 알고리즘의 핵심은 진입차수를 계산하고 이를 기반으로 과목 수강 순서를 결정하는 것입니다. 이 힌트를 바탕으로 문제를 해결해보세요.
        """
        
        # 1.
        pre_dict = defaultdict(list)
        for a, b in prerequisites:
            if b not in pre_dict:
                pre_dict[b] = [a]
            else:
                pre_dict[b] += [a]
        # print(pre_dict)
    
        # 2.
        indegree = [0] * numCourses
        for prereqs in pre_dict.values():
            for course in prereqs:
                indegree[course] += 1
        # print(indegree)
        
        # 3. indegree 0인 index deque 추가
        queue = deque([course for course in range(numCourses) if indegree[course] == 0])
        count = 0
        # print(queue)
        
        # 4. 
        while queue:
            course = queue.popleft()
            count += 1
        
            # 해당 과목을 수강한 후 indegree 감소
            for p in pre_dict[course]:
                indegree[p] -= 1
                if indegree[p] == 0:
                    queue.append(p)
    
       # 모든 과목을 수강했는지 확인
        return count == numCourses