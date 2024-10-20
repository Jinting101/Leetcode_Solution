class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        for c in expression:
            if c == "," or c == "(":
                continue
            if c in ["t", "f", "!", "&", "|"]:
                st.append(c)
            elif c == ")":
                has_true = False
                has_false = False
                while st[-1] not in ["!", "&", "|"]:
                    top_value = st.pop()
                    if top_value == "t":
                        has_true = True
                    elif top_value == "f":
                        has_false = True
                op = st.pop()
                if op == "!":
                    st.append("t" if not has_true else "f")
                elif op == "&":
                    st.append("f" if has_false else "t")
                else:
                    st.append("t" if has_true else "f")
        return st[-1] == "t"


# Initialize stack for operators & boolean values

# Traverse through expression:
    # If char is comma, or an open parenthesis, skip
    # If char is bool, or an operator, push to stack
    # If char is a closing parenthesis:
        # Initialize two boolean flags to track presence of true & false within the parentheses
        # Process values in parentheses:
            # While the top of stack is not an operator:
                # Pop from stack and check:
                    # If t: hasTrue
                    # If f: hasFalse
        # Pop operator from stack
        # Evaluate subexpression based on the operator:
            # If !, push f if hasTrue. Otherwise, push t.
            # If &, push f if hasFalse. Otherwise, push t.
            # If |, push t if hasTrue is true. Otherwise, push f.

# The final result will be at the top of the stack