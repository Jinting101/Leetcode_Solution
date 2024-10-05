class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        # if len(skill) == 2:
        #     return skill[0] * skill[1]
        # num_teams = len(skill) / 2
        # team_skill = sum(skill) / num_teams
        # res = sorted(skill)
        # ans = 0
        # for i in range(num_teams):
        #     if res[i] + res[len(res)-i-1] != team_skill:
        #         return -1
        #     ans += res[i]*res[len(res)-i-1]
        # return ans

        total = sum(skill)
        if total % (len(skill) // 2) != 0:
            return -1

        target = total // (len(skill) // 2)
        mapp = {}
        ans = 0
        
        for n in skill:
            if target - n in mapp and mapp[target - n] > 0:
                ans += n * (target - n)
                mapp[target - n] -= 1
            else:
                mapp[n] = mapp.get(n, 0) + 1
        
        # Ensure all players are paired
        for count in mapp.values():
            if count > 0:
                return -1
        return int(ans)

# Step 1: Calculate total skill and target skill sum
# First, calculate the total sum of all player skills. The target combined skill for each team will be the total sum divided by n / 2, where n is the total number of players.
# If the total skill sum cannot be evenly divided, return -1, since it would be impossible to divide players into teams with equal combined skills.

# Step 2: Use hash map to track pairings
# Iterate through the skill array. For each skill, calculate the complement needed to achieve the target combined skill. If the complement is already in the hash map and has a non-zero count, pair the current skill with the complement, calculate the chemistry, and update the answer.
# If the complement is not in the map, store the current skill as a potential pairing for future elements.

# Step 3: Return chemistry sum
# If all pairs are formed correctly, return the total chemistry. Otherwise, return -1 if any players remain unpaired.
