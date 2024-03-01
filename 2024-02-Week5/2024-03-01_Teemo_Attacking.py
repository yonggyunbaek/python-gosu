"""
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

 

Example 1:

Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
Example 2:

Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
 

Constraints:

1 <= timeSeries.length <= 104
0 <= timeSeries[i], duration <= 107
timeSeries is sorted in non-decreasing order.
"""

# 풀이1 / 시간초과
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        sort(timeSeries)
        for t in timeSeries:
            for d in range(t, t+duration):
                ans.append(d)
        ans = list(set(ans))
        return len(ans)
    
# 풀이 2
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        """
        1. 반복문으로 timeSeries에서 시간 뽑아냄.
        2. 뽑아낸 시간에 duration을 더해서 중독 시간 추출.
        3. 이전 loop에서 만들어진 중독시간보다 내가 작으면 중독시간 갱신하고 스테이.
        4. 만약 loop의 t가 중독시간보다 크면, total_time에 (중독시간 - 처맞은 시간)을 더함
        """
        
        attacked_time, poisonduration = timeSeries[0], timeSeries[0] + duration - 1
        total_time = 0
        for t in range(1, len(timeSeries)):#2

            if timeSeries[t] <= poisonduration: # Loop의 현재시간이 중독이 끝나는 시간보다 작으면, 현재시간에 중독시간만 갱신해서 더함 1 < 2
                # 중독시간 갱신
                poisonduration = timeSeries[t] + (duration - 1)# ~2
            else:# t > poisonduration
                total_time = total_time + (poisonduration - attacked_time + 1)
                attacked_time = timeSeries[t]
                # 중독시간 갱신
                poisonduration = timeSeries[t] + (duration - 1)# ~2

        total_time = total_time + (poisonduration - attacked_time + 1)
        return total_time