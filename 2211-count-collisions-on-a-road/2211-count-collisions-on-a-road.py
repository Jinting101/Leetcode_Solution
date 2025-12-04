class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip("L")
        directions = directions.rstrip("R")

        return directions.count("R") + directions.count("L")

        # res = directions.count("RL")
        # directions.replace("RL", "S")
        # stack = []
        # for x in directions:




        # RLSLR

        # RL
        # S - RL
        # SL
        # RS

        