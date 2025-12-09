class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed) , key=lambda x: -x[0])
        stack = []
        for pos,spe in cars:
            arrival_time = (target - pos) / spe
            if stack and arrival_time <= stack[-1]:
                continue
            stack.append(arrival_time)
        return len(stack)

