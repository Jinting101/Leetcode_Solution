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

        if sum(skill) % (len(skill)//2) != 0:
            return -1
        target = sum(skill) // (len(skill)//2)

        freq = {}
        for x in skill:
            freq[x] = freq.get(x, 0) + 1

        chem = 0
        used = set()
        for key in list(freq.keys()):
            if key in used:
                continue
            freq_key = freq[key]
            complement = target - key
            if complement not in freq or freq_key != freq[complement] or (key == complement and freq_key%2 != 0 ):
                return -1

            if key == complement:
                chem += (key * complement) * (freq_key // 2)

            else:
                chem += (key * complement) * freq_key

            used.add(key)
            used.add(complement)

        return chem

# first we have to know the target sum of any pair /
# that is we know that the total sum will be divided into n/2 pairs
# so target sum=total sum/n/2
# now that we have ts(target sum) for any skill we can fins the compleimntary skill ie ts-skill
# now we will loop througt the array and store the frequencies of all the skills
# then we want to check for every skill there needs to be an equal number of complimentary skills
# if not some skills will be left out meaning not possible to make pairs meaning return -1
# else we will keep track of their product also called chemistry and reutrn the chem finally

