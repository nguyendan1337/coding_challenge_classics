
#initial attempt, brute force
#passes 31/40
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size = len(gas)
        for i in range(size):
            # print(f"starting at {i}")
            tank = gas[i]
            current_station = i
            # print(f"current_station: {current_station}, tank: {tank}, cost: {cost[current_station]}")
            if tank >= cost[i]:
                tank -= cost[i]
                if current_station + 1 >= size:
                    current_station = 0
                else:
                    current_station += 1
                if current_station == i:
                    return i
                while current_station != i and tank > 0:
                    tank += gas[current_station]
                    # print(f"current_station: {current_station}, tank: {tank}, cost: {cost[current_station]}")
                    if tank >= cost[current_station]:
                        tank -= cost[current_station]
                        if current_station + 1 >= size:
                            current_station = 0
                        else:
                            current_station += 1
                        if current_station == i:
                            return i
                    else:
                        break
        return -1;

    from typing import List

#grok solution
#optimized aha solution
#must realize that if total gas < total cost, then impossible

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        total_surplus = 0   # sum(gas) - sum(cost)
        current_surplus = 0
        start = 0

        for i in range(n):
            total_surplus += gas[i] - cost[i]
            current_surplus += gas[i] - cost[i]

            if current_surplus < 0:
                # Any station from previous 'start' to current 'i' cannot be the answer
                start = i + 1
                current_surplus = 0

        # If total gas is not enough, impossible
        return start if total_surplus >= 0 else -1


