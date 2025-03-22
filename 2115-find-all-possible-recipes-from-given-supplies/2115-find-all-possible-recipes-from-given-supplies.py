class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = {}
        avail = set(supplies)
        memo = {}

        def dfs(curr):
            if curr in avail: return True
            if curr in memo: return memo[curr]
            if curr not in adj: return False

            memo[curr] = False  # Assume we can't make it
            for ing in adj[curr]:
                if not dfs(ing):
                    return False
            
            avail.add(curr)  # Now we can cook this
            memo[curr] = True
            return True
        
        # Create graph
        for r, ing in zip(recipes, ingredients):
            adj[r] = ing
        
        return [r for r in recipes if dfs(r)]


        # Initialize tracking dictionaries using comprehensions
        can_make = dict.fromkeys(supplies, True)
        recipe_to_idx = {recipe: idx for idx, recipe in enumerate(recipes)}

        def _check_recipe(recipe: str, visited: set) -> bool:
            # Already processed and can be made
            if can_make.get(recipe, False):
                return True

            # Not a valid recipe or cycle detected
            if recipe not in recipe_to_idx or recipe in visited:
                return False

            visited.add(recipe)

            # Check if all ingredients can be made
            can_make[recipe] = all(
                _check_recipe(ingredient, visited)
                for ingredient in ingredients[recipe_to_idx[recipe]]
            )

            return can_make[recipe]

        # Process each recipe and collect those that can be made
        return [recipe for recipe in recipes if _check_recipe(recipe, set())]