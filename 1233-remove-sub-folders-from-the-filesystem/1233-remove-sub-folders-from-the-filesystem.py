class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # f = sorted(folder)
        # seen = set()
        # for x in f:
        #     end = 1
        #     while end < len(x):
        #         while end < len(x) and x[end] != '/':
        #             end += 1
        #         if x[:end] in seen:
        #             break
        #         end += 1
        #     if x[:end] not in seen:
        #         seen.add(x[:end])
        # return list(seen)


        # Sort the folders lexicographically so parent folders come before their subfolders
        folder.sort()
        
        # Initialize result list with the first folder
        ans = [folder[0]]
        
        # Iterate through remaining folders starting from index 1
        for i in range(1, len(folder)):
            # Get the last added folder path and add a trailing slash
            last_folder = ans[-1] + '/'
            
            # Check if current folder starts with last_folder
            # If it doesn't start with last_folder, then it's not a subfolder
            if not folder[i].startswith(last_folder):
                ans.append(folder[i])
        
        return ans