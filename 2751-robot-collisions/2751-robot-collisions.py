class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):

        n = len(positions)
        order = sorted(range(n), key=lambda i: positions[i])

        h = healths[:]
        alive = [True]*n
        stack = []

        for idx in order:

            if directions[idx] == 'R':
                stack.append(idx)

            else:
                while stack:

                    top = stack[-1]

                    if h[top] < h[idx]:
                        alive[top] = False
                        stack.pop()
                        h[idx] -= 1

                    elif h[top] > h[idx]:
                        alive[idx] = False
                        h[top] -= 1
                        break

                    else:
                        alive[top] = False
                        alive[idx] = False
                        stack.pop()
                        break

        return [h[i] for i in range(n) if alive[i]]

        
        n = len(positions)
        pos = sorted(zip(positions, healths, directions))
        stack = [] # (health, direction)
        for i, (p, h, d) in enumerate(pos):
            if d == "L":
                while stack and stack[-1][2] == "R" and h > 0:
                    prev_p, prev_h, prev_d = stack.pop()
                    if prev_h == h:
                        break
                    elif prev_h < h:
                        stack.append((p, h - 1, "L"))
                    else:
                        h = 0
                        stack.append((p, prev_h - 1, "R"))
            else:
                stack.append((p, h, d))
        res = [x[1] for x in stack]
        print(pos)
        print(stack)
        return res